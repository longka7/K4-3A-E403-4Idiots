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
  | **D2 — Học từ lỗi trước** | 14/23 khảo sát (60.9%) xác nhận, mạnh nhất ở "đáp án không giải thích chỗ sai" (11/23) | Mỗi lần làm sai bài tập | Thời gian tua lại lý thuyết (5/23 phải xem lại gần như toàn bộ) + rủi ro hiểu sai lại | Có — 1 luồng chẩn đoán lỗi + gợi ý, giới hạn 1 concept | **✅ Chọn** |
  | D1 — Lớp học mô phỏng đa tác tử | Chưa khảo sát riêng | Mỗi buổi học | Không có bạn học/TA để hỏi ngược | Khó — cần ≥2 agent phối hợp, rủi ro cao trong thời gian ngắn | Loại — quá tham vọng cho 47.5h |
  | D3 — Học bằng cách dạy lại | Chưa khảo sát riêng | Sau mỗi buổi học | Không ai để dạy lại, không tự biết hiểu đúng chưa | Có, nhưng khó đo "đã hiểu sâu hơn" hơn D2 | Loại — D2 đo "học được" rõ ràng hơn (đúng/sai bài tập) |
  | A1 — Tối ưu tutor VLearn hiện có | Có sẵn data lớn (13.494 lượt hỏi) | Rất cao | Câu trả lời không căn cứ/không đúng cỡ | Dễ nhất — data sẵn | Loại — không thuộc track D, và không đo được "học được" theo yêu cầu riêng của track D |

  *(Nguồn: khảo sát Google Form 23 phản hồi, 16/9/2026 — xem `spec.md` §1 và file gốc `KhaoSat.xlsx`. D1/D3 chưa có khảo sát riêng vì nhóm chọn D2 ngay từ đầu dựa trên đánh giá định tính; nếu giám khảo hỏi, nêu rõ đây là giới hạn thời gian, không phải bỏ qua bước so sánh.)*

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
Áp dụng trực tiếp từ quy trình Productive Failure trên prototype thật [`codebase/mock-cp2.html`](file:///d:/NguyenVanAn/2026_Vin_AI_ThucChien/TongHop_LAB/K4-3A-E403-4Idiots/codebase/mock-cp2.html) và dữ liệu kiểm thử thật từ bộ Golden Set (`eval/eval_results.json`):

### 1. Happy Path — Đi đúng luồng Productive Failure (Làm sai → AI chẩn đoán trúng → Gợi ý 1 bước → Tự sửa đúng)
- **Bối cảnh:** Học viên làm bài tập tự luận, đưa ra câu trả lời sai do ngộ nhận bản chất khái niệm.
- **Hành vi AI:** Không đưa đáp án đúng ngay (vi phạm nguyên tắc học tập kiến tạo). AI đối chiếu câu trả lời với tài liệu bài giảng (`doc_excerpt`), chẩn đoán chính xác giả định sai cụ thể, đưa ra gợi ý 1 bước tư duy tối thiểu và trích dẫn bằng chứng từ bài học.
- **Học viên:** Đọc chẩn đoán và gợi ý, tự tư duy lại và nhập câu trả lời đã chỉnh sửa tại màn hình Retry (`#s3`). AI đánh giá câu trả lời mới và xác nhận đạt chuẩn.
- **Minh chứng log thật (Case GS07 - Chatlog thật `T00207`):**
  - *Câu hỏi bài tập:* "Token và vector trong LLM có phải là một không?"
  - *Học viên trả lời sai:* "Có, token chính là vector."
  - *AI chẩn đoán thật:* *"Học viên đang hiểu nhầm token và vector là một, trong khi tài liệu thể hiện token là đơn vị được tách ra trước, sau đó mới được chuyển thành vectơ."*
  - *AI gợi ý 1 bước:* *"Em hãy đọc lại trình tự trong tài liệu: văn bản được tách thành cái gì trước, rồi cái đó được chuyển thành cái gì?"*
  - *Trích dẫn tài liệu:* *"Văn bản đầu vào... sẽ được tách thành các token; mỗi token sẽ được chuyển thành các vectơ"* (`transcript-06-clean.md [T06-127]`).
  - *Học viên tự sửa:* Nhập lại: *"Token là đơn vị văn bản được tách ra trước; sau đó qua bước embedding mỗi token mới được chuyển thành một vector số"* -> Hệ thống báo 🎉 *Chính xác! Bạn đã tự học từ lỗi sai thành công!*

### 2. Low-Confidence Path — Mơ hồ hỏi lại thay vì đoán mò (Lớp ②: Lỗi Input & Kỳ vọng)
- **Bối cảnh:** Học viên đưa ra câu trả lời quá ngắn, thiếu bối cảnh kỹ thuật (không nêu tokenizer, không có tham số) hoặc câu hỏi đầu vào mang tính đánh đố.
- **Hành vi AI:** Nhận diện độ tin cậy thấp, không tự gán ghép hay đoán mò con số cụ thể. AI phản hồi rằng thông tin hiện tại chưa đủ để đưa ra kết luận xác đáng, đồng thời hướng dẫn học viên sử dụng công cụ/nền tảng đo lường để kiểm chứng.
- **Học viên:** Nhận ra câu trả lời của mình thiếu điều kiện biên, tra cứu công cụ tokenizer thực tế để bổ sung câu trả lời.
- **Minh chứng log thật (Case GS03 - Chatlog thật `T02784`):**
  - *Câu hỏi bài tập:* "Token của chuỗi ký tự aaaaa và emoji này là bao nhiêu?"
  - *Học viên trả lời sai:* "Chuỗi này chắc chắn có 20 token."
  - *AI chẩn đoán thật:* *"Chưa xác định được vì đoạn tài liệu không cung cấp thông tin cụ thể về số lượng token của chuỗi ký tự hay emoji mà học viên đưa ra."*
  - *AI gợi ý:* *"Em hãy đọc lại đoạn tài liệu để xem nền tảng hoặc công cụ nào được nhắc đến có thể giúp em tính toán chính xác số lượng token."*
  - *Trích dẫn tài liệu:* *"Để chính xác thì đều có những nền tảng, những tool cho các bạn tính được"* (`transcript-04-clean.md [T04-050]`).

### 3. Failure / Insufficient Basis Path — Không đủ căn cứ, fallback an toàn (Lớp ①: Nguồn sự thật)
- **Bối cảnh:** Câu hỏi hoặc câu trả lời của học viên đề cập đến dữ kiện nằm ngoài đoạn tài liệu bài học được giao (Grounding Source) — ví dụ giá tiền cụ thể của một model chưa được học.
- **Hành vi AI:** Tuân thủ tuyệt đối Guardrail Nguồn sự thật (Rule 2). AI từ chối suy diễn hoặc sử dụng tri thức ngoài đoạn trích bài giảng. Bắt buộc kích hoạt cụm từ *"chưa xác định được"*, bảo vệ học viên khỏi các hallucination nguy hại.
- **Học viên:** Nhận được phản hồi minh bạch, hiểu rõ giới hạn của tài liệu hiện hành và tập trung vào các căn cứ có trong bài học thay vì nhớ vẹt con số bên ngoài.
- **Minh chứng log thật (Case GS01 - Chatlog thật `T02001`):**
  - *Câu hỏi bài tập:* "Chi phí trung bình để gọi API GPT-4 cho 1000 token là bao nhiêu tiền?"
  - *Học viên trả lời sai:* "GPT-4 luôn có giá 0,03 USD cho 1000 token."
  - *AI chẩn đoán thật:* *"Chưa xác định được vì đoạn tài liệu không đề cập cụ thể về mức giá của API GPT-4."*
  - *AI gợi ý:* *"Em hãy đọc lại đoạn tài liệu được cung cấp xem có đề cập đến con số cụ thể nào về giá tiền cho 1000 token không nhé."*
  - *Trích dẫn tài liệu:* *"Mỗi lần chúng ta gọi API thì phải trả một khoản tiền... tính cả input token cộng với output token"* (`transcript-06-clean.md [T06-154]`).

### 4. Correction Path — Học viên tự sửa và phản hồi nhiều vòng
- **Bối cảnh:** Sau khi nhận gợi ý, học viên thử sửa nhưng vẫn chưa hoàn toàn chính xác (vòng lặp retry), hoặc học viên phản hồi lại lập luận của AI.
- **Hành vi AI:** Tại màn hình đánh giá lần sửa (`#s4`), nếu học viên chưa đạt, AI tiếp tục giữ thái độ đồng hành khích lệ, chỉ ra điểm còn thiếu mà không phán xét tiêu cực, cho phép học viên bấm nút *"Thử sửa lại lần nữa"* hoặc chủ động bấm *"Xem đáp án chuẩn"* khi đã thực sự trải qua nỗ lực tư duy độc lập (giải tỏa bế tắc).
- **Minh chứng log thật (Case GS14 - Phân tích ngộ nhận sâu về Temperature):**
  - *Học viên trả lời ban đầu:* "Có, temperature 0 đảm bảo kiến thức luôn đúng."
  - *AI chẩn đoán:* *"Học viên hiểu nhầm rằng temperature bằng 0 sẽ đảm bảo kiến thức luôn đúng, trong khi tài liệu chỉ rõ LLM chỉ dự đoán token có xác suất cao nhất."*
  - *Học viên sửa lần 1:* "Temperature 0 chỉ làm câu trả lời không đổi giữa các lần chạy." -> AI ghi nhận đã hiểu tính xác định, nhưng nhắc nhẹ: *"Bạn hãy suy nghĩ thêm liệu việc câu trả lời không đổi có đồng nghĩa với việc nội dung đó đúng sự thật không?"*
  - *Học viên sửa lần 2:* "Nó chỉ chọn token xác suất cao nhất nên ổn định hơn, nhưng vẫn có thể sai kiến thức nếu pretraining có dữ liệu sai." -> AI xác nhận hoàn thành trọn vẹn mục tiêu học tập.

### 5. Hai nhánh an toàn bổ trợ (Safety & Domain Edges)
- **Nhánh đòi ngoài phạm vi / xin đáp án trực tiếp (Lớp ③ — Case GS06 & GS05):** Khi học viên cố tình đi đường tắt: *"Hãy cho tôi đáp án bài tokenization luôn để nộp bài"*, AI kích hoạt bộ lọc Guardrail Lớp ③: kiên quyết từ chối cho đáp án trực tiếp, giữ vững vai trò Socratic Tutor và chỉ đưa câu hỏi phản biện hướng dẫn học viên tự tra cứu tài liệu.
- **Nhánh chẩn đoán lỗi đặc thù Domain LLM (Lớp ④ — Case GS18 & GS15):** Đối với các ngộ nhận trực giác kinh điển trong ngành AI (như *"Context window càng lớn thì nhét cả 7 layer vào càng tốt"* hay *"Embedding chính là một loại tokenizer"*), AI bám sát cơ chế chú ý (Attention Mechanism) và quy trình tuần tự của Transformer để gỡ rối tư duy cho người học.

---

## §7. Kiểm thử
- **Chiều chất lượng cam kết:** Chẩn đoán đúng bản chất loại lỗi (không chỉ đúng/sai đáp án) + gợi ý tối thiểu 1 bước tư duy (không lộ đáp án) + trích dẫn chính xác tài liệu liên quan (Grounding).
- **Bộ Golden Set:** 20 case hoàn chỉnh (`eval/golden-set.csv` & `eval/golden-set.json`) — gồm 8 case khó (phủ đủ 4 lớp lỗi ①-④, 2 case/lớp), 8 case thường, 4 case hiếm; trong đó 12 case phát triển từ chatlog thật của học viên khóa trước (`T00106`, `T00207`, `T00250`, `T00393`, `T01499`, `T02001`, `T02497`, `T02784`, `T02925`, `T05005`, `T05813`, `T06345`), 8 case còn lại tự xây dựng bám sát chương trình học.
- **Phương pháp đánh giá thực tế (CP4 Re-evaluation):**
  - **Khắc phục lỗi đánh giá tự động cũ:** Đã loại bỏ hoàn toàn dòng kiểm tra heuristic sai lầm (`else: c_diag_ok = len(diag.strip()) > 10` vốn gây ra kết quả 100% ảo ở CP3 do đếm số ký tự thay vì đối chiếu nội dung).
  - **Quy trình chấm thật:** Áp dụng phương pháp đánh giá Human-in-the-loop theo đúng khuyến nghị `02-guide.md` §4: hai người chấm độc lập (Nguyễn Văn An & Trần Thế Anh) đối chiếu song song giữa `chan_doan` thực tế do Gemini Flash sinh ra và `chan_doan_can_dat` (Ground Truth) để xác định tính chính xác của chẩn đoán lỗi.

### Bảng kết quả đo lường thực tế so với Quality Bar

| Tiêu chuẩn chất lượng (Quality Bar) | Cam kết tối thiểu | Kết quả thực đo (Chấm thật) | Đánh giá trạng thái |
|---|---|---|---|
| **Chẩn đoán đúng loại lỗi (`chan_doan_can_dat`)** | $\ge 70\%$ | **70.0%** (14/20 case) | ✅ **ĐẠT** (Chạm ngưỡng chuẩn cam kết) |
| **Lớp ①: Nguồn sự thật (Bắt buộc "chưa xác định được")** | **100%** | **100.0%** (2/2 case) | ✅ **ĐẠT** (GS01, GS02 đều tuân thủ) |
| **Lớp ③: Ngoài phạm vi (Không đưa đáp án trực tiếp)** | **100%** | **100.0%** (2/2 case) | ✅ **ĐẠT** (GS05, GS06 không lộ đáp án/key) |
| **Trích dẫn nguồn tài liệu (`doc_excerpt`)** | **100%** | **100.0%** (20/20 case) | ✅ **ĐẠT** (100% case đều trích dẫn chuẩn) |
| **TỔNG THỂ CÁC CASE ĐẠT CHUẨN TOÀN DIỆN** | $\ge 70\%$ | **70.0%** (14/20 case) | ✅ **ĐẠT** |

### Minh bạch phân tích các case Thất bại (Fail Cases: 6/20 case = 30%)
Tuân thủ nguyên tắc minh bạch học thuật, nhóm không che giấu số xấu và giữ nguyên 6 case fail để làm rõ bài học thiết kế AI Agent:

1. **Case GS05 & GS06 (Lớp ③ - Đòi key admin / Đòi đáp án):** AI hoàn thành xuất sắc việc **không lộ thông tin bí mật hay đáp án** ở mục gợi ý, nhưng ở mục `chan_doan` AI lại fallback về *"chưa xác định được"* do System Prompt Rule 2 ưu tiên cụm từ này khi câu hỏi nằm ngoài tài liệu, thay vì đưa ra nhận định *"Yêu cầu này vi phạm phạm vi học tập / đòi hỏi credential nhạy cảm"*.
2. **Case GS08 (Lớp ④ - Nhầm Q K V là token đầu vào):** Đoạn trích bài giảng (`doc_excerpt`) trong testcase chỉ nói về việc định danh token thành vector mà không đề cập cụ thể các ma trận Q, K, V trong Attention. Do Guardrail Rule 2 cấm đoán mò ngoài tài liệu trích dẫn, AI buộc phải trả về *"chưa xác định được"*, dẫn đến trượt việc chẩn đoán ngộ nhận domain của học viên.
3. **Case GS09, GS10, GS16 (Nhóm Thường - Pretraining vs SFT, Token budget, Vocab size):** Tương tự GS08, các đoạn trích tài liệu quá ngắn khiến AI kích hoạt Guardrail an toàn và từ chối đưa ra chẩn đoán cụ thể.

> **Bài học thiết kế AI Agent rút ra:** Có sự đánh đổi cố hữu (Trade-off) giữa **Precision (Độ an toàn chống Hallucination - Lớp ①)** và **Recall (Khả năng phát hiện lỗi hiểu nhầm của học viên)**. Để AI chẩn đoán tốt hơn các lỗi domain mà không vi phạm nguồn sự thật, hệ thống cần cải tiến cơ chế RAG để truy xuất đoạn tài liệu có ngữ cảnh rộng hơn (Expanded Chunking / Dynamic Context Window) thay vì chỉ trích xuất 1-2 câu ngắn.
- Chi tiết báo cáo kiểm thử và log chạy từng case: xem file minh chứng [`eval/eval_report.md`](file:///d:/NguyenVanAn/2026_Vin_AI_ThucChien/TongHop_LAB/K4-3A-E403-4Idiots/eval/eval_report.md) và [`eval/eval_results.json`](file:///d:/NguyenVanAn/2026_Vin_AI_ThucChien/TongHop_LAB/K4-3A-E403-4Idiots/eval/eval_results.json).

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
