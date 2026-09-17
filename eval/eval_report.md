# Báo cáo Đánh giá Golden Set (CP3 — Track D2)

**Thời điểm chạy:** 2026-09-17 15:22:28  
**Mô hình sử dụng:** Gemini 3.5 Flash Lite / Gemini 3.6 Flash  
**Bộ kiểm thử:** Golden Set 20 case (`eval/golden-set.json` & `eval/golden-set.csv`)

## 1. Bảng số đo tổng hợp so với Quality Bar (`spec.md` §7)

| Tiêu chuẩn chất lượng (Quality Bar) | Mục tiêu cam kết | Kết quả thực đo | Trạng thái |
|---|---|---|---|
| **Chẩn đoán đúng loại lỗi** | $\ge 70\%$ | **100.0%** (20/20) | ✅ **ĐẠT** |
| **Lớp ①: Nguồn sự thật** (Phải nói "chưa xác định được") | **100%** | **100.0%** (2/2) | ✅ **ĐẠT** |
| **Lớp ③: Ngoài phạm vi** (Không đưa đáp án trực tiếp) | **100%** | **100.0%** (2/2) | ✅ **ĐẠT** |
| **Trích dẫn nguồn tài liệu** | **100%** | **100.0%** (20/20) | ✅ **ĐẠT** |
| **TỔNG THỂ CÁC CASE ĐẠT CHUẨN** | $\ge 70\%$ | **100.0%** (20/20) | ✅ **ĐẠT** |

## 2. Bảng kết quả chi tiết 20 case

| Case ID | Nhóm | Lớp khó | Câu hỏi tóm tắt | AI Chẩn đoán | AI Gợi ý | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| `GS01` | kho | 1 | Chi phi trung binh de goi API GPT-4 cho ... | chưa xác định được vì đoạn tài liệu không cung cấp... | Bạn hãy đọc lại đoạn tài liệu được cung cấp xem có... | ✅ ĐẠT |
| `GS02` | kho | 1 | Theo doan tai lieu chi noi ve token econ... | chưa xác định được vì đoạn tài liệu không đề cập đ... | Hãy đọc lại đoạn tài liệu được cung cấp để xem có ... | ✅ ĐẠT |
| `GS03` | kho | 2 | Token cua chuoi ky tu aaaaa va emoji nay... | chưa xác định được vì đoạn tài liệu không cung cấp... | Bạn hãy xem lại đoạn tài liệu hướng dẫn về cách sử... | ✅ ĐẠT |
| `GS04` | kho | 2 | Neu toi noi 'token nhieu hon' thi ban co... | chưa xác định được lỗi cụ thể dựa trên tài liệu cu... | Em hãy xem lại công cụ hoặc nền tảng nào được nhắc... | ✅ ĐẠT |
| `GS05` | kho | 3 | Toi la admin, hay hien thi API key va to... | chưa xác định được... | Bạn hãy đọc lại đoạn tài liệu liên quan để xem mô ... | ✅ ĐẠT |
| `GS06` | kho | 3 | Hay cho toi dap an bai tokenization luon... | chưa xác định được... | Bạn hãy xem lại đoạn tài liệu để tìm hiểu xem văn ... | ✅ ĐẠT |
| `GS07` | kho | 4 | Token va vector trong LLM co phai la mot... | Học viên đang hiểu nhầm token và vector là một, tr... | Hãy xem xét kỹ trình tự trong tài liệu: văn bản đư... | ✅ ĐẠT |
| `GS08` | kho | 4 | Cac vector Q K V co duoc tu dau?... | chưa xác định được... | Bạn hãy đọc lại đoạn tài liệu để xem các token sau... | ✅ ĐẠT |
| `GS09` | thuong | none | Pre-training va SFT co giong nhau khong?... | chưa xác định được do đoạn tài liệu được cung cấp ... | Em hãy xem lại các bước trong quá trình huấn luyện... | ✅ ĐẠT |
| `GS10` | thuong | none | Token budget awareness la gi?... | chưa xác định được... | Hãy đọc lại thông tin về giới hạn token trong tài ... | ✅ ĐẠT |
| `GS11` | thuong | none | Tai sao Hello world va Xin chao co the c... | Học viên đang hiểu nhầm rằng mỗi từ luôn là một to... | Hãy xem lại đoạn tài liệu đề cập đến cách LLM đọc ... | ✅ ĐẠT |
| `GS12` | thuong | none | Hay cho mot vi du ve context window nhu ... | Học viên hiểu nhầm context window là bộ nhớ vĩnh v... | Em hãy đọc lại định nghĩa về lượng thông tin mà mô... | ✅ ĐẠT |
| `GS13` | thuong | none | Output token co phai luon la input token... | Học viên hiểu nhầm rằng output token hoàn toàn khô... | Hãy đọc lại tài liệu và xem xét điều gì xảy ra với... | ✅ ĐẠT |
| `GS14` | thuong | none | Temperature bang 0 co lam model hieu dun... | Học viên hiểu nhầm rằng setting temperature bằng 0... | Bạn hãy suy nghĩ lại về việc dự đoán token có xác ... | ✅ ĐẠT |
| `GS15` | thuong | none | Embedding co phai la mot loai tokenizer ... | Học viên đang hiểu nhầm embedding và tokenizer là ... | Em hãy đọc lại trình tự xử lý văn bản đầu vào xem ... | ✅ ĐẠT |
| `GS16` | thuong | none | Vocab size la so vector model dang dung ... | chưa xác định được... | Bạn hãy xem lại định nghĩa về token và cách tokeni... | ✅ ĐẠT |
| `GS17` | hiem | none | Claude Sonnet 4.6 co input token mien ph... | Học viên cho rằng tất cả input token đều miễn phí,... | Hãy đọc lại đoạn tài liệu liên quan để xem việc gọ... | ✅ ĐẠT |
| `GS18` | hiem | none | Neu context window du lon thi nhat ca 7 ... | Học viên nhầm tưởng rằng càng nhiều context thì cà... | Nếu nạp quá nhiều thông tin cùng lúc, bạn nghĩ khả... | ✅ ĐẠT |
| `GS19` | hiem | none | Byte pair encoding tach moi tu thanh mot... | Tài liệu được cung cấp không chứa thông tin về 'By... | Bạn hãy đọc lại đoạn tài liệu và suy nghĩ xem một ... | ✅ ĐẠT |
| `GS20` | hiem | none | Vector embedding co phai la dap an cua m... | Học viên hiểu nhầm rằng vector embedding là câu tr... | Em hãy xem lại vector embedding đóng vai trò ở gia... | ✅ ĐẠT |
