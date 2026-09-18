# Kịch bản thuyết trình CP6 — Nhóm 4Idiots (Track D2)

Tổng thời lượng: **5 phút trình bày + 5 phút Q&A**, đúng cấu trúc 6 phần bắt buộc (`02-guide.md` §5.1). Mọi số liệu trong này đều lấy thật từ `spec.md`/`eval/` — không thêm số mới, khi lên sân khấu chỉ cần đọc đúng, không cần học thuộc từng chữ.

**Phân vai (mỗi người ≥1 phần, đúng "vibe-coding rule" — ai cũng phải giải trình được phần mình nói):**
- **Khánh (Leader/BA):** Phần 1, 2, 6 (mở đầu, đóng)
- **Thế Anh (Data/Eval):** góp phần 3 (giải thích case chỗ khó)
- **An (AI/Prototype):** Phần 3 (chạy demo live), Phần 4 (kết quả đo)
- **Khanh (UX/Validation):** Phần 5

---

## Phần 1 — User & Job (45 giây) — Khánh

> "Xin chào ban giám khảo, nhóm 4Idiots, track D2 — Học tập thích ứng và tương tác.
>
> Người dùng của tụi mình là một học viên K4 đang làm bài tập ngay sau khi học một khái niệm mới trên VLearn. Vấn đề thật: khi làm sai, hệ thống hiện tại chỉ báo *'sai rồi, đáp án là...'* — không chỉ ra đúng chỗ học viên đang hiểu nhầm gì, khiến học viên phải tua lại cả bài giảng để tìm lỗi.
>
> Đây không phải giả định — tụi mình khảo sát **23 học viên**, **14 trên 23 người, tức 60,9%, xác nhận có pain này**, đạt chuẩn Đường A của khoá (≥20 người, ≥50% xác nhận). Dấu hiệu mạnh nhất: **11 trên 23 người** nói thẳng *'đáp án chỉ nói sai rồi, không giải thích chỗ hiểu nhầm'* — đúng trọng tâm bài toán tụi mình chọn."

---

## Phần 2 — Vì sao chọn tính năng này (45 giây) — Khánh

> "Tụi mình so sánh 4 hướng. **D1 — lớp học mô phỏng đa tác tử** bị loại vì rủi ro kỹ thuật cao, khó demo gọn trong thời gian ngắn. **D3 — học bằng cách dạy lại** bị loại vì khó đo được 'đã hiểu sâu hơn chưa' bằng con số khách quan. **A1 — tối ưu tutor VLearn hiện có** tuy có sẵn dữ liệu lớn nhưng không thuộc track D và không đo được 'học được' theo đúng yêu cầu riêng của track.
>
> Tụi mình chọn **D2 — Học từ lỗi trước**, vì đo trực tiếp được 'học được' bằng đúng/sai bài tập trước và sau khi sửa, và lát cắt đủ nhỏ để build nổi trong 3 buổi."

---

## Phần 3 — Giải pháp & demo live (2 phút) — Thế Anh giới thiệu case, An chạy demo

**Thế Anh (20 giây):**
> "Lát cắt của tụi mình gói trong một câu: một học viên làm bài tập về một khái niệm, trả lời sai — AI chẩn đoán đúng chỗ hiểu nhầm cụ thể, không đưa đáp án ngay mà chỉ gợi ý một bước tối thiểu kèm trích dẫn tài liệu — học viên tự sửa và giải thích lại được.
>
> Tụi mình xây bộ 20 case kiểm thử theo đúng 4 lớp chỗ khó của khoá: nguồn sự thật, mơ hồ, ngoài phạm vi, và đặc thù domain — 12 trong số đó lấy thật từ chatlog học viên khoá trước."

**An (1 phút 40 giây, demo trực tiếp trên `mock-cp2.html`):**
> "Giờ tụi mình demo trực tiếp 2 case — không dựng sẵn.
>
> **Case một, case chuẩn:** [chọn GS07 trong Kho Golden Set] Học viên trả lời sai rằng token với vector là một. [bấm Nộp] AI đang gọi Gemini thật... [đọc kết quả] — thấy không, AI chỉ ra đúng: học viên nhầm token là văn bản với vector là biểu diễn số, gợi ý đọc lại trình tự xử lý chứ không đưa thẳng đáp án, và trích dẫn nguyên văn tài liệu bài giảng.
>
> **Case hai, case chỗ khó** — đây là phần tụi mình muốn khoe nhất, vì AI xử lý đúng case khó mới là cái khó thật: [chọn GS01] học viên hỏi giá gọi API GPT-4, nhưng tài liệu bài giảng không hề nêu mức giá cụ thể. [bấm Nộp, đọc kết quả] — AI không bịa ra một con số nào cả, nó nói rõ *'chưa xác định được'* vì tài liệu không đủ căn cứ. Đây chính là cơ chế chống hallucination tụi mình thiết kế trong system prompt, không phải AI né tránh ngẫu nhiên."

---

## Phần 4 — Kết quả đo (45 giây) — An

> "Tụi mình chạy hết 20 case trong golden set, chấm tay đối chiếu với đáp án kỳ vọng — **14 trên 20 case, tức 70%, chẩn đoán đúng loại lỗi**, đúng chuẩn tụi mình đã cam kết từ trước khi đo.
>
> Case thất bại đáng kể nhất: một số case ngoài lớp bắt buộc AI vẫn quá thận trọng, trả lời 'chưa xác định được' dù tài liệu đủ căn cứ để chẩn đoán — tụi mình phân tích đây là đánh đổi giữa việc chống bịa đặt và khả năng phát hiện lỗi, và hướng cải thiện tiếp theo là mở rộng ngữ cảnh trích xuất tài liệu."

---

## Phần 5 — User thật nói gì (45 giây) — Khanh

> "Tụi mình cho 2 người ngoài nhóm dùng thử trực tiếp — cả hai đều là willing user đã đăng ký từ vòng đầu. Cả hai đều nói **luồng thao tác chạy tốt, không bấm nhầm hay bị kẹt ở đâu** — nhưng cùng phản hồi một điểm: **khó hiểu ở bước AI tự sinh câu hỏi tự luận theo điểm trắc nghiệm** — chưa rõ vì sao câu hỏi lại ra như vậy.
>
> Tụi mình ghi nhận đây là phần cần làm rõ thêm UI, đã đưa vào backlog. Thời gian ngắn nên chưa đủ 5 người theo chuẩn khoá, tụi mình xin khai thiếu phần này thay vì giấu."

---

## Phần 6 — Nếu có thêm 1 tuần (30 giây) — Khánh

> "Hai việc ưu tiên: một, hoàn thiện phần validate với đủ 5 người dùng thử thay vì 2. Hai, cải thiện cơ chế trích xuất tài liệu để AI tự tin chẩn đoán hơn ở các case ngoài 4 lớp bắt buộc, mà vẫn giữ nguyên tắc không bịa đặt.
>
> Bài học lớn nhất của nhóm: xây một AI Agent an toàn tuyệt đối, không bịa, thì dễ — nhưng làm nó vừa an toàn vừa hữu ích là một sự đánh đổi thật, cần đo bằng số chứ không chỉ cảm tính. Cảm ơn ban giám khảo."

---

## Chuẩn bị Q&A (5 phút)

Giám khảo có **thẻ chạy 1 case lạ tại chỗ** — cả nhóm cần sẵn sàng, không chỉ người demo. Ôn nhanh các câu có thể bị hỏi:

| Câu hỏi khả năng cao | Ai trả lời | Ý chính |
|---|---|---|
| "Augment hay automate — vì sao?" | Khánh | Conditional automation — AI chỉ dừng ở chẩn đoán + gợi ý, không đưa đáp án, vì đưa đáp án ngay sẽ mất tác dụng productive failure |
| "Failure nguy hiểm nhất của sản phẩm?" | An | 6/20 case AI quá thận trọng, không dám chẩn đoán khi lẽ ra đủ căn cứ — đánh đổi precision/recall |
| "Phần bạn làm là gì?" | *(từng người tự trả lời phần mình)* | — |
| "Sao chỉ có 2 người validate?" | Khanh | Thời gian ngắn, đã khai thiếu rõ ràng trong `validation/README.md`, không giấu |
| "Golden set 20 case lấy từ đâu?" | Thế Anh | 12/20 case từ chatlog thật, đã verify turn_id; 8 case tự viết bám taxonomy 4 lớp |
| "Case lạ giám khảo đưa, AI xử lý thế nào?" | An (demo trực tiếp) | Chạy y hệt luồng đã demo — nộp câu trả lời, đọc kết quả AI trả về thật |
