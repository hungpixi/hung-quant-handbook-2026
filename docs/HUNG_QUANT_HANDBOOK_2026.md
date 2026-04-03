# HƯNG QUANT HANDBOOK 2026

## Trang Bìa

**Tên tài liệu:** `Hưng Quant Handbook 2026`  
**Phụ đề:** `Sổ tay 30 ngày xây nền quant forex, nghiên cứu MQL5, và dựng 4 cỗ máy kiếm tiền`  
**Tác giả:** `Hưng`

**Tinh thần của cuốn này:**

- Kính nghiệp.
- Tôn trọng thị trường.
- Học để sống sót trước, mở rộng sau.
- Xây hệ thống để dùng lại được, dạy lại được, và vận hành được.

---

## Lời Mở Đầu

Cuốn này không được viết như một bài content để đọc xong thấy hưng phấn vài giờ rồi bỏ đó. Nó cũng không được viết như một bài tổng hợp kiến thức chung chung, càng không phải một bản sao chép nguyên xi giọng điệu của người khác.

Tài liệu này được viết lại theo giọng của Hưng: thẳng, rõ, tôn trọng nghề, và xem trading là một môn phải học nghiêm túc như học một nghề kỹ thuật. Có thể điểm khởi đầu của vài ý tưởng đến từ một người chị làm content, nhưng phần trình bày ở đây đã được chuyển thành một hệ thống học tập và vận hành, không còn là giọng phán xét thị trường hay người đọc.

Mục tiêu của cuốn này có ba lớp:

1. Giúp người mới hiểu bản chất của việc giao dịch có lợi nhuận.
2. Giúp người đang có bot, có set, có cảm giác “đang lời” nhưng chưa biết mình đang ăn bằng cái gì, bắt đầu nhìn lại hệ thống một cách tỉnh táo.
3. Giúp người học có ngay một workflow thực tế trên Codex CLI và Antigravity để đọc, ghi chép, nghiên cứu, backtest, và biến tri thức thành tài sản có thể tái sử dụng.

Điều quan trọng nhất mà cuốn này muốn giữ là thái độ. Người đi được lâu trong thị trường thường không phải người nói mạnh nhất, cũng không phải người nhảy nhanh nhất. Thường là người biết mình đang học cái gì, đang test cái gì, đang sống nhờ edge nào, và biết lúc nào cần dừng lại để không tự hủy hệ thống của mình.

Cuốn này cũng được biên tập theo tinh thần của một tài liệu hướng dẫn thật: có mạch đọc, có bài tập, có worksheet, có checkpoint, có workflow, và có các lệnh thực thi cụ thể. Mục tiêu không phải làm người đọc thấy “ngầu”, mà làm người đọc bước được từ hiểu sang làm.

---

## Cách Dùng Cuốn Này

Cuốn này được thiết kế theo kiểu `handbook + workbook`, nghĩa là vừa có phần để đọc hiểu tổng thể, vừa có phần để làm bài tập, ghi chú, và biến kiến thức thành hành động.

Bạn có thể dùng theo ba cách.

### Cách 1: Đọc từ đầu đến cuối

Cách này phù hợp nếu bạn muốn có một bức tranh tổng thể trước khi bắt tay vào làm. Khi đọc tuần tự, bạn sẽ thấy được mạch logic như sau:

- Trading là một nghề có cấu trúc.
- Edge không nằm ở chỗ “bắt đúng vài lệnh”.
- Bot nhiều input không đồng nghĩa với bot mạnh.
- DCA không mặc định là xấu, nhưng rất dễ bị dùng sai vai trò.
- One-click setup không phải là đồ chơi cho đẹp, mà là thứ giúp bạn học đều, lưu đúng, và quay lại đúng chỗ khi cần.

### Cách 2: Học theo từng ngày

Đây là cách phù hợp nhất nếu bạn thật sự chỉ có 1-2 giờ mỗi ngày. Mỗi ngày bạn chỉ cần:

1. Chạy `qstart`.
2. Chạy `qday`.
3. Đọc đúng phần liên quan trong handbook.
4. Làm bài tập ngày đó.
5. Ghi lại một quyết định rõ ràng.

Cách học này ép bạn không bị lan man. Mỗi ngày chỉ cần một khái niệm, một hành động, một ghi chú, một quyết định.

### Cách 3: Tra cứu theo vấn đề

Khi bạn đang kẹt ở một bài toán cụ thể, ví dụ:

- Không biết phải backtest MQL5 cho bot nhiều module thế nào.
- Không biết xử lý `digit sensitivity` của broker ra sao.
- Không biết đọc file `.set` theo logic hệ thống như thế nào.
- Không biết nên lấy khoảng DCA bằng cảm giác hay bằng dữ liệu.
- Không biết làm affiliate broker theo hướng nghiêm túc thế nào.

thì bạn có thể nhảy trực tiếp đến chương tương ứng.

---

## Cam Kết 30 Ngày

Nếu muốn cuốn này có giá trị thật, bạn cần giữ 4 cam kết.

### Cam kết 1: Không tối ưu tham số khi chưa xác minh alpha

Đây là lỗi phổ biến nhất. Rất nhiều người mới có cảm giác “nghiên cứu rất chăm”, nhưng thật ra đang dành phần lớn thời gian để xoay tham số cho một signal vốn không có lợi thế đủ mạnh.

### Cam kết 2: Không dùng DCA như bằng chứng của edge

Nếu equity curve đẹp hơn nhờ DCA, điều đó chỉ chứng minh rằng DCA đã can thiệp vào đường vốn. Nó chưa chứng minh signal gốc có edge.

### Cam kết 3: Mỗi tuần phải có một quyết định giữ hoặc bỏ

Học mà không loại bớt thì không phải học, mà là tích lũy nhiễu. Sau mỗi tuần, bạn phải bỏ được cái gì đó: một tín niệm sai, một signal yếu, một thói quen tối ưu bừa, hay một phần bot không còn đáng giữ.

### Cam kết 4: Mỗi note phải kết thúc bằng hành động

Một note chỉ có ý nghĩa khi nó dẫn đến một bước tiếp theo rõ ràng: tiếp tục test, dừng test, thêm filter, đổi giả thuyết, hoặc loại bỏ hẳn.

---

## Mục Lục Rút Gọn

1. Nghề trading và vì sao phần lớn trader không có lợi nhuận.
2. Hướng đi tốt nhất cho retail trader năm 2026.
3. Bot 2.9.8, file `demo.set`, và bài toán alpha so với recovery.
4. Bốn cỗ máy kiếm tiền cần dựng song song.
5. Hệ thống one-click để học, test, và vận hành.
6. Lộ trình 30 ngày học kiểu có bài tập về nhà.
7. Tư duy backtest MQL5 cho bot nhiều logic.
8. Chuẩn hóa digits và đọc phổ giá để đề xuất khoảng DCA.
9. Worksheet, checklist, và checkpoint mỗi tuần.
10. Nguồn tham khảo và cách đi tiếp sau 30 ngày.

---

## Chương 1. Nghề Trading Và Cái Nhìn Thẳng Vào Sự Thật

### 1. Trading có lợi nhuận thật sự là gì

Trading có lợi nhuận bền vững không đến từ việc đoán đúng vài lần liên tiếp. Nó đến từ việc bạn sở hữu một hệ thống mà về dài hạn có khả năng tạo ra kỳ vọng dương, trong khi vẫn kiểm soát được xác suất chết tài khoản.

Một cách nói gọn:

`Lợi nhuận bền vững = Edge x Position Sizing x Regime Fit x Execution x Survival`

Nếu thiếu một trong năm cột này, hệ thống sẽ bị gãy theo một cách nào đó:

- Có edge mà sizing ngu thì chết vì chuỗi thua.
- Có signal đẹp mà sai regime thì vào đúng lúc thị trường không trả tiền cho kiểu đánh đó.
- Có entry hay mà execution tệ thì backtest đẹp, live xấu.
- Có lời ngắn hạn mà không sống đủ lâu thì edge cũng vô nghĩa.

### 2. Vì sao rất nhiều trader thua

Phần lớn trader không thua vì họ “ngu”. Họ thua vì làm sai trình tự học nghề. Họ thường:

- Tìm điểm vào lệnh trước khi hiểu mình đang kiếm tiền bằng cơ chế nào.
- Tìm indicator trước khi hiểu môi trường thị trường nào mới phù hợp với indicator đó.
- Tìm cách nhân nhanh tài khoản trước khi học cách kiểm soát khả năng sống sót.
- Tập trung vào winrate thay vì expectancy.
- Tập trung vào equity curve thay vì risk of ruin.

Một bot có thể thắng rất đều trong lịch sử, nhưng nếu toàn bộ vẻ đẹp đó được trả bằng một đuôi rủi ro khổng lồ thì nó không phải hệ thống bền. Nó chỉ là hệ thống chưa gặp đúng pha thị trường để bộc lộ điểm yếu.

Nói cách khác, thị trường không thường giết người vì một quyết định sai duy nhất. Nó thường giết người vì họ giữ quá lâu một cách hiểu sai về chính hệ thống của mình.

### 3. Hai thứ Hưng xem là lõi của nghề

Khi nhìn thị trường theo cách tối giản nhất, Hưng cho rằng có hai thứ cần nắm:

#### Lòng tham

Giá không chạy vì indicator. Giá chạy vì con người và dòng vốn phản ứng với kỳ vọng. Lòng tham, FOMO, tâm lý giữ lệnh thắng quá lâu, tâm lý gỡ lệnh thua, hay hành vi chase theo breakout đều là một phần của động lực giá.

#### Thặng dư

Một cặp giao dịch hoặc một nhịp thị trường chỉ có thể đi bền nếu còn dư địa để đi. Dư địa đó có thể đến từ:

- Dòng tiền mới.
- Chênh lệch định giá chưa đóng.
- Vị thế chưa được unwind hết.
- Sự mất cân bằng cung cầu chưa được hấp thụ xong.

Nếu không còn thặng dư, giá rất dễ quay về vùng cân bằng hoặc đảo chiều.

### 4. Điều người mới phải hiểu thật sớm

Người mới rất dễ nhầm ba thứ:

- Nhầm lãi tạm thời với edge thật.
- Nhầm drawdown nhỏ với hệ thống an toàn.
- Nhầm nhiều input với nghiên cứu sâu.

Trong thực tế:

- Một bot có hơn 200 input vẫn có thể chỉ là một bot không biết mình lời nhờ gì.
- Một set file đẹp vẫn có thể chỉ hợp với một broker, một phase, một điều kiện spread.
- Một chiến lược có thể đúng về hướng nhưng sai về cách triển khai nên cuối cùng vẫn lỗ.

### Bài tập Chương 1

Tạo file:

- `memory/concepts/edge-definition.md`

Và trả lời đầy đủ 5 câu:

1. Tôi nghĩ mình đang kiếm tiền từ đâu?
2. Tôi nghĩ mình sẽ mất tiền vì đâu?
3. Nếu bỏ DCA thì hệ thống của tôi còn gì?
4. Tôi đang hợp với loại thị trường nào nhất?
5. Tôi đang học để thắng nhanh hay để sống sót lâu?

---

## Chương 2. Hướng Đi Tốt Nhất Cho Retail Trader Năm 2026

### 1. Không cần đánh bại toàn bộ thị trường

Sự xuất hiện ngày càng dày của bot giao dịch, mô hình AI, execution algos, và việc thanh khoản bị quét nhanh hơn là chuyện thật. Điều đó làm thị trường ngắn hạn khó chịu hơn:

- Breakout giả xuất hiện dày hơn.
- Vùng sideway trở nên bẩn hơn.
- Stop bị quét nhanh hơn.
- Khả năng overtrade tăng mạnh.

Nhưng điều đó không có nghĩa retail hết cửa. Nó chỉ có nghĩa retail phải chọn trận đánh phù hợp hơn.

### 2. Những hướng vẫn đáng theo

#### Trend-following

Đây vẫn là hướng đáng nghiên cứu nhất với retail vì:

- Có logic kinh tế và hành vi rõ hơn.
- Có thể giải thích bằng dòng tiền, vị thế, và tâm lý đám đông.
- Có thể backtest đơn giản hơn so với nhiều hệ mơ hồ.
- Phù hợp với XAUUSD và một số cặp forex thanh khoản cao.

#### Breakout / Continuation

Nếu một thị trường đã nén đủ lâu và có động lực thật sự, continuation thường là phần retail còn có thể tận dụng tương đối tốt, miễn là:

- Chọn đúng khung giờ.
- Có filter tránh chop.
- Không dùng đòn quá lớn.
- Không cố bắt mọi cú phá.

Nếu áp dụng đúng, breakout không chỉ là chuyện “thấy phá là đuổi”. Breakout có giá trị khi bạn hiểu rằng có những giai đoạn thị trường phải rời vùng cân bằng cũ để đi tìm vùng cân bằng mới. Lúc đó, continuation không còn là trò đuổi giá mù quáng, mà là hành động đi theo dòng tiền đang thực sự di chuyển.

#### Regime-aware systems

Đây là nâng cấp tư duy rất quan trọng. Người không có tư duy regime thường hỏi:

“Signal nào ngon nhất?”

Người có tư duy regime hỏi:

- Hôm nay là trend day hay chop day?
- Session này có đáng trade không?
- Biến động hôm nay có khác thường không?
- Nếu spread đang nở, mình còn muốn vào theo kiểu cũ nữa không?

### 3. Những hướng không nên lấy làm trục chính trong 30 ngày đầu

- Indicator soup.
- Pattern kể chuyện nhưng không viết được thành rule testable.
- Martingale vô hạn.
- Tối ưu toàn bộ set một lần.
- SMC theo kiểu “nhìn có vẻ hợp” nhưng không chuyển được thành logic rõ.

### 4. Kết luận thực dụng

Nếu phải chọn một con đường tốt nhất cho giai đoạn hiện tại, Hưng sẽ chọn:

`simple systematic trend + strong risk controls + disciplined research loop`

Nói dễ hiểu: đánh ít hơn, rõ hơn, có kiểm chứng hơn.

Đánh ít hơn không phải vì nhát. Đánh ít hơn vì người có hệ thống không cần xuất hiện ở mọi nơi. Họ chỉ cần có mặt khi thị trường thật sự trả tiền cho kiểu chơi của mình.

### Bài tập Chương 2

Tạo file:

- `memory/concepts/why-trend-still-works.md`

Trả lời:

- Vì sao trend vẫn còn đất sống dù bot AI mạnh hơn?
- Trend thất bại trong những hoàn cảnh nào?
- Tôi sẽ dùng dấu hiệu nào để nhận diện chop?
- Tôi có chấp nhận bỏ qua rất nhiều lệnh chỉ để lấy những lệnh sạch hơn hay không?

---

## Chương 3. Bot 2.9.8, demo.set, Và Bài Toán Alpha So Với Recovery

### 1. Điều chúng ta đã biết từ file `demo.set`

File `demo.set` hiện tại cho thấy:

- Có `199` tham số.
- Có `28` nhóm chức năng.
- Các lớp liên quan đến `DCA` và `Sniper` đang là phần nổi bật nhất trong vận hành.
- Nhiều lớp filter hoặc lớp kiểm soát môi trường đang tắt.

Điều này dẫn đến một nhận định quan trọng: bot hiện tại không nên được xem như một bot “đa môi trường nên mạnh”. Nó nên được xem như một framework nhiều module, trong đó cần tách rõ:

1. Signal tạo alpha.
2. Filter tạo chọn lọc.
3. Sizing quyết định tốc độ phình rủi ro.
4. Recovery quyết định đường vốn nhìn ra sao.

### 2. Vì sao “nhiều signal, nhiều input” không mặc định là lợi thế

Có ba ảo giác rất dễ xuất hiện:

#### Ảo giác bao phủ

Cứ thấy có đủ RSI, Stoch, Ichimoku, BB, Momentum, Pinbar, Supertrend, UTBOT... là tưởng bot này “đi được mọi nơi”. Thực tế, rất có thể chỉ một phần rất nhỏ trong số đó là phần được dùng thật, còn lại là khả năng tiềm năng chưa được kích hoạt hoặc những tham số để tối ưu hóa bừa.

#### Ảo giác tối ưu

Càng nhiều tham số, người dùng càng có cảm giác “mình kiểm soát tốt hơn”. Nhưng trong nghiên cứu định lượng, nhiều chiều tham số đồng nghĩa với nguy cơ overfit cao hơn.

#### Ảo giác an toàn

Rất nhiều hệ thống nhìn “khó cháy” vì có DCA, Sniper, Hedging, hay các lớp cứu lệnh. Nhưng những lớp này không tạo edge nếu signal gốc không có kỳ vọng dương.

### 3. Nhận định tạm thời cho trường hợp XAUUSD + breakout

Trường hợp bạn mô tả về vàng đang có lời với signal Ichimoku breakout là một hướng đáng nghiên cứu. Nhưng cách nhìn đúng phải là:

- Có thể Ichimoku đang đóng vai trò trigger.
- Alpha thật có thể đến từ trend persistence của vàng.
- DCA đang đóng vai trò làm mượt quá trình hồi vốn.
- Nếu bỏ DCA mà hệ thống vẫn còn expectancy chấp nhận được, lúc đó mới có cơ sở nói signal có giá trị.

Đây là chỗ phải giữ thái độ rất tỉnh. Một set đang lời không phải là bằng chứng cuối cùng. Nó chỉ là một manh mối đủ tốt để tiếp tục mổ xẻ.

### 4. Điều tuyệt đối không nên làm

Không nên lấy một set hiện đang chạy ổn trên một broker, một symbol, một phase rồi suy ra rằng:

- Bot hợp mọi môi trường.
- Cứ nhiều signal là càng mạnh.
- Chỉ cần tối ưu thêm vài chục input nữa là sẽ tốt hơn.

### 5. Cách đọc bot theo 4 lớp

#### Lớp 1: Signal

Bot vào lệnh vì điều gì?  
Đây là lớp cần xác minh đầu tiên.

#### Lớp 2: Filter

Bot có biết khi nào không nên trade không?  
Nếu không có lớp này, rất nhiều lệnh chỉ là “thấy tín hiệu thì vào”.

#### Lớp 3: Sizing

Bot tăng lot, giới hạn lot, và phân bổ lot theo quy tắc nào?

#### Lớp 4: Recovery

Bot xử lý chuỗi lệnh âm như thế nào? DCA, Sniper, Hedging, Open Opposite... đang đóng vai trò gì?

### Bài tập Chương 3

Đọc:

- `memory/bots/bot-298-set-analysis.md`
- `research/bot-298-ablation-plan.md`

Chạy:

```powershell
.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set
```

Sau đó ghi lại:

- 10 biến cần test đầu tiên.
- 5 biến tuyệt đối chưa được tối ưu lung tung.
- 3 giả thuyết lớn nhất về việc bot đang lời nhờ gì.

---

## Chương 4. Bốn Cỗ Máy Kiếm Tiền

### 1. Cỗ máy 1: Trader Engine

Đây là cỗ máy tạo tiền trực tiếp từ giao dịch. Nó không cần phải quá nhiều chiến lược. Trong giai đoạn 30 ngày đầu, chỉ nên hướng tới:

- Một engine chủ lực cho XAUUSD.
- Một engine phụ cho một rổ nhỏ forex hoặc một setup session rõ.

Output bắt buộc của cỗ máy này phải bao gồm:

- Strategy spec.
- Set file chính.
- Nhật ký giao dịch.
- Dashboard theo dõi kết quả.

### 2. Cỗ máy 2: Research Engine

Đây là cỗ máy nhiều người bỏ qua nhất nhưng lại là thứ quyết định bạn có tiến bộ thật hay không.

Nó phải sinh ra:

- Note giả thuyết mỗi ngày.
- Protocol backtest.
- Weekly review.
- Danh sách giữ / bỏ.

Nếu không có cỗ máy nghiên cứu, bạn sẽ rất dễ bám vào một phiên bản bot đang lời tạm thời và ngừng học.

### 3. Cỗ máy 3: Product Engine

Nếu bạn thật sự muốn đi xa hơn trading cá nhân, bạn cần biết đóng gói:

- Playbook.
- Báo cáo.
- Bộ set.
- Bộ tài liệu hướng dẫn.
- Bộ nội dung có thể dùng lại để training hoặc onboarding.

### 4. Cỗ máy 4: Distribution Engine

Đây là nơi affiliate broker, referral, content, case study, và onboarding đi vào hệ thống.

Điểm Hưng muốn giữ rất rõ là: affiliate chỉ thật sự là một nghề tử tế khi bạn xem mình đang cung cấp một dịch vụ hỗ trợ trader sống sót lâu hơn, chứ không phải kéo volume cho bằng được.

Điều này có nghĩa:

- Không hứa lợi nhuận.
- Không đẩy người mới vào overtrade.
- Không giấu drawdown.
- Không lấy volume làm thước đo duy nhất.

### Bài tập Chương 4

Tạo file:

- `memory/brokers/affiliate-manifesto.md`

Trả lời:

- Tôi đang giúp trader điều gì?
- Tôi tuyệt đối không làm điều gì?
- Trader nào phù hợp với hệ thống của tôi?
- KPI thành công của tôi ngoài tiền referral là gì?

---

## Chương 5. Hệ Thống One-Click Xuyên Suốt Quá Trình Học

### 1. One-click không chỉ là cài máy

Nhiều người khi nghe “one-click setup” chỉ nghĩ đến chuyện cài tool cho nhanh. Nhưng trong một hệ học tập và nghiên cứu nghiêm túc, one-click phải giải quyết cả vòng đời công việc:

- Cài máy.
- Mở đúng workflow trong ngày.
- Tạo đúng file cần viết.
- Gợi đúng bước tiếp theo.
- Giúp quay lại đúng chỗ khi nghỉ một thời gian.

Đó là lý do one-click được đưa vào lõi của cuốn này, chứ không bị để ở phần phụ lục. Nếu workflow đủ tốt, nó sẽ kéo cả kỷ luật của bạn lên theo. Nếu workflow tệ, bạn sẽ liên tục mất năng lượng vào việc nhớ xem mình đang ở đâu.

### 2. Flow làm việc hiện có

#### Bước 1: Bootstrap

```powershell
.\scripts\bootstrap\windows\setup.ps1
```

Script này:

- Kiểm tra `git`, `python`, `uv`, `node`, `codex`, `antigravity`.
- Tạo cây thư mục chuẩn.
- Tạo file mẫu cho note và weekly review.
- In ra các lệnh cần nhớ.

#### Bước 2: Khởi động ngày học

```powershell
.\scripts\start\qstart.ps1
```

Lệnh này nhắc bạn:

- nhịp 90 phút nên học thế nào
- đọc tài liệu gì
- viết note ở đâu
- lệnh tiếp theo nên chạy là gì

#### Bước 3: Đi vào ngày học cụ thể

```powershell
.\scripts\start\qday.ps1 -Day 8
```

Lệnh này:

- tạo file note đích nếu chưa có
- chỉ đúng đường dẫn cần viết
- ép bạn kết thúc bằng một quyết định

#### Bước 4: Review theo tuần

```powershell
.\scripts\start\qreview.ps1 -Week 1
```

Lệnh này:

- tạo file review tuần
- buộc bạn nhìn lại những gì còn đúng và những gì phải bỏ

#### Bước 5: Phân tích set file

```powershell
.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set
```

#### Bước 6: Phân tích phổ giá từ CSV

```powershell
.\scripts\start\qanalyze-symbol-csv.ps1 -CsvFile .\data\XAUUSD_M15.csv -Digits 2
```

### 3. Cấu trúc thư mục để tư duy không bị tản

```text
docs/
memory/
research/
reports/
journals/
scripts/
templates/
```

Mỗi thư mục có một vai trò riêng:

- `docs/`: handbook, playbook, tài liệu nền.
- `memory/`: tri thức đã chốt, có thể gọi lại.
- `research/`: giả thuyết, protocol, kết quả test.
- `reports/`: tổng kết tuần, tổng kết tháng.
- `journals/`: nhật ký học và nhật ký giao dịch.
- `scripts/`: các entry points one-click.

### 4. Cách lưu tri thức để dùng lại

Mỗi note phải có đủ 6 mục:

1. Giả thuyết.
2. Lý do tin.
3. Cách kiểm chứng.
4. Kết quả hiện tại.
5. Quyết định.
6. Lệnh gọi lại.

Khi làm đúng, bạn sẽ dần có một kho tri thức vận hành được chứ không chỉ là các file ghi chép rời rạc.

---

## Chương 6. Lộ Trình 30 Ngày

### Tinh thần chung

Mỗi ngày chỉ cần giữ 4 trụ cột:

- `Học`: chỉ một khái niệm.
- `Làm`: phải động tay vào chart, bot, hoặc data.
- `Viết`: để lại dấu vết tri thức.
- `Gọi lệnh`: dùng đúng one-click để workflow không vỡ.

### Tuần 1: Xây nền tư duy đúng

**Ngày 1:** Định nghĩa edge.  
**Ngày 2:** Cung cầu và động lực thị trường.  
**Ngày 3:** Trend persistence.  
**Ngày 4:** Sơ đồ bot 2.9.8.  
**Ngày 5:** Phản biện bot của chính mình.  
**Ngày 6:** Xếp hạng các signal.  
**Ngày 7:** Weekly review.

Mục tiêu của tuần 1 không phải kiếm ra thêm signal mới. Mục tiêu là bỏ đi sự mơ hồ.

### Tuần 2: Xây engine có thể sống

**Ngày 8:** Đào sâu XAUUSD và breakout.  
**Ngày 9:** Viết strategy spec.  
**Ngày 10:** Dựng regime map.  
**Ngày 11:** Viết risk engine.  
**Ngày 12:** Đặt DCA đúng vai trò.  
**Ngày 13:** Dựng execution guard.  
**Ngày 14:** Weekly review.

### Tuần 3: Backtest như người nghiên cứu

**Ngày 15:** Viết protocol test.  
**Ngày 16:** Test signal only.  
**Ngày 17:** Filter ablation.  
**Ngày 18:** Sizing comparison.  
**Ngày 19:** Stress test.  
**Ngày 20:** Parameter stability.  
**Ngày 21:** Weekly review.

### Tuần 4: Vận hành và mở rộng

**Ngày 22:** Live ops SOP.  
**Ngày 23:** Research loop.  
**Ngày 24:** Product engine.  
**Ngày 25:** Affiliate engine.  
**Ngày 26:** Teaching outline.  
**Ngày 27:** Knowledge base map.  
**Ngày 28:** Bootstrap test.  
**Ngày 29:** Daily rhythm.  
**Ngày 30:** Lệnh cho tháng 2.

### Kết quả kỳ vọng sau 30 ngày

Bạn chưa cần trở thành “quái vật lợi nhuận”. Nhưng bạn nên có:

- Một hướng nghiên cứu rõ.
- Một hệ thống note và review không lộn xộn.
- Một hoặc hai engine xứng đáng nghiên cứu sâu hơn.
- Một góc nhìn tỉnh táo hơn về DCA, recovery, và risk.
- Một workflow thực sự chạy được trên máy.

Nếu bạn làm đều, 30 ngày sau bạn chưa cần giàu hơn rất nhiều. Nhưng bạn phải trở nên khó bị lừa hơn. Đó là bước tiến thật.

---

## Chương 7. Tư Duy Backtest MQL5 Cho Bot Nhiều Logic

### 1. Sai lầm phổ biến nhất

Sai lầm phổ biến nhất là nạp set vào Strategy Tester, thấy đường vốn đẹp, rồi nghĩ rằng mình đang “backtest nghiêm túc”.

Với bot như 2.9.8, cách đó gần như chắc chắn dẫn đến hiểu sai. Vì một hệ thống nhiều logic cần được tách từng lớp để kiểm chứng.

### 2. Thứ tự backtest đúng

#### Bước 1: Chuẩn hóa môi trường

Bạn phải ghi rõ:

- Broker nào.
- Symbol nào.
- Digits bao nhiêu.
- Tick size bao nhiêu.
- Spread thường là bao nhiêu.
- Khung giờ và timezone nào.

#### Bước 2: Xác minh signal

Tắt:

- DCA
- Sniper
- Hedging
- Trailing

Chỉ giữ lại signal và cấu trúc đóng lệnh tối thiểu nếu cần. Nếu bước này không có giá trị, mọi bước sau đều đáng ngờ.

#### Bước 3: Thêm filter

Lần lượt test:

- Trading time
- EMA filter
- MACD filter
- Zone cycle

Không bật cùng lúc ngay từ đầu.

#### Bước 4: Thêm sizing và DCA

Sau khi signal đã có cơ sở, mới bắt đầu xem:

- `multiplier`
- `distance ladder`
- `TPDCA`
- `max lots`

#### Bước 5: Thêm recovery nâng cao

Đây phải là lớp cuối cùng:

- Sniper
- Hedging
- Open opposite
- Balance lot

### 3. KPI bắt buộc

Bạn không được chỉ nhìn net profit. Cần ít nhất:

- Net profit
- Profit factor
- Max drawdown
- Recovery factor
- Longest losing run
- Max concurrent orders
- Time in drawdown

### 4. Quy tắc ra quyết định

- Nếu signal only âm sâu, đừng gọi recovery là edge.
- Nếu filter làm DD giảm rõ mà expectancy không sụp, filter đó đáng giữ.
- Nếu tham số chỉ đẹp ở một vùng rất hẹp, khả năng cao là overfit.
- Nếu broker đổi một chút mà kết quả khác hẳn, chưa được phép live rộng.

Điều này nghe có vẻ đơn giản nhưng lại rất quan trọng. Một hệ thống chỉ sống được trên đúng một bộ điều kiện lý tưởng thì không phải hệ thống mạnh. Nó chỉ là một cấu hình đang hợp thời.

---

## Chương 8. Chuẩn Hóa Digits Và Đọc Phổ Giá Để Đề Xuất Khoảng DCA

### 1. Vì sao digits là vấn đề lớn

Một tham số `distance=10` không có nghĩa gì nếu bạn chưa biết:

- Broker đó quote bao nhiêu digits.
- EA xử lý theo `Point`, `Pip`, hay khoảng giá tuyệt đối.
- Tick size của symbol đó là gì.

Đây là lý do rất nhiều người copy set giữa các broker rồi than rằng:

- cùng bot nhưng kết quả khác hẳn
- cùng symbol nhưng broker này êm, broker kia mệt
- backtest được mà live không khớp

### 2. Cách nghĩ đúng về khoảng DCA

Không nên nghĩ:

“Để 10 thấy hợp mắt.”

Nên nghĩ:

“Với symbol này, timeframe này, signal này, adverse excursion thường nằm ở đâu, ATR trung vị là bao nhiêu, khoảng rung lắc điển hình là bao nhiêu, rồi mới quy đổi về distance.”

### 3. Quy trình đề xuất khoảng DCA bằng dữ liệu

1. Xuất CSV OHLC từ MT5.
2. Chạy script đọc phổ giá.
3. Ghi lại:
   - median range
   - P75 range
   - P90 range
   - median ATR
4. Tạo 3 bộ set:
   - `tight`
   - `mid`
   - `wide`
5. Backtest cùng signal, cùng giai đoạn, chỉ thay ladder.

### 4. Điều đang thiếu và hướng đi tiếp

Hiện trong workspace đã có tool để đọc phổ giá cơ bản. Bước tiếp theo nếu muốn đi sâu hơn là xây thêm một engine nghiên cứu excursion:

- nhận dữ liệu giá
- nhận logic entry giả định
- đo adverse excursion sau entry
- đề xuất `distance0`, `distance ladder`, `max layers`

Đó mới là hướng đi gần với ý bạn nói: “đọc dữ liệu rồi đề xuất khoảng DCA hợp lý, sau đó mới backtest.”

Một khi đi theo hướng này, bạn bắt đầu rời khỏi vùng “chỉnh set theo cảm giác” để bước vào vùng “thiết kế ladder theo dữ liệu”. Đây là thay đổi rất lớn trong chất lượng tư duy.

---

## Chương 9. Worksheet Và Checkpoint

### Worksheet 1: Edge Statement

Trả lời thật nghiêm túc:

- Edge của tôi là gì?
- Nó tồn tại trong điều kiện nào?
- Nó chết trong điều kiện nào?
- Tôi đo nó bằng chỉ số nào?

### Worksheet 2: Bot Review

- Bot của tôi vào lệnh vì lý do gì?
- Bot của tôi cứu lệnh bằng cách nào?
- Phần nào tạo alpha?
- Phần nào chỉ làm đẹp đường vốn?

### Worksheet 3: Broker Profile

- Broker:
- Symbol:
- Digits:
- Tick size:
- Spread median:
- Spread xấu:
- Session chính:
- Ghi chú thực thi:

### Checkpoint Mỗi Tuần

Cuối mỗi tuần, phải trả lời:

- Tuần này tôi học được gì mà vẫn còn đúng?
- Tôi đã bỏ được cái gì?
- Tôi đang tự lừa mình ở đâu?
- Tuần sau tôi chỉ giữ lại một hướng nào?

---

## Chương 10. Tinh Thần Làm Nghề

Hưng muốn chốt cuốn này bằng một quan điểm rất rõ: trading là nghề, không phải một cuộc thi nói mạnh hơn ai. Bot, affiliate, content, training, hay product hóa đều có thể là con đường tử tế nếu mình đặt giá trị thật và sự sống còn dài hạn lên trên cảm giác thắng nhanh.

Mục tiêu sau 30 ngày không phải là trở thành “thần đồng”. Mục tiêu là:

- Biết mình đang học cái gì.
- Biết mình đang test cái gì.
- Biết mình đang sống nhờ edge nào.
- Biết khi nào nên dừng.
- Biết cách để lại hệ thống cho chính mình và cho người khác dùng được.

Nếu đạt được chừng đó, bạn đã đi xa hơn rất nhiều người chỉ chăm chăm tìm lệnh.

---

## Nguồn Tham Khảo

- OpenStax Writing Guide Handbook, để lấy cảm hứng về cách tổ chức handbook tra cứu: https://openstax.org/books/writing-guide/pages/handbook
- Moskowitz, Ooi, Pedersen, *Time Series Momentum*: https://www.sciencedirect.com/science/article/pii/S0304405X11002613
- AQR, *A Century of Evidence on Trend Following*: https://www.aqr.com/insights/research/journal-article/a-century-of-evidence-on-trend-following-investing
- BIS on FX market structure: https://www.bis.org/publ/mktc13.htm
- NBER, *Machine Learning in Asset Management*: https://www.nber.org/papers/w33351

---

## Kết

Cuốn sách này chỉ có giá trị khi nó trở thành hệ thống làm việc của bạn. Bước nhỏ nhất để bắt đầu là:

```powershell
.\scripts\bootstrap\windows\setup.ps1
.\scripts\start\qstart.ps1
.\scripts\start\qday.ps1 -Day 1
```

Sau đó đừng cố làm quá nhiều. Hãy làm đúng việc của ngày hôm nay, ghi lại cho sạch, và để thị trường dạy mình một cách có cấu trúc.

Nếu chia sẻ cuốn này cho người khác, Hưng muốn nó được chia sẻ đúng tinh thần của nó: không phải để ai đó hưng phấn rồi lao vào thị trường, mà để họ có một nền học nghề tử tế hơn, bớt trả học phí vô ích hơn, và biết quý trọng nghề hơn.
