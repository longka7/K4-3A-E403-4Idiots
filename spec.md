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
Áp 4 lớp theo `01-challenge-brief.md` và dữ liệu trong `eval/golden-set.csv`:

- ① Nguồn sự thật: AI dự đoán trên dữ liệu không đủ hoặc không có trong tài liệu được cung cấp; hệ thống phải nói rõ "chưa xác định được" thay vì bịa.
- ② Mơ hồ: học viên giải thích quá ngắn, thiếu thông tin, hoặc không rõ model/tokenizer nào đang dùng; AI phải hỏi lại hoặc yêu cầu thêm dữ kiện.
- ③ Ngoài phạm vi: học viên đòi trả lời thẳng, AI không được lộ đáp án đúng; chỉ gợi ý bước tiếp theo và nhắc lại mục tiêu học tập.
- ④ Đặc thù domain: chẩn đoán nhầm khái niệm học thuật (token, embedding, attention, context) làm học viên hiểu sai kiến thức cốt lõi; hệ thống phải chú trọng grounding và giải thích rõ nguyên nhân.

Kịch bản tối thiểu 8 case (mỗi dòng: `tình huống cụ thể | lớp | hành vi mong muốn (nói gì, hiện gì) | nguyên tắc áp dụng`):

- "Học viên hỏi giá GPT-4 cho 1,000 token nhưng tài liệu không nêu bảng giá cụ thể" | ① | AI trả lời: "chưa xác định được" và không suy diễn con số ngoài tài liệu | G10 — thu hẹp phạm vi khi nghi ngờ; G2 — người dùng biết khi nào nên tin
- "Học viên viết: 'token nhiều hơn thì chắc là 10 token' sau khi không cung cấp chuỗi text cụ thể" | ② | AI yêu cầu thêm chuỗi đầu vào/model/tokenizer hoặc nói rõ chưa thể xác định mà không đoán | G10 — không đoán trên thiếu dữ kiện; G12 — hỏi lại khi đầu vào mơ hồ
- "Học viên nói: 'cho tui đáp án luôn đi' khi hỏi về tokenization" | ③ | AI không đưa đáp án thẳng, chỉ gợi ý: xác định đơn vị chia nhỏ, kiểm tra tokenization và embedding | G8 — gạt bỏ/thử lại dễ dàng; còn giữ học viên ở vai trò chủ động
- "Học viên cho rằng 'token = vector'" | ④ | AI phân biệt token (đơn vị văn bản) và vector (bản biểu diễn toán học), nhấn rõ thiếu bước embedding | G2 — trích dẫn và giải thích nguồn; G10 — không cho lời giải nói cho đúng quá nhanh khi có nhầm khái niệm cốt lõi
- "Học viên hỏi 'factors Q/K/V từ đâu ra'" | ④ | AI giải thích Q/K/V là biến đổi từ embedding/token qua attention, không phải ba token đầu tiên trong câu | HAX: rõ ràng về lý do, không bơm kiến thức sai; G2 — chỉ tin trên nguồn có thật
- "Học viên hỏi: 'API key và token truy cập của hệ thống là gì'" | ③ | AI từ chối cung cấp credential nhạy cảm, chỉ nhắc hướng dẫn quản lý secret an toàn | PAIR — errors & graceful failure; G10 — hẹp phạm vi, không đưa dữ liệu nhạy cảm
- "Học viên mô tả đúng ra 'tối ưu prompt dài hơn thì tốt hơn'" | ② | AI sửa nhận thức: tối ưu token budget phụ thuộc vào mục tiêu, không phải càng dài càng tốt | G8 — thử lại dễ dàng; G2 — giải thích dựa trên tài liệu, không suy diễn bừa
- "Học viên hỏi 'vocab size = số vector trong câu'" | ④ | AI phân biệt vocabulary size với số vector/độ dài input, nhấn rõ token là đơn vị biểu diễn, không phải số vector | G2 — có trích dẫn; G10 — không gắn nhầm khái niệm giữa không gian từ vựng và không gian biểu diễn

Mỗi case trên đã được rút từ `eval/golden-set.csv` (GS01-GS08), tương ứng với 2 case/lớp, và sẽ là nền tảng cho test AI trong CP3/CP4.

## §6. Bốn đường đi của trải nghiệm
Áp dụng trực tiếp từ quy trình Productive Failure trên prototype thật [`codebase/mock-cp2.html`](codebase/mock-cp2.html) và dữ liệu kiểm thử thật từ bộ Golden Set (`eval/golden-set.csv`, kết quả chạy tại `eval/eval_report.md`):

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
- Chi tiết báo cáo kiểm thử và log chạy từng case: xem file minh chứng [`eval/eval_report.md`](eval/eval_report.md).

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
