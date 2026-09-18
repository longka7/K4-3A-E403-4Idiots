# Validation — R6 (bonus +8 điểm)

> **Chưa có dữ liệu thật.** Đây chỉ là khung mẫu để điền — không được điền quote/quan sát giả. Số liệu bị chỉnh sửa hoặc bịa sẽ không được tính (theo đúng nguyên tắc minh bạch của khoá).

## Cách làm (theo `02-guide.md` §3.4 + README "R6 · Cho người ngoài dùng thử")

1. Tìm **5 người ngoài nhóm** (trong đó ≥2 người đã khai từ CP1: Nguyễn Duy Khánh, Lưu Xuân Dũng).
2. **Giao 1 task cụ thể** cho họ làm trên `codebase/mock-cp2.html` (VD: "làm sai bài tập token vs vector, xem AI chẩn đoán gì rồi thử sửa lại").
3. **Ngồi im quan sát** — đừng hỏi "sản phẩm này hay không?". Ghi lại đúng những gì họ làm, họ vướng ở đâu, và **chép nguyên văn** lời họ nói (kể cả viết/nói sai chính tả).
4. Điền vào bảng bên dưới — mỗi người 1 dòng.
5. Sau khi có đủ log, chọn **≥1 thay đổi** đã làm dựa trên feedback, ghi vào `spec.md` §9 Changelog (giữ nguyên thiết kế thì cũng phải ghi rõ lý do tại sao).

**Quote đạt chuẩn** là lời nói lúc đang cố làm task (VD: "mình không hiểu AI đang gợi ý cái gì"), **không phải** lời khen xã giao (VD: "demo ok đấy").

---

## Bảng nhật ký

| # | Người thử (tên/vai) | Willing user từ CP1? | Task giao | Quan sát (họ làm gì, vướng ở đâu) | Quote nguyên văn | Mức nghiêm trọng |
|---|---|---|---|---|---|---|
| 1 | Nguyễn Duy Khánh — 202602736 | Có | Làm 5 câu trắc nghiệm + 1 case golden set (trả lời sai cố ý) → đọc chẩn đoán AI → tự sửa lại | Khó hiểu ở phần AI tạo đề (bài tự luận thích ứng sinh theo điểm quiz); không vướng ở thao tác bấm nút nào khác | "Khó hiểu ở phần AI tạo đề" | Nhẹ |
| 2 | Lưu Xuân Dũng — 202602746 | Có | Làm 5 câu trắc nghiệm + 1 case golden set (trả lời sai cố ý) → đọc chẩn đoán AI → tự sửa lại | Cùng nhận xét: khó hiểu ở phần AI tạo đề; tổng thể đánh giá luồng chạy tốt, không bị kẹt | "Không có chỗ nào bấm nhầm hoặc không biết làm gì tiếp theo, về cơ bản là bài này làm khá tốt" | Nhẹ |
| 3 | | Không | | | | |
| 4 | | Không | | | | |
| 5 | | Không | | | | |

> *Ghi chú nguồn: 2 dòng trên do trưởng nhóm trực tiếp hỏi và ghi lại ý chính từ Khánh/Dũng (không phải chụp màn hình tin nhắn gốc) — nếu giám khảo hỏi, nhóm nói rõ đây là ghi nhận trực tiếp qua trao đổi, không phải log chat.*

---

## Tổng hợp cuối (bắt buộc 4 dòng)

- **Chủ đề lặp nhiều nhất:** *(dựa trên 2/2 log hiện có, cần thêm ≥3 người nữa để chắc chắn đây là pattern thật chứ không phải trùng hợp)* Cả 2 người thử đều thấy khó hiểu ở bước AI sinh bài tự luận thích ứng — chưa rõ vì sao câu tự luận lại được tạo ra dựa trên điểm trắc nghiệm.
- **1-2 thay đổi làm trước demo:** *(nhóm tự quyết — gợi ý: thêm 1 dòng giải thích ngắn ngay trước khi AI sinh câu hỏi, VD "Dựa trên X% điểm trắc nghiệm, AI sẽ ra 1 câu tự luận độ khó phù hợp", ghi vào `spec.md` §9 nếu áp dụng)*
- **Giữ nguyên gì và vì sao:** *(điền sau khi đủ log — phần luồng thao tác/bấm nút không ai gặp vướng nên không cần đổi)*
- **Đưa vào backlog (nói ở slide 6 "nếu có thêm 1 tuần"):** *(điền sau)*
