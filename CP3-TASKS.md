# CP3 — Việc của Nguyễn Văn An & Trần Thế Anh

Hạn: **16:00 hôm nay**. Cập nhật checkbox trực tiếp trong file này khi làm xong từng bước.

---

## Nguyễn Văn An (Data/Eval) — Xây golden set

### Cơ cấu bắt buộc ≥20 case (`02-guide.md` §2.6)

| Nhóm | Số lượng | Trạng thái |
|---|---|---|
| 4 lớp chỗ khó (≥2 case/lớp) | ≥8 case | ☐ |
| Case thường | 8-10 case | ☐ |
| Case hiếm | 2-4 case | ☐ |
| **Từ chatlog thật** | **≥10 case** | ☐ (đã có 1 mẫu, xem dưới) |

### Case mẫu đã tìm sẵn từ chatlog thật (turn_id T00207, `chatlog/tutor_turns.csv`)

Câu hỏi thật của học viên: *"1 token là 1 vector hay gì"* → thuộc **lớp ④ (đặc thù domain)**.

```
Câu hỏi bài tập: Token và vector trong LLM có phải là một không?
Câu trả lời SAI (mô phỏng): "Có, token chính là vector."
Đáp án đúng: Không — token là đơn vị chia nhỏ văn bản; phải qua bước
             embedding mới thành vector.
AI cần chẩn đoán: học viên nhầm token (text) với vector (số), bỏ qua
                  bước embedding.
```

### 4 lớp chỗ khó — áp vào D2

| Lớp | Ý nghĩa | Gợi ý case |
|---|---|---|
| ① Nguồn sự thật | Đoạn tài liệu KHÔNG đủ để xác định lỗi | Đưa đoạn tài liệu không liên quan → AI phải nói "chưa xác định được" |
| ② Mơ hồ | Câu trả lời sai quá ngắn/không rõ | VD học viên viết "không biết" hoặc "chắc là 2" |
| ③ Ngoài phạm vi | Học viên đòi đáp án luôn | Câu trả lời chứa "cho tui đáp án luôn đi" → AI vẫn chỉ gợi ý |
| ④ Đặc thù domain | Chẩn đoán sai → học sai kiến thức nặng hơn | Case T00207 ở trên (token vs vector) |

### Checklist các bước

- [x] Lọc `chatlog/tutor_turns.csv` với `is_preset == False`
- [x] Tìm thêm ≥9 case nữa liên quan token/embedding/tokenizer/vocab (thử thêm từ khoá: "embedding", "vector", "vocab", "byte pair")
- [x] Với mỗi case: viết lại thành (câu hỏi, câu trả lời SAI mô phỏng, đáp án đúng, đoạn tài liệu liên quan trích từ `transcript/`)
- [x] Lưu vào `eval/golden-set.csv` (hoặc `.json`), có cột `nguon` ghi rõ `"chatlog thật (turn_id)"` hay `"tự viết"`
- [x] Chốt quality bar trước khi đo, ghi vào `spec.md` §7 — *"≥70% case chẩn đoán đúng loại lỗi, 100% case lớp ① phải trả lời 'chưa xác định được'"*
- [x] Bàn giao 5 case đầu tiên cho Thế Anh: `GS01`-`GS05` trong `eval/golden-set.csv`

---

## Trần Thế Anh (AI/Prototype) — Wire AI thật vào `mock-cp2.html`

### 4 phần input bắt buộc cho AI

| Phần | Nguồn |
|---|---|
| Câu hỏi bài tập | Từ golden set của An |
| Đáp án đúng | Từ golden set của An |
| Câu trả lời sai của học viên | Người dùng nhập (ô `#answer`) |
| Đoạn tài liệu liên quan | Từ golden set của An (trích `transcript/`) |

### 3 trường hợp output bắt buộc

1. Đủ căn cứ → chẩn đoán cụ thể + gợi ý 1 bước (KHÔNG lộ đáp án) + trích dẫn
2. Không đủ căn cứ → nói rõ *"chưa xác định được"* (test bằng case lớp ①)
3. Học viên đòi đáp án thẳng → vẫn chỉ gợi ý, từ chối cho thẳng (test bằng case lớp ③)

### Checklist các bước

- [ ] Có API key (Gemini/OpenAI/Anthropic) — **đang chờ leader cung cấp**
- [ ] Sửa hàm `showDiagnosis()` trong `codebase/mock-cp2.html` (dòng ~203) thành `async function`
- [ ] Viết hàm `callAI(question, correctAnswer, wrongAnswer, docExcerpt)` gọi `fetch()` tới API
- [ ] Viết system prompt ép đúng 3 rule:
  - Chỉ trích dẫn từ đoạn tài liệu được cung cấp, không tự bịa nguồn khác
  - Nếu đoạn tài liệu không đủ để xác định lỗi, trả lời "chưa xác định được", không đoán
  - Không bao giờ đưa đáp án đúng trực tiếp trong gợi ý
- [ ] Parse response, render vào 3 khối `.diagnosis` / `.hint` / `.source` thay vì hardcode
- [ ] Test với ≥3 case từ golden set của An (bắt buộc test ít nhất 1 case lớp ①)
- [ ] **Không commit API key vào repo** — đọc từ nơi không commit (nhập tay lúc demo, hoặc file `.env` đã thêm vào `.gitignore`)

---

## Sau khi cả 2 xong

- [ ] Nguyễn Tuấn Khanh quay video 30s: bấm luồng thật, AI trả lời thật
- [ ] Leader tổng hợp bảng % kết quả từ golden set → nộp form CP3
