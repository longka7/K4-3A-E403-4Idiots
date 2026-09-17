# Quick test script for D2 Prototype AI
# Run: python eval/quick_test.py

import urllib.request
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

# Đọc API key từ config.js hoặc .env
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

test_case_ids = [
    ('GS01', 'Lớp ①: Nguồn sự thật (Bắt buộc chẩn đoán "chưa xác định được")'),
    ('GS06', 'Lớp ③: Đòi đáp án (Bắt buộc từ chối và chỉ đưa gợi ý 1 bước)'),
    ('GS07', 'Lớp ④: Đặc thù domain (Bắt trúng lỗi nhầm token với vector)')
]

print("=" * 65, flush=True)
print("  KIỂM TRA ĐỘ HIỆU QUẢ CỦA AI CHẨN ĐOÁN LỖI (GEMINI 3.5 FLASH LITE)", flush=True)
print("=" * 65, flush=True)

def call_ai(payload):
    data = json.dumps(payload).encode('utf-8')
    # Thử qua các model đang online và có quota
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

for cid, title in test_case_ids:
    c = next(x for x in golden_set if x['case_id'] == cid)
    user_prompt = f"Câu hỏi bài tập: {c['cau_hoi_bai_tap']}\nĐáp án đúng: {c['dap_an_dung']}\nCâu trả lời của học viên: {c['cau_tra_loi_sai_mo_phong']}\nĐoạn tài liệu liên quan: {c['doc_excerpt']}"
    
    payload = {
        "contents": [{"role": "user", "parts": [{"text": system_prompt + "\n\n" + user_prompt}]}],
        "generationConfig": {"responseMimeType": "application/json", "temperature": 0.1}
    }
    
    try:
        res, model_used = call_ai(payload)
        
        print(f"\n▶ [{cid}] {title} (Model: {model_used})", flush=True)
        print(f"  • Câu hỏi:          {c['cau_hoi_bai_tap']}", flush=True)
        print(f"  • Học viên trả lời: {c['cau_tra_loi_sai_mo_phong']}", flush=True)
        print(f"  • AI Chẩn đoán:     {res.get('chan_doan')}", flush=True)
        print(f"  • AI Gợi ý:         {res.get('goi_y')}", flush=True)
        print(f"  • Trích đoạn:       {res.get('trich_dan')}", flush=True)
        
        # Đánh giá tiêu chí
        if cid == 'GS01':
            passed = 'chưa xác định được' in res.get('chan_doan', '').lower()
            print(f"  ==> Đánh giá: {'✅ ĐẠT (Chẩn đoán chính xác: \"chưa xác định được\")' if passed else '❌ CHƯA ĐẠT'}", flush=True)
        elif cid == 'GS06':
            passed = 'không' in res.get('goi_y', '').lower() or 'từ chối' in res.get('goi_y', '').lower() or 'bạn hãy' in res.get('goi_y', '').lower() or 'thử' in res.get('goi_y', '').lower()
            print(f"  ==> Đánh giá: {'✅ ĐẠT (Từ chối đưa đáp án & hướng dẫn tự kiểm tra)' if passed else '❌ CHƯA ĐẠT'}", flush=True)
        elif cid == 'GS07':
            passed = 'vector' in res.get('chan_doan', '').lower() and 'token' in res.get('chan_doan', '').lower()
            print(f"  ==> Đánh giá: {'✅ ĐẠT (Chẩn đoán đúng lỗi bản chất: token vs vector)' if passed else '❌ CHƯA ĐẠT'}")
    except Exception as e:
        print(f"\n▶ [{cid}] {title} -> Lỗi: {e}", flush=True)
    time.sleep(1)

print("\n" + "=" * 65, flush=True)
print("Hoàn tất kiểm tra!", flush=True)
