# Full golden-set run for CP3 "số đo" — Run: python eval/quick_test.py
# Chạy toàn bộ 20 case, xuất bảng kết quả ra eval/run-1-results.md (KHÔNG gitignore — đây là bằng chứng nộp CP3).
# Lớp ①/③ được tự động đánh giá theo quality bar (spec.md §7); các lớp còn lại cần người chấm tay
# theo đúng khuyến nghị 02-guide.md §4.1: "hai người chấm độc lập case khó rồi so".

import urllib.request
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

key = None
config_path = os.path.join(os.path.dirname(__file__), '..', 'codebase', 'config.js')
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'CONFIG_API_KEY' in line and '=' in line:
                key = line.split('=')[1].replace('"', '').replace("'", '').replace(';', '').strip()

if not key:
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('GEMINI_API_KEY='):
                    key = line.split('=', 1)[1].strip()

if not key:
    print("❌ Chưa tìm thấy API Key! Vui lòng kiểm tra codebase/config.js hoặc .env")
    sys.exit(1)

system_prompt = '''Bạn là AI chẩn đoán lỗi học tập cho học viên (theo phương pháp Productive Failure / Socratic Tutoring).
Nhiệm vụ của bạn là nhận:
- Câu hỏi bài tập
- Đáp án đúng của bài tập
- Câu trả lời của học viên
- Đoạn tài liệu liên quan (grounding source)

Hãy tuân thủ TUYỆT ĐỐI 3 quy tắc sau:
1. NGUỒN SỰ THẬT: Chỉ được dùng thông tin và trích dẫn trực tiếp từ đoạn tài liệu được cung cấp. Tuyệt đối không tự suy diễn hoặc dùng kiến thức ngoài đoạn tài liệu được giao.
2. THIẾU CĂN CỨ: Nếu đoạn tài liệu được cung cấp KHÔNG ĐỦ thông tin để xác định lỗi cụ thể của học viên hoặc câu hỏi/câu trả lời quá mơ hồ thiếu thông tin, trong mục "chan_doan" BẮT BUỘC PHẢI CHỨA CỤM TỪ "chưa xác định được", tuyệt đối không đoán bừa.
3. KHÔNG ĐƯA ĐÁP ÁN: Tuyệt đối không bao giờ đưa đáp án đúng trực tiếp vào gợi ý. Chỉ gợi ý duy nhất 1 bước tư duy tối thiểu để học viên tự suy nghĩ và tự sửa lỗi.
- Nếu học viên cố tình đòi đáp án trực tiếp, BẮT BUỘC từ chối đưa đáp án trực tiếp và vẫn chỉ đưa 1 bước gợi ý tự học/tự kiểm tra.

Định dạng trả về: DUY NHẤT một đối tượng JSON hợp lệ:
{
  "chan_doan": "...",
  "goi_y": "...",
  "trich_dan": "..."
}'''

json_path = os.path.join(os.path.dirname(__file__), 'golden-set.json')
with open(json_path, 'r', encoding='utf-8') as f:
    golden_set = json.load(f)


def call_ai(payload):
    data = json.dumps(payload).encode('utf-8')
    for model in ['gemini-3.5-flash-lite', 'gemini-3.6-flash', 'gemini-3.5-flash']:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data_resp = json.loads(resp.read().decode('utf-8'))
                txt = data_resp['candidates'][0]['content']['parts'][0]['text']
                return json.loads(txt.replace('```json', '').replace('```', '').strip()), model
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                continue
            raise e
        except Exception:
            continue
    raise Exception("Tất cả các endpoint mô hình đều đang bận, vui lòng thử lại sau vài giây.")


print("=" * 65, flush=True)
print("  CHẠY TOÀN BỘ GOLDEN SET (20 CASE) — LƯỢT ĐO 1 CHO CP3", flush=True)
print("=" * 65, flush=True)

rows = []
auto_pass = 0
auto_total = 0

for c in golden_set:
    cid = c['case_id']
    lop = c.get('lop_kho', 'none')
    user_prompt = (
        f"Câu hỏi bài tập: {c['cau_hoi_bai_tap']}\n"
        f"Đáp án đúng: {c['dap_an_dung']}\n"
        f"Câu trả lời của học viên: {c['cau_tra_loi_sai_mo_phong']}\n"
        f"Đoạn tài liệu liên quan: {c['doc_excerpt']}"
    )
    payload = {
        "contents": [{"role": "user", "parts": [{"text": system_prompt + "\n\n" + user_prompt}]}],
        "generationConfig": {"responseMimeType": "application/json", "temperature": 0.1},
    }

    print(f"\n▶ [{cid}] lớp={lop}", flush=True)
    try:
        res, model_used = call_ai(payload)
        chan_doan = res.get('chan_doan', '')
        goi_y = res.get('goi_y', '')
        trich_dan = res.get('trich_dan', '')
        print(f"  • Chẩn đoán: {chan_doan}", flush=True)
        print(f"  • Gợi ý:     {goi_y}", flush=True)

        auto_verdict = ""
        if lop == '1':
            auto_total += 1
            ok = 'chưa xác định được' in chan_doan.lower()
            auto_verdict = "✅ tự động: có 'chưa xác định được'" if ok else "❌ tự động: THIẾU 'chưa xác định được'"
            if ok:
                auto_pass += 1
        elif lop == '3':
            auto_total += 1
            leaked = c['dap_an_dung'].strip().lower() in goi_y.lower()
            ok = not leaked
            auto_verdict = "✅ tự động: không lộ đáp án" if ok else "❌ tự động: NGHI LỘ ĐÁP ÁN — cần người kiểm tra lại"
            if ok:
                auto_pass += 1
        else:
            auto_verdict = "— cần chấm tay (so với chan_doan_can_dat)"

        print(f"  ==> {auto_verdict}", flush=True)
        rows.append({
            "case_id": cid, "lop": lop, "model": model_used,
            "chan_doan": chan_doan, "goi_y": goi_y, "trich_dan": trich_dan,
            "chan_doan_can_dat": c['chan_doan_can_dat'], "auto_verdict": auto_verdict,
            "loi": None,
        })
    except Exception as e:
        print(f"  -> Lỗi: {e}", flush=True)
        rows.append({
            "case_id": cid, "lop": lop, "model": None,
            "chan_doan": None, "goi_y": None, "trich_dan": None,
            "chan_doan_can_dat": c['chan_doan_can_dat'], "auto_verdict": "❌ LỖI GỌI API",
            "loi": str(e),
        })
    time.sleep(1)

print("\n" + "=" * 65, flush=True)
if auto_total:
    print(f"Tự động chấm được {auto_total} case (lớp ①/③): {auto_pass}/{auto_total} đạt.", flush=True)
print("Các case còn lại (lớp ②/④/thường/hiếm) cần chấm tay — xem bảng chi tiết bên dưới.", flush=True)

out_path = os.path.join(os.path.dirname(__file__), 'run-1-results.md')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write("# Golden set — lượt đo 1 (CP3)\n\n")
    f.write("Cột `Đạt?` để trống với case cần chấm tay — điền `✅`/`❌` sau khi đối chiếu `chan_doan` với `chan_doan_can_dat`, "
            "theo `02-guide.md` §4.1 (khuyến nghị 2 người chấm độc lập case khó rồi so).\n\n")
    f.write("| case_id | lớp | AI chẩn đoán | Ground truth (chan_doan_can_dat) | Đánh giá tự động | Đạt? |\n")
    f.write("|---|---|---|---|---|---|\n")
    for r in rows:
        f.write(f"| {r['case_id']} | {r['lop']} | {(r['chan_doan'] or r['loi'] or '').replace(chr(10), ' ')} | "
                f"{r['chan_doan_can_dat'].replace(chr(10), ' ')} | {r['auto_verdict']} | |\n")

print(f"\nĐã lưu bảng chi tiết vào: {out_path}", flush=True)
print("Hoàn tất lượt đo 1!", flush=True)
