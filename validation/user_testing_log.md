# Feedback Log — R6

> Mỗi dòng ghi rõ nguồn thu thập, vì nhóm có 2 đợt hỏi khác nhau (Khanh hỏi trực tiếp qua thao tác + leader hỏi qua trao đổi) — cả hai đều là dữ liệu thật, không gộp lại thành một để tránh trộn lẫn nguồn.

| # | Người thử | Nhiệm vụ giao | Điểm tắc nghẽn / Quan sát | Trích dẫn nguyên văn | Quyết định xử lý của nhóm | Nguồn ghi nhận |
|---|---|---|---|---|---|---|
| 1 | Nguyễn Duy Khánh — 202602736 | Trả lời 5 câu trắc nghiệm rồi làm 2 case thuộc lớp khó ①(Nguồn sự thật) và ④(Đặc thù domain) trên bản Prototype CP2 | Lo ngại nguy cơ người dùng bị mắc kẹt quá lâu ở một câu hỏi | "Nếu chẳng may người dùng mãi mắc kẹt ở 1 câu hỏi sẽ khiến họ rất ức chế." | Sản phẩm đã có sẵn nút "Đổi câu hỏi khác" cho phép thoát bất kỳ lúc nào — **không phải tính năng mới thêm để phản hồi feedback này** (đính chính: bản trước ghi nhầm là đã sửa code ở CP4, thực tế nút này có sẵn từ trước, chưa có cơ chế giới hạn "hỏi quá 1 lần" như Khánh đề xuất). Ghi nhận làm gợi ý cải tiến cho backlog. | Nguyễn Tuấn Khanh hỏi trực tiếp (thao tác trên bản Prototype CP2) |
| 2 | Lưu Xuân Dũng — 202602746 | Trả lời 5 câu trắc nghiệm rồi làm case GS01, GS07 trên bản Prototype CP2 | Không ghi nhận điểm tắc nghẽn cụ thể | "Giao diện đẹp." | *Lưu ý: đây là lời khen chung chung, chưa đạt chuẩn "quote lúc đang cố làm task" theo Mom Test — giữ lại làm tín hiệu phụ, không dùng làm bằng chứng chính cho R6.* | Nguyễn Tuấn Khanh hỏi trực tiếp (thao tác trên bản Prototype CP2) |
| 3 | Nguyễn Duy Khánh — 202602736 | Làm 5 câu trắc nghiệm + 1 case golden set (trả lời sai cố ý) trên bản mới nhất (đã có AI thật + giao diện redesign) → đọc chẩn đoán AI → tự sửa lại | Khó hiểu ở phần AI tạo đề (bài tự luận thích ứng sinh theo điểm quiz); không vướng ở thao tác bấm nút nào khác | "Khó hiểu ở phần AI tạo đề" | Đưa vào backlog: thêm 1 dòng giải thích ngắn trước khi AI sinh câu hỏi tự luận | Trưởng nhóm hỏi trực tiếp qua trao đổi |
| 4 | Lưu Xuân Dũng — 202602746 | Làm 5 câu trắc nghiệm + 1 case golden set (trả lời sai cố ý) trên bản mới nhất → đọc chẩn đoán AI → tự sửa lại | Cùng nhận xét: khó hiểu ở phần AI tạo đề; tổng thể đánh giá luồng chạy tốt, không bị kẹt | "Không có chỗ nào bấm nhầm hoặc không biết làm gì tiếp theo, về cơ bản là bài này làm khá tốt" | Xác nhận luồng thao tác ổn, không cần sửa | Trưởng nhóm hỏi trực tiếp qua trao đổi |
| 5 | | | | | | |

---

## Tổng hợp cuối (bắt buộc 4 dòng)

- **Chủ đề lặp nhiều nhất:** Khó hiểu ở bước AI sinh bài tự luận thích ứng theo điểm trắc nghiệm — được cả 2 người nhắc tới độc lập qua 2 đợt hỏi khác nhau.
- **1-2 thay đổi làm trước demo:** Thêm 1 dòng giải thích ngắn ngay trước khi AI sinh câu hỏi tự luận (VD "Dựa trên X% điểm trắc nghiệm, AI sẽ ra 1 câu tự luận độ khó phù hợp") — *(nhóm tự quyết có làm kịp không trước demo; nếu không kịp thì đưa xuống mục backlog bên dưới)*.
- **Giữ nguyên gì và vì sao:** Luồng thao tác/bấm nút chính không ai gặp vướng qua cả 2 đợt test — không cần đổi.
- **Đưa vào backlog:** Cân nhắc thêm cơ chế giới hạn số lần thử trước khi cho bỏ qua câu hỏi (ý tưởng từ Khánh) nếu còn thời gian sau demo.
