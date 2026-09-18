# Kịch bản quay Video Demo dự phòng — CP5

Khác với video CP3 (chỉ cần chứng minh chạy được, quay thô): video này là **bản thay thế khi live hỏng trên sân khấu**, nên phải quay đúng y hệt phần sẽ trình bày — khớp với Slide 3 "Giải pháp & demo live" (2 phút) trong `02-guide.md` §5.1.

**Bắt buộc 2 case:** 1 case chuẩn (AI chẩn đoán đúng, mượt) + 1 case chỗ khó (AI phải biết nói "chưa xác định được" thay vì bịa). Đã kiểm chứng cả 2 case chạy thật đúng như kỳ vọng trước khi viết kịch bản này.

---

## Chuẩn bị trước khi quay

- [ ] API key đã cấu hình trong `codebase/config.js` (đã có sẵn)
- [ ] Chạy `python3 -m http.server 8791` rồi mở `http://localhost:8791/codebase/mock-cp2.html`
- [ ] Cửa sổ trình duyệt rộng ~1000-1100px để chữ rõ, không cần full màn hình
- [ ] Dry run thử 1 lượt trước khi quay thật (đúng yêu cầu checklist CP5)
- [ ] Tắt hết tab/thông báo khác, tránh popup hệ thống che màn hình lúc quay

---

## Phần 1 — Case chuẩn (GS07 — lớp ④, ~50 giây)

| Thời gian | Thao tác | Lời dẫn gợi ý |
|---|---|---|
| 0:00–0:05 | Vào Bước 1, mở tab "Kho 20 case Golden Set", chọn case **GS07** trong dropdown | "Đây là bài tập về khái niệm token và vector trong LLM." |
| 0:05–0:10 | Chỉ vào câu hỏi + đoạn tài liệu grounding hiện sẵn | "Học viên đã trả lời sai — cho rằng token chính là vector." |
| 0:10–0:15 | Bấm "Nộp câu trả lời cho AI chấm" | "Bấm nộp, AI Gemini sẽ đọc và chẩn đoán thật, không có kịch bản dựng sẵn." |
| 0:15–0:25 | Chờ loading (~3-5s), AI trả kết quả | Để nguyên, không cắt — cho thấy đây là lời gọi AI thật |
| 0:25–0:45 | Đọc to 3 khối kết quả: chẩn đoán, gợi ý, trích dẫn | *"AI chỉ ra đúng: học viên nhầm token với vector, bỏ qua bước embedding — gợi ý dẫn dắt tư duy chứ không đưa thẳng đáp án, và có trích dẫn nguyên văn tài liệu bài giảng để đối chiếu."* |
| 0:45–0:50 | Bấm "Đổi câu hỏi khác" để chuyển sang case tiếp theo | "Giờ thử với một case khó hơn." |

## Phần 2 — Case chỗ khó (GS01 — lớp ①, ~50 giây)

| Thời gian | Thao tác | Lời dẫn gợi ý |
|---|---|---|
| 0:50–0:55 | Chọn case **GS01** trong dropdown | "Câu hỏi về chi phí gọi API GPT-4 — nhưng tài liệu bài giảng không hề nêu mức giá cụ thể." |
| 0:55–1:00 | Bấm "Nộp câu trả lời cho AI chấm" | "Đây là phép thử quan trọng: AI có bịa số liệu không có thật hay không." |
| 1:00–1:10 | Chờ loading, AI trả kết quả | |
| 1:10–1:35 | Đọc to kết quả, nhấn mạnh cụm "chưa xác định được" | *"AI không bịa ra một con số nào — nó nói rõ tài liệu không đủ căn cứ, và gợi ý học viên tự đọc lại đoạn liên quan thay vì đoán bừa. Đây chính là nguyên tắc chống hallucination mà nhóm đã thiết kế trong system prompt."* |
| 1:35–1:45 | Bấm nút "AI chẩn đoán chưa chuẩn — Bỏ qua gợi ý" (nếu muốn minh hoạ thêm quyền kiểm soát của học viên) | "Học viên luôn có thể bỏ qua gợi ý và tự làm theo cách của mình." |

## Phần 3 — Chốt (~10-15 giây, tuỳ chọn)

Nếu muốn khép lại gọn: quay lại màn tổng kết hoặc nói 1 câu chốt: *"Đây là 2 trong 20 case golden set nhóm đã xây, đo được thật 70% chẩn đoán đúng loại lỗi trên toàn bộ."*

---

## Lưu ý khi quay

- Nói tự nhiên theo ý, không cần học thuộc lòng lời dẫn — cột "Lời dẫn gợi ý" chỉ để tham khảo ý chính.
- Nếu AI trả lời hơi khác so với lần test (do không tất định), **cứ đọc đúng những gì AI thực sự trả ra** — không đọc theo kịch bản cũ, tránh nói sai với màn hình đang chiếu.
- Quay xong nhớ export/save video, đặt tên rõ ràng (VD `demo-video-cp5-4idiots.mp4`), chuẩn bị nộp cùng `demo-slides.pdf`.
