# Template AI Spec *(spec.md — commit trước hạn chốt spec: 21:00 17/9, tại CP4 · quality bar chốt từ thời điểm nộp)*

> Cấu trúc phủ đúng "SPEC 8 phần" của chương trình: Bằng chứng (§1-§2) · Lát cắt (§4) · Canvas (đính kèm CP1) · Augment/Automate (§4) · 4 đường đi của trải nghiệm (§6) · Kiểu lỗi (§5) · Kiểm thử (§7) · Phân công (§8). Hướng dẫn viết từng mục: `02-guide.md`.

```markdown
# AI SPEC — Học từ lỗi trước (Productive Failure) · Nhóm 4Idiots · Phòng E403
Hướng: [x] D — Học tập thích ứng & tương tác (đề D2)
Loại: [x] Tính năng mới

## §1. User & Job
- Job executor: Một học viên K4 đang làm bài tập/quiz sau khi vừa học một đoạn lý thuyết trên VLearn.
- Core JTBD: Làm bài tập, sai một câu, rồi tự tìm hiểu đúng chỗ mình hiểu nhầm để sửa. *(bỏ chữ "AI" khỏi câu — việc này vẫn tồn tại, đúng chuẩn JTBD)*
- Problem statement (KHÔNG chữ AI): Khi học viên làm sai bài tập, hệ thống hiện tại chỉ báo "sai rồi, đáp án là..." mà không chỉ ra đúng chỗ giả định sai của riêng học viên đó — khiến học viên phải tự tua lại toàn bộ bài giảng để tìm ra lỗi, tốn thời gian và có thể hiểu sai lại.
- Evidence (chuẩn A — khảo sát):
  - Số liệu khảo sát (n = ?, % xác nhận): ⏳ CHỜ TV2 — điền từ `research/survey-d2.md` sau khi đủ khảo sát (ít nhất vài người cho CP1, ≥20 người trước CP4)
  - ≥5 quote/ví dụ nguyên văn + nguồn: ⏳ CHỜ TV2 — lấy nguyên văn cột "Câu chốt"/"Ghi chú" trong bảng log

## §2. Impact & quyết định chọn
- Bảng impact ≥3 ứng viên:

  | Ứng viên | Bao nhiêu người gặp | Tần suất | Mỗi lần tốn gì | Build nổi trong 3 buổi? | Chọn? |
  |---|---|---|---|---|---|
  | **D2 — Học từ lỗi trước** | ⏳ chờ khảo sát | Mỗi lần làm sai bài tập | Thời gian tua lại lý thuyết + rủi ro hiểu sai lại | Có — 1 luồng chẩn đoán lỗi + gợi ý, giới hạn 1 concept | **✅ Chọn** |
  | D1 — Lớp học mô phỏng đa tác tử | ⏳ chờ khảo sát | Mỗi buổi học | Không có bạn học/TA để hỏi ngược | Khó — cần ≥2 agent phối hợp, rủi ro cao trong thời gian ngắn | Loại — quá tham vọng cho 47.5h |
  | D3 — Học bằng cách dạy lại | ⏳ chờ khảo sát | Sau mỗi buổi học | Không ai để dạy lại, không tự biết hiểu đúng chưa | Có, nhưng khó đo "đã hiểu sâu hơn" hơn D2 | Loại — D2 đo "học được" rõ ràng hơn (đúng/sai bài tập) |
  | A1 — Tối ưu tutor VLearn hiện có | Có sẵn data lớn (13.494 lượt hỏi) | Rất cao | Câu trả lời không căn cứ/không đúng cỡ | Dễ nhất — data sẵn | Loại — không thuộc track D, và không đo được "học được" theo yêu cầu riêng của track D |

  *(Cột "bao nhiêu người gặp/tần suất" cập nhật bằng số thật từ khảo sát trước CP4 — hiện đang là ước lượng định tính, cần thay bằng số đếm được.)*

- Ứng viên ĐÃ LOẠI + vì sao: D1 (rủi ro kỹ thuật cao, đa tác tử khó demo gọn 5 phút), D3 (khó đo mức hiểu sâu hơn bằng chỉ số khách quan), A1 (không thuộc track D, không có yêu cầu đo "học được" như D2).
- Ứng viên CHỌN + vì sao: D2 — vì có thể đo trực tiếp "học được" bằng đúng/sai bài tập trước/sau (đúng yêu cầu riêng của track D), và lát cắt nhỏ (1 concept, 1 lần sai) build nổi trong thời gian sự kiện.

## §3. Giải pháp tương tự đã nghiên cứu
- ⏳ CHỜ — mỗi thành viên dùng thử 1 sản phẩm gần giống (ChatGPT study mode / Khanmigo / Duolingo / Quizlet AI) và trả lời 4 câu theo `02-guide.md` §2.2 (15 phút/người).

## §4. Thiết kế
- Lát cắt MỘT CÂU: *Một học viên · làm bài tập về một khái niệm (VD tokenization) trước khi xem bài giảng, làm sai · AI chẩn đoán đúng giả định sai cụ thể của học viên và gợi ý một bước tối thiểu kèm đoạn tài liệu liên quan (không đưa đáp án ngay) · học viên tự sửa và giải thích lại được khái niệm.*
- Non-goals (KHÔNG build trong hackathon):
  1. Không xây bộ misconception bank đầy đủ cho cả môn — chỉ 1 concept demo.
  2. Không làm giao diện hoàn chỉnh — mock/sketch đủ để bấm qua luồng.
  3. Không theo dõi lịch sử lỗi nhiều buổi/thích ứng dài hạn — chỉ 1 lượt sai → 1 lượt sửa.
- Mức prototype nhắm tới: [ ] Sketch [x] Mock — phần chẩn đoán lỗi gọi AI thật (bắt buộc ≥1 lời gọi thật), phần giao diện có thể mock.
- Automation: [x] conditional — AI chỉ dừng ở "chẩn đoán lỗi cụ thể + gợi ý 1 bước + trích dẫn tài liệu", KHÔNG tự đưa đáp án đúng ngay. Lý do theo cost-of-error: nếu AI đưa đáp án ngay thì mất tác dụng productive failure (học viên không tự kiến tạo); nếu AI chẩn đoán sai lỗi mà vẫn "chắc chắn" thì học viên tin sai — nên luôn trích dẫn nguồn (transcript/slide) để học viên tự đối chiếu, không yêu cầu tin mù AI.
- §4b. Nguyên tắc đã áp dụng: ⏳ CHỜ — chọn ≥4 nguyên tắc từ HAX/PAIR (`further-reading/`) và điền bảng, áp cụ thể vào từng bước của luồng D2.

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản (≥8)
⏳ CHỜ — áp 4 lớp theo `01-challenge-brief.md`:
① Nguồn sự thật (AI bịa lỗi không có thật?) · ② Mơ hồ (học viên trả lời/giải thích mơ hồ, AI đoán hay hỏi lại?) · ③ Ngoài phạm vi (học viên đòi AI cho đáp án luôn?) · ④ Đặc thù domain (chẩn đoán sai lỗi → học viên học sai kiến thức ngay — hậu quả nặng nhất).

## §6. Bốn đường đi của trải nghiệm
⏳ CHỜ điền cụ thể theo prototype thật — khung tham khảo:
- Happy path: học viên làm sai → AI chẩn đoán đúng → gợi ý → học viên tự sửa đúng.
- Low-confidence (②): học viên giải thích mơ hồ → AI hỏi lại thay vì đoán.
- Failure/không căn cứ (①): AI không chắc lỗi ở đâu → nói rõ "chưa xác định được", không bịa.
- Correction: học viên tự nhận ra và sửa câu trả lời trước → AI cập nhật theo câu mới nhất.
- Khi bị đòi ngoài phạm vi (③): học viên đòi đáp án ngay → AI từ chối đưa thẳng, nhắc lại mục đích tự sửa.
- Case đặc thù domain (④): AI chẩn đoán nhầm loại lỗi → có cơ chế học viên phản hồi "không đúng vậy" để AI thử lại.

## §7. Kiểm thử
- Chiều chất lượng: chẩn đoán đúng loại lỗi (không chỉ đúng/sai đáp án) + gợi ý tối thiểu (không lộ đáp án) + có trích dẫn tài liệu.
- Golden set (≥20 case, file trong `eval/`): ⏳ CHỜ TV2 — mining lỗi thường gặp từ chatlog/transcript trong `data/vlearn-pack/`.
- Quality bar: ⏳ CHỜ chốt bằng số cụ thể trước 21:00 17/9 (CP4) — VD "≥70% case chẩn đoán đúng loại lỗi, 100% không lộ đáp án trực tiếp".
- Kết quả các lượt chạy: ⏳ điền sau khi có prototype (từ CP3).

## §8. Phân công & kế hoạch
- Phân công có tên:
  | Vai trò | Người | Việc chính |
  |---|---|---|
  | Leader + BA | Nguyễn Long Khánh | Canvas, spec.md (§1-§2 evidence/impact), điều phối, nộp 5 mốc CP |
  | Data/Eval | ⏳ TV2 — cần tên | Khảo sát D2, mining lỗi thường gặp, golden set (§7) |
  | AI/Prototype | ⏳ TV3 — cần tên | Build luồng chẩn đoán lỗi (≥1 lời gọi AI thật), `codebase/` |
  | UX/Validation | ⏳ TV4 — cần tên | Mock/flow CP2, video CP3/CP5, R6 (≥5 người dùng thử thật) |
- Willing users (≥3 tên — cần cho CP1 và R6): ⏳ CHỜ TV3.

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào) |
|---|---|---|
| CP1 | Khởi tạo spec từ Canvas draft | Chuẩn bị nộp CP1 |
```
