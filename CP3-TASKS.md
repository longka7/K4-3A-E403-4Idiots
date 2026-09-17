# CP3 — Việc của Nguyễn Văn An & Trần Thế Anh

Hạn: **16:00 hôm nay**. Cập nhật checkbox trực tiếp trong file này khi làm xong từng bước.

> ⚠️ **ĐỔI VAI (17/9, đã xác nhận với leader):** Thế Anh đã làm xong phần Data/Eval (golden set — xem dưới, đã verify 12/12 turn_id thật). **Từ giờ An chuyển sang làm phần AI/Prototype** (wire AI thật) — xem checklist ở mục thứ 2. Thế Anh coi như xong phần của mình.

---

## ✅ ĐÃ XONG — Golden set (ban đầu giao An, Thế Anh đã làm)

### Cơ cấu bắt buộc ≥20 case (`02-guide.md` §2.6)

| Nhóm                        | Số lượng                                           | Trạng thái                       |
| --------------------------- | -------------------------------------------------- | -------------------------------- |
| 4 lớp chỗ khó (≥2 case/lớp) | 8 case (đúng 2/lớp)                                | ✅                               |
| Case thường                 | 8 case                                             | ✅                               |
| Case hiếm                   | 4 case                                             | ✅                               |
| **Từ chatlog thật**         | **12/20 case** — đã verify đúng 12/12 turn_id thật | ✅ vượt chuẩn                    |
| **Tổng**                    | **20 case**                                        | ✅ — file: `eval/golden-set.csv` |

### Case mẫu đã tìm sẵn từ chatlog thật (turn_id T00207, `chatlog/tutor_turns.csv`)

Câu hỏi thật của học viên: _"1 token là 1 vector hay gì"_ → thuộc **lớp ④ (đặc thù domain)**.

```
Câu hỏi bài tập: Token và vector trong LLM có phải là một không?
Câu trả lời SAI (mô phỏng): "Có, token chính là vector."
Đáp án đúng: Không — token là đơn vị chia nhỏ văn bản; phải qua bước
             embedding mới thành vector.
AI cần chẩn đoán: học viên nhầm token (text) với vector (số), bỏ qua
                  bước embedding.
```

### 4 lớp chỗ khó — áp vào D2

| Lớp              | Ý nghĩa                                    | Gợi ý case                                                           |
| ---------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| ① Nguồn sự thật  | Đoạn tài liệu KHÔNG đủ để xác định lỗi     | Đưa đoạn tài liệu không liên quan → AI phải nói "chưa xác định được" |
| ② Mơ hồ          | Câu trả lời sai quá ngắn/không rõ          | VD học viên viết "không biết" hoặc "chắc là 2"                       |
| ③ Ngoài phạm vi  | Học viên đòi đáp án luôn                   | Câu trả lời chứa "cho tui đáp án luôn đi" → AI vẫn chỉ gợi ý         |
| ④ Đặc thù domain | Chẩn đoán sai → học sai kiến thức nặng hơn | Case T00207 ở trên (token vs vector)                                 |

### Checklist các bước

- [x] Lọc `chatlog/tutor_turns.csv` với `is_preset == False`
- [x] Tìm thêm ≥9 case nữa liên quan token/embedding/tokenizer/vocab (thử thêm từ khoá: "embedding", "vector", "vocab", "byte pair")
- [x] Với mỗi case: viết lại thành (câu hỏi, câu trả lời SAI mô phỏng, đáp án đúng, đoạn tài liệu liên quan trích từ `transcript/`)
- [x] Lưu vào `eval/golden-set.csv` (hoặc `.json`), có cột `nguon` ghi rõ `"chatlog thật (turn_id)"` hay `"tự viết"`
- [x] Chốt quality bar trước khi đo, ghi vào `spec.md` §7 — _"≥70% case chẩn đoán đúng loại lỗi, 100% case lớp ① phải trả lời 'chưa xác định được'"_
- [x] Bàn giao toàn bộ 20 case cho An: `eval/golden-set.csv`

---

## 🔴 Nguyễn Văn An (nhận lại AI/Prototype) — Wire AI thật vào `mock-cp2.html`

### 4 phần input bắt buộc cho AI

⚠️ **Chỉ AI #2 (chẩn đoán lỗi) — KHÔNG phải AI #1 (sinh trắc nghiệm/tự luận, đó là phần mở rộng không bắt buộc CP3).** 4 input này lấy thẳng từ `eval/golden-set.csv` (hoặc `eval/golden-set.json`), không cần dựng thêm bộ dữ liệu nào khác:

| Phần                         | Nguồn                                                                                  | Cột trong golden-set       |
| ---------------------------- | -------------------------------------------------------------------------------------- | -------------------------- |
| Câu hỏi bài tập              | `eval/golden-set.csv`                                                                  | `cau_hoi_bai_tap`          |
| Đáp án đúng                  | `eval/golden-set.csv`                                                                  | `dap_an_dung`              |
| Câu trả lời sai của học viên | Khi test: cột `cau_tra_loi_sai_mo_phong`. Khi demo thật: người dùng nhập (ô `#answer`) | `cau_tra_loi_sai_mo_phong` |
| Đoạn tài liệu liên quan      | `eval/golden-set.csv`                                                                  | `doc_excerpt`              |

So output AI với cột `chan_doan_can_dat` để chấm đúng/sai khi chạy golden set.

### 3 trường hợp output bắt buộc

1. Đủ căn cứ → chẩn đoán cụ thể + gợi ý 1 bước (KHÔNG lộ đáp án) + trích dẫn
2. Không đủ căn cứ → nói rõ _"chưa xác định được"_ (test bằng case lớp ①)
3. Học viên đòi đáp án thẳng → vẫn chỉ gợi ý, từ chối cho thẳng (test bằng case lớp ③)

### Checklist các bước

- [x] Có API key (Gemini/OpenAI/Anthropic) — **đã nhận key Gemini và cấu hình bảo mật**
- [x] Sửa hàm `showDiagnosis()` trong `codebase/mock-cp2.html` (dòng ~203) thành `async function`
- [x] Viết hàm `callAI(question, correctAnswer, wrongAnswer, docExcerpt)` gọi `fetch()` tới API
- [x] Viết system prompt ép đúng 3 rule:
  - Chỉ trích dẫn từ đoạn tài liệu được cung cấp, không tự bịa nguồn khác
  - Nếu đoạn tài liệu không đủ để xác định lỗi, trả lời "chưa xác định được", không đoán
  - Không bao giờ đưa đáp án đúng trực tiếp trong gợi ý
- [x] Parse response, render vào 3 khối `.diagnosis` / `.hint` / `.source` thay vì hardcode
- [x] Test với ≥3 case từ `eval/golden-set.csv` (bắt buộc test ít nhất 1 case lớp ①) — đã test các case GS01 (lớp ①), GS02 (lớp ①), GS03 (lớp ②), GS04 (lớp ②), GS05 (lớp ③), GS06 (lớp ③), GS07 (lớp ④), GS08 (lớp ④) đạt chuẩn 100%
- [x] **Không commit API key vào repo** — đọc từ nơi không commit (nhập tay lúc demo, hoặc file `.env` / `config.js` đã thêm vào `.gitignore`)

### Code mẫu — load golden set + gọi AI

Đã convert sẵn `eval/golden-set.json` (mảng object, dễ dùng trong JS hơn CSV — không bắt buộc, chỉ để tiện):

````js
async function loadGoldenSet() {
  const res = await fetch("eval/golden-set.json");
  return res.json(); // mảng 20 object, mỗi object có: cau_hoi_bai_tap, cau_tra_loi_sai_mo_phong, dap_an_dung, chan_doan_can_dat, doc_excerpt, lop_kho, ...
}

async function callAI(question, correctAnswer, wrongAnswer, docExcerpt) {
  const systemPrompt = `Bạn là AI chẩn đoán lỗi học tập. Chỉ dùng đoạn tài liệu được cung cấp — không bịa nguồn khác.
Nếu đoạn tài liệu không đủ để xác định lỗi cụ thể, trả lời "chưa xác định được", không đoán.
Không bao giờ đưa đáp án đúng trực tiếp trong gợi ý.
Trả về JSON: {"chan_doan": "...", "goi_y": "...", "trich_dan": "..."}`;

  const userPrompt = `Câu hỏi: ${question}\nĐáp án đúng: ${correctAnswer}\nCâu trả lời của học viên: ${wrongAnswer}\nĐoạn tài liệu liên quan: ${docExcerpt}`;

  const res = await fetch(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + API_KEY,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text: systemPrompt + "\n\n" + userPrompt }] }],
      }),
    },
  );
  const data = await res.json();
  const text = data.candidates[0].content.parts[0].text;
  return JSON.parse(text.replace(/```json|```/g, "").trim());
}

// Test nhanh 1 case từ golden set (vd GS07, lớp ④):
const cases = await loadGoldenSet();
const c = cases.find((x) => x.case_id === "GS07");
const result = await callAI(c.cau_hoi_bai_tap, c.dap_an_dung, c.cau_tra_loi_sai_mo_phong, c.doc_excerpt);
console.log(result, "— so với chan_doan_can_dat:", c.chan_doan_can_dat);
````

Đây chỉ là khung mẫu (dùng Gemini làm ví dụ) — An sửa lại theo API/key thật khi có.

---

## Sau khi cả 2 xong

- [ ] Nguyễn Tuấn Khanh quay video 30s: bấm luồng thật, AI trả lời thật
- [ ] Leader tổng hợp bảng % kết quả từ golden set → nộp form CP3
