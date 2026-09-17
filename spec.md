# Template AI Spec *(spec.md — commit trước hạn chốt spec: 21:00 17/9, tại CP4 · quality bar chốt từ thời điểm nộp)*

> Cấu trúc phủ đúng "SPEC 8 phần" của chương trình: Bằng chứng (§1-§2) · Lát cắt (§4) · Canvas (đính kèm CP1) · Augment/Automate (§4) · 4 đường đi của trải nghiệm (§6) · Kiểu lỗi (§5) · Kiểm thử (§7) · Phân công (§8). Hướng dẫn viết từng mục: `02-guide.md`.

```markdown
# AI SPEC — Học từ lỗi trước (Productive Failure) · Nhóm 4Idiots · Phòng E403
Hướng: [x] D — Học tập thích ứng & tương tác (đề D2)
Loại: [x] Tính năng mới

## §1. User & Job
- Job executor: Một học viên K4 đang làm bài tập/quiz sau khi vừa học một đoạn lý thuyết trên VLearn.
- Core JTBD: Làm bài tập, sai một câu, rồi tự tìm hiểu đúng chỗ mình hiểu nhầm để sửa.
- Problem statement (KHÔNG chữ AI): Khi học viên làm sai bài tập, hệ thống hiện tại chỉ báo "sai rồi, đáp án là..." mà không chỉ ra đúng chỗ giả định sai của riêng học viên đó — khiến học viên phải tự tua lại toàn bộ bài giảng để tìm ra lỗi, tốn thời gian và có thể hiểu sai lại.
- Evidence (chuẩn A — khảo sát, Google Form `KhaoSat.xlsx`, 16/9/2026):
  - Số liệu khảo sát: **n = 23, 14/23 xác nhận pain = 60.9%** — đạt chuẩn Đường A (≥20 người, ≥50% xác nhận). Phương pháp xác nhận pain: đếm người rơi vào ≥1 trong 3 dấu hiệu sau (theo `research/survey-d2.md`):
    - Q2 (mất ≥5 phút hiểu vì sao sai): 6/23
    - Q3 (quên gần hết lý thuyết, phải xem lại gần như toàn bộ): 5/23
    - Q5 (đáp án chỉ nói "sai rồi..." không giải thích chỗ hiểu nhầm): 11/23 — **dấu hiệu mạnh nhất, đúng trọng tâm bài toán D2**
  - Quote nguyên văn (câu 7 — đánh giá hiệu quả tự học hiện tại):
    1. *"trung bình khá thôi, mình nghĩ vẫn cần có sự hướng dẫn từ phía con người"*
    2. *"Chưa tốt lắm"*
    3. *"Hơi chuối"*
    4. *"Tương đối khó hiểu, bài tập khó"*
    5. *"Chất lưong video hít or miss, chất luong bài tập tệ"*
    6. *"Không áp dụng cách học này"*
  - ⚠️ Lưu ý minh bạch: form hiện ẩn danh (không ghi tên người trả lời) — đủ chuẩn vì có timestamp thật, nhưng nếu còn thời gian nên thêm ô tên/mã HV (không bắt buộc) cho các lượt sau để log đầy đủ hơn theo `02-guide.md` §1.3.

## §2. Impact & quyết định chọn
- Bảng impact ≥3 ứng viên:

  | Ứng viên | Bao nhiêu người gặp | Tần suất | Mỗi lần tốn gì | Build nổi trong 3 buổi? | Chọn? |
  |---|---|---|---|---|---|
  | **D2 — Học từ lỗi trước** | 14/23 khảo sát (60.9%) xác nhận pain; riêng dấu hiệu "đáp án không giải thích chỗ sai" là 11/23 (47.8%) | Ước lượng 3 lần sai trong một bộ 10 câu | Mỗi lần mất khoảng 5 phút để tìm nguyên nhân (6/23 gặp pain này), tương đương khoảng 15 phút/bộ; 5/23 còn phải xem lại gần như toàn bộ lý thuyết | Có — 1 luồng chẩn đoán lỗi + gợi ý, giới hạn trong 1 khái niệm kiến thức | **✅ Chọn** |
  | D1 — Lớp học mô phỏng đa tác tử | Chưa khảo sát riêng | Mỗi buổi học | Thời gian tra cứu, liên hệ giảng viên lab coach để được giải đáp thắc mắc | Khó — cần ≥2 agent phối hợp, rủi ro cao trong thời gian ngắn | Loại — quá tham vọng cho 47.5h |
  | D3 — Học bằng cách dạy lại | Chưa khảo sát riêng | Sau mỗi buổi học | Rủi ro hiểu sai kiến thức do Không có ai để dạy lại | Có, nhưng khó đo "đã hiểu sâu hơn" hơn D2 | Loại — D2 đo "học được" rõ ràng hơn (đúng/sai bài tập) |
  | A1 — Tối ưu tutor VLearn hiện có | Có sẵn data lớn (13.494 lượt hỏi) | Chưa kiểm tra | Câu trả lời không căn cứ/không đúng cỡ | Dễ nhất — data sẵn | Loại — không thuộc track D, và không đo được "học được" theo yêu cầu riêng của track D |

  *(Nguồn: khảo sát Google Form 23 phản hồi, 16/9/2026 — xem `spec.md` §1 và file gốc `KhaoSat.xlsx`. D1/D3 chưa có khảo sát riêng vì nhóm chọn D2 ngay từ đầu dựa trên đánh giá định tính; nếu giám khảo hỏi, nêu rõ đây là giới hạn thời gian, không phải bỏ qua bước so sánh.)*

- Ứng viên ĐÃ LOẠI + vì sao: D1 (rủi ro kỹ thuật cao, đa tác tử khó demo gọn 5 phút), D3 (khó đo mức hiểu sâu hơn bằng chỉ số khách quan), A1 (không thuộc track D, không có yêu cầu đo "học được" như D2).
- Ứng viên CHỌN + vì sao (giải thích kèm số): D2 — ảnh hưởng được lượng hóa bằng 14/23 người (60.9%) gặp pain × khoảng 3 lần sai/bộ 10 câu × khoảng 5 phút tìm nguyên nhân mỗi lần = khoảng 15 phút/bộ/người gặp pain; 6/23 người (26.1%) xác nhận mất từ 5 phút để hiểu vì sao sai, và 5/23 người (21.7%) phải xem lại gần như toàn bộ lý thuyết. D2 cũng đo trực tiếp "học được" bằng đúng/sai bài tập trước/sau (đúng yêu cầu riêng của track D), trong phạm vị kiến thức nhỏ (1 khái niệm trong day 1), 1 lần sai nên build được trong thời gian sự kiện.

## §3. Giải pháp tương tự đã nghiên cứu
- ⏳ CHỜ — mỗi thành viên dùng thử 1 sản phẩm gần giống (ChatGPT study mode / Khanmigo / Duolingo / Quizlet AI) và trả lời 4 câu theo `02-guide.md` §2.2 (15 phút/người).

## §4. Thiết kế
- Lát cắt MỘT CÂU: *Một học viên · làm bài tập về một khái niệm (VD tokenization) trước khi xem bài giảng và trả lời sai · AI chẩn đoán nguyên nhân hiểu sai, không cho đáp án ngay mà tạo câu hỏi khoanh vùng lỗi kèm gợi ý tối thiểu và dẫn chứng về khái niệm liên quan · học viên tự sửa và giải thích lại được khái niệm.*
- Non-goals (KHÔNG build trong hackathon):
  1. Không xây bộ misconception bank đầy đủ cho cả môn — chỉ 1 concept demo.
  2. Không làm giao diện hoàn chỉnh — mock/sketch đủ để bấm qua luồng.
  3. Không theo dõi lịch sử lỗi nhiều buổi/thích ứng dài hạn — chỉ 1 lượt sai → 1 lượt sửa.
- Mức prototype nhắm tới: [ ] Sketch [x] Mock — phần chẩn đoán lỗi gọi AI thật (bắt buộc ≥1 lời gọi thật), phần giao diện có thể mock.
- Automation: [x] conditional — AI luôn tạo ra 1 bộ câu hỏi, nhưng chỉ dừng ở bước hỗ trợ "tạo câu hỏi khoanh vùng lỗi sai + gợi ý 1 bước + trích dẫn tài liệu", học viên tự đưa ra đáp án. AI cũng sẽ không bao giờ tự quyết định rằng học viên đã hiểu đúng khái niệm chỉ sau 1 câu hỏi mà sẽ luôn confirm lại bằng 1 câu hỏi khác với mức độ thông hiểu cao hơn. Lý do theo cost-of-error: nếu AI chẩn đoán sai lỗi mà vẫn "chắc chắn" thì học viên tin sai — nên luôn trích dẫn nguồn (transcript/slide) để học viên tự đối chiếu, không yêu cầu tin mù AI; Đồng thời AI không mặc định học viên đã nắm được khái niệm chỉ sau 1 lần trả lời đúng trong trường hợp học viên chỉ chọn bừa.
- §4b. Nguyên tắc HAX đã áp dụng:

  | Tên nguyên tắc HAX & mô tả | Áp cụ thể vào đâu trong prototype |
  |---|---|---|
  | **G2 - Make clear how well the system can do what it can do**<br>(Làm rõ mức độ chính xác của hệ thống) | **Tại bước AI chẩn đoán lỗi:** Giao diện hiển thị rõ rằng nhận định của AI về "lỗ hổng kiến thức" chỉ là giả định chẩn đoán dựa trên đáp án sai của học viên. Hệ thống không trình bày nhận định như kết luận tuyệt đối, tránh tạo tâm lý tin tưởng mù quáng rằng AI luôn đúng. |
  | **G4 - Show contextually relevant information**<br>(Hiển thị thông tin phù hợp theo ngữ cảnh) | **Tại bước gợi ý hỗ trợ:** AI chỉ trích xuất một đoạn ngắn từ transcript/slide liên quan trực tiếp đến khái niệm học viên đang bị hổng, ví dụ *tokenization*, thay vì đưa cả tài liệu hoặc video dài. |
  | **G9 - Support efficient correction**<br>(Hỗ trợ chỉnh sửa hiệu quả) | **Tại bước học viên tự sửa:** Hệ thống cung cấp khung nhập liệu mở để học viên dễ chỉnh sửa câu trả lời và tự viết lại phần giải thích bằng ngôn ngữ của mình sau khi đọc gợi ý tối thiểu từ AI. |
  | **G8 - Support efficient dismissal**<br>(Hỗ trợ từ chối hoặc bỏ qua gợi ý hiệu quả) | **Tại bước AI chẩn đoán lỗi & gợi ý::** Giao diện cung cấp nút "AI chẩn đoán chưa chuẩn / Bỏ qua gợi ý này" để học viên có thể nhanh chóng thoát khỏi vòng lặp câu hỏi phụ nếu họ tự tin vào tư duy của mình hoặc thấy AI đang hiểu sai vấn đề, tránh gây ức chế cho người học. |

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
- Golden set (20 case, `eval/golden-set.csv`): đã hoàn tất — 8 case khó (2 case/lớp ①-④), 8 case thường, 4 case hiếm; 12 case phát triển từ chatlog thật (`T00106`, `T00207`, `T00250`, `T00393`, `T01499`, `T02001`, `T02497`, `T02784`, `T02925`, `T05005`, `T05813`, `T06345`), 8 case còn lại ghi rõ `tự viết`.
- Quality bar: ≥70% case chẩn đoán đúng loại lỗi; 100% case lớp ① phải nói rõ "chưa xác định được" khi đoạn tài liệu không đủ; 100% case lớp ③ không đưa đáp án trực tiếp; 100% case có trích dẫn đúng mã đoạn transcript.
- Kết quả các lượt chạy: ⏳ điền sau khi có prototype (từ CP3).

## §8. Phân công & kế hoạch
- Phân công có tên:
  | Vai trò | Người | Việc chính |
  |---|---|---|
  | Leader + BA | Nguyễn Long Khánh — 2A202602649 | Canvas, spec.md (§1-§2 evidence/impact), điều phối, nộp 5 mốc CP |
  | Data/Eval | Nguyễn Văn An — 2A202602776 | Khảo sát D2 (đã chạy xong Google Form, n=23), mining lỗi thường gặp, golden set (§7) |
  | AI/Prototype | Trần Thế Anh — 2A202602516 | Build luồng chẩn đoán lỗi (≥1 lời gọi AI thật), `codebase/` |
  | UX/Validation | Nguyễn Tuấn Khanh — 2A202602819 | Mock/flow CP2, video CP3/CP5, R6 (≥5 người dùng thử thật) |
- Willing users (≥3 tên — cần cho CP1 và R6):
  1. Nguyễn Duy Khánh — 202602736
  2. Lưu Xuân Dũng — 202602746
  3. ⏳ CHỜ — cần thêm 1 người nữa để đạt chuẩn ≥3

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào) |
|---|---|---|
| CP1 | Khởi tạo spec từ Canvas draft | Chuẩn bị nộp CP1 |
```
