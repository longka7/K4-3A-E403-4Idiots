# CP4 — chốt spec.md, hạn 21:00 hôm nay (17/9)

Sau 21:00 không sửa quality bar được nữa, nên phần nào xong thì chốt luôn, đừng để tới sát giờ mới viết.

CP4 chỉ có một việc: hoàn thiện `spec.md`. TA sẽ kiểm 5 ô này tại CP4:
- Evidence chuẩn A/B có log — đã xong (survey n=23)
- Bảng impact + ứng viên đã loại — đã xong
- 4 lớp chỗ khó cụ thể — **chưa làm**
- ≥4 nguyên tắc HAX/PAIR có chỗ áp dụng cụ thể — **chưa làm**
- Quality bar bằng số — đã có định nghĩa, còn thiếu bảng kết quả thật

Còn 3 phần trống cần làm trong tối nay: §4b, §5, §6, §7 (phần bảng kết quả). Chia như sau, mỗi người viết thẳng vào `spec.md`, xong thì báo trong nhóm để leader gộp lại.

---

## Thế Anh — viết §5 (4 lớp chỗ khó + kịch bản)

Anh đã làm golden set rồi nên phần này làm nhanh, gần như tận dụng lại.

Việc cần làm:
1. Viết lại 4 lớp chỗ khó cho cụ thể (không nói chung chung), đối chiếu với 4 nguồn lỗi trong PAIR chương 6: lỗi dữ liệu/dự đoán, lỗi input & kỳ vọng, lỗi chất lượng output, lỗi hệ thống nhiều tầng.
2. Viết ≥8 kịch bản, mỗi kịch bản một dòng theo format: `tình huống cụ thể | lớp | hành vi mong muốn (nói gì, hiện gì) | nguyên tắc áp dụng`.

Cách làm nhanh nhất: lấy đúng 8 case "khó" trong `eval/golden-set.csv` (GS01-GS08, đã đúng 2 case/lớp rồi), mỗi case viết lại thành 1 dòng kịch bản theo format trên. Không cần nghĩ case mới.

## An — chạy lại số liệu thật cho §7 + viết §6

Việc quan trọng nhất: sửa cách chấm điểm trong `eval/run_full_evaluation.py`. Chỗ đang sai là dòng `else: c_diag_ok = len(diag.strip()) > 10` — chỗ này chỉ đếm độ dài câu trả lời chứ không so với đáp án đúng (`chan_doan_can_dat`), nên báo cáo ra 100% dù thực tế có case AI trả lời sai. Cách sửa nhanh nhất trong tối nay: bỏ phần tự động chấm ở đoạn này, in cả AI trả lời lẫn đáp án đúng ra cạnh nhau, rồi hai người (An + một bạn khác) tự chấm tay từng case — đúng cách guide khuyên (`02-guide.md` mục 4).

Sau khi có số thật, gửi cho leader để điền vào §7. Nhớ giữ cả case fail, không được giấu — số xấu vẫn tính điểm miễn là thật, sửa/giấu số mới bị trừ.

Xong phần trên thì viết tiếp §6 (4 đường đi trải nghiệm: đi đúng / mơ hồ hỏi lại / không đủ căn cứ / học viên tự sửa) — dùng luôn ví dụ thật từ log vừa chạy, không cần bịa thêm.

## Khanh — viết §4b (nguyên tắc HAX/PAIR)

Chọn ≥4 nguyên tắc, mỗi cái phải chỉ ra được nó nằm ở đâu trong `mock-cp2.html` thật, không chỉ nói lý thuyết. Vài cái mình thấy đã có sẵn trong sản phẩm, anh viết lại cho rõ thôi:

- Khi tài liệu không đủ, AI nói "chưa xác định được" thay vì đoán bừa — đây là nguyên tắc G10 (thu hẹp phạm vi khi nghi ngờ).
- AI luôn kèm trích dẫn đoạn tài liệu — G2 (user biết khi nào nên tin).
- Khi gọi API lỗi, có màn hình báo lỗi riêng chứ không đứng im — PAIR "Errors & Graceful Failure".
- Gợi ý không đưa đáp án thẳng, học viên vẫn tự bấm nút thử lại được — G8 (gạt bỏ/thử lại dễ dàng).

Đọc thêm ở `further-reading/hax-guidelines.md` và `further-reading/pair-guidebook-digest.md` nếu cần câu chữ chuẩn hơn.

Nếu còn thời gian sau phần này, làm thêm §3 (dùng thử 1 sản phẩm tương tự — ChatGPT study mode, Khanmigo, Duolingo, Quizlet AI — trả lời 4 câu theo `02-guide.md` §2.2, 15 phút thôi, không bắt buộc điểm nhưng có trong template). Video CP3 nếu chưa gửi thì gửi luôn.


