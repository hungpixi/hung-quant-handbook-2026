# BÁO CÁO CHIẾN LƯỢC 2026 CỦA HƯNG

> Tài liệu gốc được viết lại ngày 03/04/2026.
> 
> Bản này không dùng lại văn phong content gây sốc. Nội dung được sắp xếp lại theo hướng kính nghiệp, tôn trọng thị trường, tôn trọng người học, và ưu tiên khả năng vận hành thật.

---

## Lời mở đầu

Tài liệu này được viết lại từ một nguồn cảm hứng của một người chị làm content. Phần ảnh hưởng về góc nhìn vẫn còn, nhưng giới thiệu, cách lập luận, và cách hành động đã được chuyển thành giọng của Hưng: đi thẳng vào vấn đề, giữ lòng tôn trọng thị trường, và xem trading là một nghề cần học bài bản.

Nếu một tài liệu chỉ làm người đọc thấy hưng phấn, tài liệu đó chưa đủ. Nếu một tài liệu chỉ đưa ra dự báo mà không dạy cách tự kiểm chứng, tài liệu đó cũng chưa đủ. Bản này có 3 mục tiêu:

1. Dạy người mới hiểu bản chất việc giao dịch có lợi nhuận.
2. Xây một lộ trình 30 ngày để đi từ học lan man sang học có hệ thống.
3. Dựng một bộ môi trường one-click để quá trình học, nghiên cứu, viết note, backtest, và vận hành không bị đứt quãng.

Trading là một nghề cần sự tôn nghiêm. Thị trường không nợ ai cả, nhưng cũng không đối xử tệ với người biết học và biết giữ mình.

---

## Phần I. Bản chất nghề trading

### 1. Vì sao đa số trader không có lợi nhuận

Đa số trader thua không phải vì kém thông minh. Họ thua vì làm sai thứ tự:

- Tìm entry trước khi hiểu edge.
- Tìm indicator trước khi hiểu thị trường đang có regime gì.
- Tìm cách nhân đôi tài khoản trước khi học cách sống sót.
- Dùng DCA để kéo dài thời gian đến lúc gặp một nhát cắt đứt toàn bộ lợi nhuận.
- Nhiều người nhầm drawdown tạm thời với khả năng sống sót dài hạn.

Nếu phải gom gọn trong một công thức, trading có lợi nhuận bền vững là:

`Expectancy x Position Sizing x Regime Fit x Execution Quality x Survival`

Trong đó:

- `Expectancy`: về dài hạn, mỗi lệnh có giá trị kỳ vọng dương.
- `Position Sizing`: đánh đúng kích thước để khi sai vẫn còn sống.
- `Regime Fit`: dùng chiến lược đúng lúc.
- `Execution Quality`: spread, slippage, session, tin tức không phá nát hệ thống.
- `Survival`: sống đủ lâu để edge được biểu lộ.

### 2. Hai thứ Hưng xem là lõi của nghề

- `Lòng tham`: người trong thị trường luôn chạy theo kỳ vọng lợi nhuận, FOMO, và ham muốn giá đi tiếp.
- `Thặng dư`: một cặp giao dịch hay một thị trường chỉ có thể cho xu hướng bền khi dòng tiền, nhu cầu, hoặc áp lực định giá thực sự còn dư địa để đi thêm.

Nói ngắn gọn:

- Không có động cơ tiếp diễn, trend yếu.
- Không có thặng dư, giá dễ trở lại cân bằng.
- Không có kỷ luật, trader sẽ tự huỷ edge của chính mình.

### 3. Điều trader mới cần hiểu sớm

- Thị trường không thưởng sự tự tin vô căn cứ.
- Một robot có winrate cao không có nghĩa là một hệ thống mạnh.
- Một backtest đẹp chưa chắc là một cỗ máy có thể live.
- DCA có thể là công cụ quản trị vị thế có điều kiện, nhưng nếu nó là lý do duy nhất equity curve đẹp thì đó là tín hiệu cảnh báo.

### Bài tập về nhà 01

Viết file note đầu tiên với tên `memory/concepts/edge-definition.md` trả lời 5 câu:

1. Tôi đang có thể kiếm tiền từ đâu?
2. Tôi đang có thể mất tiền vì đâu?
3. Nếu bỏ DCA thì hệ thống còn gì?
4. Thị trường nào hợp với tôi nhất hiện tại?
5. Tôi muốn học để sống sót, hay học để thắng nhanh?

---

## Phần II. Hướng đi tốt nhất trong trading năm 2026

### 1. Không cần đánh bại mọi bot AI

Thị trường thay đổi vì AI và bot mạnh hơn là thật. Thanh khoản bị quét nhanh hơn, breakout giả xuất hiện nhiều hơn, và những vùng sideway ngắn hạn khó nhai hơn. Nhưng điều đó không xoá bỏ toàn bộ edge của retail.

Thứ retail vẫn còn có thể làm tốt:

- Chọn thị trường và khung giờ đúng.
- Dùng hệ trend-following và continuation.
- Thêm regime filter để tránh chop.
- Giảm tần suất, tăng chất lượng lệnh.
- Lấy risk engine làm cột sống.

### 2. Những họ chiến lược đang còn giá trị

#### Trend-following

Đây là họ chiến lược đáng để nghiên cứu nhất cho retail.

- Dễ giải thích.
- Dễ backtest hơn so với signal huyền học.
- Có tính bền trên nhiều thị trường.
- Phù hợp với XAUUSD và một số cặp forex thanh khoản cao.

#### Breakout / Continuation

Phù hợp khi:

- thị trường có động lực thực sự
- có nhịp nén trước đó
- thanh khoản đủ dày
- session và vol ủng hộ

#### Regime-aware systems

Không hỏi "signal nào ngon nhất", mà hỏi:

- Hôm nay là trend day hay chop day?
- Session này có thích hợp để bắt breakout không?
- Lúc nào phải giảm size?
- Lúc nào phải tắt máy?

#### Volatility-aware sizing

Không phải lệnh nào cũng đặt cùng một lot. Thị trường biến động khác nhau cần size khác nhau.

### 3. Những hướng không nên lấy làm cốt sống tháng đầu

- Indicator soup.
- Chiêu trò chọn lẻ, mê tín pattern, vào lệnh vì thấy "có vẻ đúng".
- SMC nếu chưa viết thành rule có thể test được.
- Martingale vô hạn.
- Tối ưu tham số chỉ để đẹp đường vốn quá khứ.

### Bài tập về nhà 02

Viết file `memory/concepts/why-trend-still-works.md` trả lời:

- Vì sao trend vẫn tồn tại dù AI mạnh hơn?
- Điều gì làm trend fail?
- Tôi sẽ nhận diện chop bằng cách nào?
- Tôi có chấp nhận bỏ qua nhiều lệnh để đợi lệnh đẹp hơn không?

---

## Phần III. Bot 2.9.8 và bài toán "nhiều signal, hơn 200 input"

### 1. Nhìn đúng vấn đề

Một bot có 4 nhóm logic và hơn 200 input không mặc định là xấu. Nhưng nó chỉ tốt khi mỗi input thuộc một vai trò rõ ràng.

Nếu không, nó sẽ tạo ra 3 ảo giác:

- `Ảo giác bao phủ`: tưởng như đánh được mọi môi trường.
- `Ảo giác tinh chỉnh`: tưởng như chỉ cần vặn tham số là ra lời.
- `Ảo giác an toàn`: tưởng như DCA là làm giảm rủi ro.

### 2. Các nhóm input cần tách ra

Khi có file `.set`, phân tích cần tách thành 4 tầng:

- `Signal`: vào lệnh vì lý do gì?
- `Filter`: môi trường nào mới được vào?
- `Sizing`: vào bao nhiêu?
- `Recovery`: sai thì xử lý ra sao?

### 3. Các câu hỏi phải trả lời

- Nếu chỉ giữ signal mà bỏ DCA, bot còn có expectancy dương không?
- Nếu bỏ một nhóm filter, equity curve xấu lên bao nhiêu?
- Nếu đổi từ XAUUSD sang EURUSD hay GBPUSD, logic còn giữ được không?
- Nếu gặp giai đoạn sideway dài, bot sống được không?

### 4. Nhận định tạm thời về trường hợp XAUUSD + Ichimoku breakout

Trường hợp bạn nêu ra rất đáng đào sâu. Giả thuyết làm việc tốt nhất hiện tại là:

- Ichimoku breakout có thể không phải alpha duy nhất.
- Alpha thật có thể đến từ trend persistence và continuation của vàng.
- DCA đang có thể đóng vai trò làm mềm đường vốn nhiều hơn là tạo edge.
- Vàng có những phase có narrative và dòng tiền rõ hơn nên breakout dễ "sống" hơn nhiều cặp khác.

Không nên kết luận sớm là "Ichimoku thần kỳ". Việc đúng cần làm là `ablation test`.

### 5. Framework backtest đúng cho bot 2.9.8

Không có cách backtest nào hợp cho mọi môi trường. Có `framework backtest` hợp cho nhiều loại môi trường:

1. Test signal gốc, không DCA.
2. Test signal gốc + filter.
3. Test signal gốc + filter + sizing.
4. Test thêm recovery như một lớp bổ sung.
5. Chạy stress test spread/slippage/session/news.
6. Chạy out-of-sample.
7. Chạy parameter stability, không tìm điểm đẹp nhất.

Nếu bước 1-3 không có edge mà bước 4 mới đẹp, thì hệ thống đang bán tail risk.

### Bài tập về nhà 03

Khi bỏ file `.set` vào workspace, tạo bảng:

| Input | Nhóm | Giả thuyết tác dụng | Mức độ quan trọng | Có thể bỏ? |
| --- | --- | --- | --- | --- |

Mục tiêu của bài tập này là ép hơn 200 input xuống:

- 10-15 input cột sống
- 20-30 input phụ
- phần còn lại đưa vào nhóm "chưa chứng minh được giá trị"

---

## Phần IV. Bốn cỗ máy kiếm tiền

### 1. Cỗ máy 1: Trader Engine

Đây là hệ thống ra tiền trực tiếp từ trading.

Mục tiêu:

- 1 engine chủ lực cho XAUUSD
- 1 engine phụ cho một rổ FX nhỏ
- MQL5 để live
- có risk engine rõ ràng

Output bắt buộc:

- strategy spec
- setfile chính
- dashboard kết quả
- nhật ký theo ngày

### 2. Cỗ máy 2: Research Engine

Đây là bộ máy giúp bạn không đứng yên ở một phiên bản bot.

Mục tiêu:

- mỗi ngày 1 note giả thuyết
- mỗi tuần 1 report
- mỗi tháng 1 danh sách giữ/bỏ

Không có research engine, trader engine sẽ dần trở nên mê tín và bị thị trường "lấy lại học phí".

### 3. Cỗ máy 3: Product Engine

Đây là cách đóng gói những thứ bạn đã xây:

- bộ setfile
- bộ playbook
- bộ báo cáo
- bộ giáo trình cho người học

Nếu làm đúng, đây là cầu nối giữa trading thực chiến và việc mở rộng thu nhập.

### 4. Cỗ máy 4: Distribution Engine

Đây là affiliate, referral, content, case study, và onboarding.

Hưng đề xuất xem đây là một nghề phù hợp nếu bạn giữ đúng tinh thần:

- không lừa người mới vào overtrade
- không bán giấc mơ giàu nhanh
- không dùng ref như KPI duy nhất
- lấy `trader survival` làm KPI hàng đầu

Ref broker như Exness, XM, hoặc các sàn khác có thể là một "chánh nghiệp" nếu vai trò của bạn là:

- giúp trader vào đúng loại tài khoản
- giúp họ hiểu risk
- giúp họ có quy trình giao dịch rõ ràng
- giúp họ sống sót lâu hơn trong thị trường

### Bài tập về nhà 04

Viết file `memory/brokers/affiliate-manifesto.md` trả lời:

- Tôi đang giúp trader điều gì?
- Tôi từ chối làm những điều gì?
- Trader nào phù hợp vào hệ thống của tôi?
- KPI thành công của tôi có những gì ngoài volume?

---

## Phần V. One-click setup xuyên suốt quá trình học

### 1. Mục tiêu của one-click

One-click không chỉ để cài máy. One-click phải giúp:

- vào bài học hôm nay ngay lập tức
- mở đúng note cần viết
- nhớ mình đang học đến đâu
- tạo report đúng mẫu
- giảm ma sát trong việc học và nghiên cứu

Nếu mỗi ngày bạn phải tự nhớ "hôm nay mở file nào", "viết vào đâu", "prompt nào đúng", thì hệ thống chưa tốt.

### 2. Kiến trúc môi trường

Workspace phải có 6 nhóm:

- `docs/`: tài liệu gốc, báo cáo, playbook
- `memory/`: tri thức đã được chốt
- `research/`: giả thuyết, kết quả test, bảng so sánh
- `journals/`: nhật ký giao dịch và nhật ký học
- `reports/`: tổng kết tuần, tổng kết tháng
- `scripts/`: lệnh khởi động và bootstrap

### 3. Luồng one-click từ đầu đến cuối

#### Lúc mới cài máy

Chạy:

```powershell
.\scripts\bootstrap\windows\setup.ps1
```

Script này phải:

- kiểm tra `git`
- kiểm tra `python`
- kiểm tra `uv`
- kiểm tra `node`
- kiểm tra `codex`
- kiểm tra `antigravity`
- tạo cây thư mục
- tạo các file mẫu nếu chưa có
- tạo alias PowerShell cho workflow

#### Lúc bắt đầu ngày học

Chạy:

```powershell
.\scripts\start\qstart.ps1
```

Script này phải:

- in ra bài học hôm nay
- nhắc 4 bước trong 90 phút
- chỉ đường đến file note cần viết
- chỉ đường đến command review

#### Lúc vào bài học cụ thể

Chạy:

```powershell
.\scripts\start\qday.ps1 -Day 8
```

Script này phải:

- mở template note của ngày đó
- nhắc bài tập về nhà
- chỉ file cần đọc
- tạo output file nếu chưa tồn tại

#### Lúc tổng kết tuần

Chạy:

```powershell
.\scripts\start\qreview.ps1 -Week 1
```

Script này phải:

- tạo file report tuần
- tổng hợp bài học
- ép bạn ra quyết định giữ/bỏ

### 4. Memory phải được lưu thế nào

Mỗi file trong `memory/` phải có 6 mục:

1. Giả thuyết
2. Lý do tin
3. Cách kiểm chứng
4. Kết quả hiện tại
5. Quyết định
6. Lệnh gọi lại

Ví dụ:

```md
# XAUUSD Trend Persistence

## Giả thuyết
Vàng có xu hướng duy trì breakout tốt hơn một số cặp FX trong những giai đoạn có động lực và vol hợp lệ.

## Lý do tin
...

## Cách kiểm chứng
...

## Kết quả hiện tại
...

## Quyết định
Tạm giữ để test tiếp.

## Lệnh gọi lại
qday 08
```

---

## Phần VI. Lộ trình 30 ngày

Mỗi ngày có 4 trụ cột:

- `Học`: không học rộng, chỉ học một concept.
- `Làm`: phải động tay vào chart, bot, hay hệ thống.
- `Viết`: để lại dấu vết tri thức.
- `Gọi lệnh`: dùng one-click để giảm ma sát.

### Tuần 1. Xây nền tư duy đúng

#### Ngày 1. Định nghĩa nghề

- Học:
  - Expectancy là gì.
  - Vì sao winrate cao chưa chắc là tốt.
- Làm:
  - Viết lại định nghĩa cá nhân về trading có lợi nhuận.
- Viết:
  - `memory/concepts/edge-definition.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 1`

#### Ngày 2. Cung cầu và động lực

- Học:
  - Thị trường là một auction.
- Làm:
  - Nhìn 10 chart XAUUSD và note những đoạn có động lực rõ.
- Viết:
  - `memory/concepts/auction-logic-xauusd.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 2`

#### Ngày 3. Trend tồn tại vì sao

- Học:
  - Trend persistence.
  - Dòng tiền và vị thế.
- Làm:
  - Giải thích trend cho một người mới trong 15 dòng.
- Viết:
  - `memory/concepts/why-trend-still-works.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 3`

#### Ngày 4. Bot của mình đang làm gì

- Học:
  - Signal, filter, sizing, recovery là 4 tầng khác nhau.
- Làm:
  - Vẽ sơ đồ bot 2.9.8 bằng tay.
- Viết:
  - `memory/bots/bot-298-architecture.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 4`

#### Ngày 5. Tự phản biện bot mình

- Học:
  - Tail risk và risk of ruin.
- Làm:
  - Viết 5 cách bot có thể chết.
- Viết:
  - `memory/bots/bot-298-antithesis.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 5`

#### Ngày 6. Dọn dẹp signal

- Học:
  - Signal nào có logic kinh tế, signal nào chỉ là trigger.
- Làm:
  - Xếp hạng các signal hiện có.
- Viết:
  - `research/signal-scorecard.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 6`

#### Ngày 7. Chốt thesis tuần 1

- Học:
  - Làm ít hơn nhưng chất hơn.
- Làm:
  - Chọn trục nghiên cứu tháng đầu.
- Viết:
  - `reports/week-01-review.md`
- Gọi lệnh:
  - `.\scripts\start\qreview.ps1 -Week 1`

### Tuần 2. Xây engine có thể sống

#### Ngày 8. Đào sâu XAUUSD + Ichimoku breakout

- Học:
  - Breakout và continuation.
- Làm:
  - Chọn 20 lệnh thắng, 20 lệnh thua để đối chiếu.
- Viết:
  - `research/xauusd-ichimoku-hypothesis.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 8`

#### Ngày 9. Viết strategy spec XAUUSD

- Học:
  - Entry không đủ, cần invalidation.
- Làm:
  - Viết rule set đủ rõ để người khác test được.
- Viết:
  - `docs/playbooks/xauusd-trend-engine.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 9`

#### Ngày 10. Dựng regime filter

- Học:
  - Trend day, chop day, news day.
- Làm:
  - Gán mỗi ngày giao dịch mẫu vào một regime.
- Viết:
  - `memory/concepts/regime-map.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 10`

#### Ngày 11. Dựng risk engine

- Học:
  - Risk per trade, per campaign, per day.
- Làm:
  - Đặt hard stop cho tài khoản và cho hệ thống.
- Viết:
  - `docs/playbooks/risk-engine.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 11`

#### Ngày 12. Đặt DCA đúng chỗ

- Học:
  - DCA là overlay, không phải alpha.
- Làm:
  - Thiết kế 3 mode:
    - no DCA
    - capped scale-in
    - limited recovery
- Viết:
  - `docs/playbooks/dca-safety-framework.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 12`

#### Ngày 13. Guard execution

- Học:
  - Spread, slippage, news blackout.
- Làm:
  - Liệt kê 10 trường hợp backtest đẹp nhưng live tệ.
- Viết:
  - `memory/concepts/execution-guard.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 13`

#### Ngày 14. Chốt 2 engine tạm thời

- Học:
  - Ít nhưng rõ hơn.
- Làm:
  - Chốt engine A và B.
- Viết:
  - `reports/week-02-review.md`
- Gọi lệnh:
  - `.\scripts\start\qreview.ps1 -Week 2`

### Tuần 3. Backtest như người nghiên cứu

#### Ngày 15. Protocol

- Học:
  - In-sample, out-of-sample, stress assumptions.
- Làm:
  - Viết protocol test.
- Viết:
  - `research/backtest-protocol.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 15`

#### Ngày 16. Test signal gốc

- Học:
  - Signal phải tự đứng được.
- Làm:
  - Test signal không DCA.
- Viết:
  - `research/signal-alone-test.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 16`

#### Ngày 17. Test filter

- Học:
  - Filter thật sự có tác dụng gì.
- Làm:
  - Bật tắt từng filter.
- Viết:
  - `research/filter-ablation.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 17`

#### Ngày 18. Test sizing

- Học:
  - Size sai có thể giết một edge tốt.
- Làm:
  - So sánh fixed lot, fixed fractional, vol-adjusted.
- Viết:
  - `research/sizing-comparison.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 18`

#### Ngày 19. Stress test

- Học:
  - Thị trường thực tế xấu hơn backtest.
- Làm:
  - Spread x2, slippage x2, session shift.
- Viết:
  - `research/stress-test.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 19`

#### Ngày 20. Parameter stability

- Học:
  - Đừng tìm vùng ổn định, không tìm điểm đẹp.
- Làm:
  - Ghi nhận tham số nhạy cảm.
- Viết:
  - `research/parameter-stability.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 20`

#### Ngày 21. Chốt người ở lại

- Học:
  - Hệ thống nào sống được mới xứng đáng được scale.
- Làm:
  - Chọn hệ thống giữ lại.
- Viết:
  - `reports/week-03-review.md`
- Gọi lệnh:
  - `.\scripts\start\qreview.ps1 -Week 3`

### Tuần 4. Từ trader thành operator

#### Ngày 22. Live ops

- Học:
  - Vận hành quan trọng ngang entry.
- Làm:
  - Viết SOP live.
- Viết:
  - `docs/playbooks/live-ops-sop.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 22`

#### Ngày 23. Research loop

- Học:
  - Nghiên cứu không có nhịp sẽ trở thành tích note vô nghĩa.
- Làm:
  - Đặt lịch mỗi ngày 1 note, mỗi tuần 1 review.
- Viết:
  - `docs/playbooks/research-loop.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 23`

#### Ngày 24. Product hóa

- Học:
  - Tài sản trí tuệ cũng cần đóng gói.
- Làm:
  - Xác định bộ tài liệu, bộ setfile, bộ report.
- Viết:
  - `docs/playbooks/product-engine.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 24`

#### Ngày 25. Affiliate đúng nghĩa

- Học:
  - Ref cũng là nghề dịch vụ.
- Làm:
  - Thiết kế onboarding cho trader mới.
- Viết:
  - `docs/playbooks/affiliate-engine.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 25`

#### Ngày 26. Dạy được cho người khác

- Học:
  - Cái gì dạy được mới là cái hiểu thật.
- Làm:
  - Viết đề cương 3 bài:
    - edge là gì
    - vì sao 95% trader thua
    - DCA cứu hay giết
- Viết:
  - `docs/playbooks/teaching-outline.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 26`

#### Ngày 27. Chuẩn hóa memory

- Học:
  - Tri thức muốn dùng lại được phải có taxonomy.
- Làm:
  - Dọn dẹp và di chuyển file note về đúng chỗ.
- Viết:
  - `docs/playbooks/knowledge-base-map.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 27`

#### Ngày 28. Kiểm tra one-click trên thực tế

- Học:
  - Hệ thống tốt phải khởi động nhanh.
- Làm:
  - Chạy thử setup trên máy sạch hoặc user mới.
- Viết:
  - `reports/bootstrap-test.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 28`

#### Ngày 29. Nhịp 90 phút mỗi ngày

- Học:
  - Bạn không cần cả ngày để tiến bộ.
- Làm:
  - Chốt routine 90 phút:
    - 15 phút review
    - 25 phút nghiên cứu
    - 25 phút test/ghi chép
    - 25 phút tổng kết
- Viết:
  - `docs/playbooks/daily-rhythm.md`
- Gọi lệnh:
  - `.\scripts\start\qday.ps1 -Day 29`

#### Ngày 30. Lệnh cho tháng 2

- Học:
  - Cắt bỏ và chọn lọc là năng lực quan trọng.
- Làm:
  - Chốt:
    - engine nào scale
    - engine nào dừng
    - sản phẩm nào đóng gói
    - kênh nào tiếp tục xây
- Viết:
  - `reports/month-02-order.md`
- Gọi lệnh:
  - `.\scripts\start\qreview.ps1 -Week 4`

---

## Phần VII. Tiêu chuẩn ra quyết định

Một chiến lược được phép sống tiếp chỉ khi đạt đủ 5 cổng:

1. Có logic kinh tế hoặc microstructure tối thiểu.
2. Có kết quả chấp nhận được khi bỏ recovery.
3. Có stress test không gây vỡ toàn bộ thesis.
4. Có tham số tương đối ổn định.
5. Có risk of ruin phù hợp với quy mô vốn thật.

Nếu thiếu 1 trong 5 cổng này, chiến lược chưa được phép gọi là cột sống.

---

## Phần VIII. Tư duy backtest MQL5 cho bot multi-logic

### 1. Không backtest theo kiểu "nạp set và xem lợi nhuận"

Với một bot như 2.9.8, backtest theo kiểu nạp set vào rồi xem đường vốn là cách nhanh nhất để tự lừa mình.

Lý do:

- Bot có nhiều lớp logic.
- Nhiều lớp đang tắt, nhiều lớp đang bật.
- DCA và sniper có thể che mất alpha thật.
- Kết quả đẹp có thể chỉ đến từ việc thị trường lịch sử chưa gặp đúng pha xấu nhất.

Backtest đúng phải trả lời được:

1. Signal này có expectancy riêng không?
2. DCA đang giúp tối ưu hay che đậy?
3. Khoảng cách DCA đang dùng có phù hợp với biến động thật của symbol không?
4. Bộ set có nhạy với digit, spread, session, và broker config không?

### 2. Digit sensitivity là bài toán phải xử lý sớm

Đây là một điểm rất thực chiến. Cùng một tham số `10` nhưng:

- sàn 2 digit
- sàn 3 digit
- sàn 5 digit

có thể cho ra ý nghĩa hoàn toàn khác nhau nếu code đang xử lý theo `point`, `pip`, hay `giá trị giá trực tiếp`.

Vì vậy, khi đọc bất kỳ set nào, phải tự hỏi:

- Biến khoảng cách này đang tính theo `Point`, `Pip`, hay `Price`?
- Broker này quote bao nhiêu digits?
- Symbol này có tick size là bao nhiêu?
- Vàng, forex, crypto, index có chung một quy tắc chuyển đổi không?

Nếu không có lớp chuẩn hóa digit, set rất dễ:

- quá chặt trên sàn này
- quá rộng trên sàn khác
- backtest đẹp nhưng live tệ

### 3. Cách đúng để chọn khoảng DCA

Không chọn khoảng cách DCA bằng cảm giác. Cũng không chọn bằng một con số "nhìn thấy hay".

Thứ tự đúng:

1. Lấy dữ liệu lịch sử của symbol theo khung giờ đang dùng.
2. Đo phân bố biến động:
   - median range
   - ATR
   - adverse excursion
   - khoảng giá giữa các lần swing ngược
3. Chuẩn hóa về cùng một đơn vị:
   - point
   - pip
   - ATR multiple
4. Dùng phân bố này để đề xuất:
   - `distance0`
   - `distance ladder`
   - `hard stop zone`
5. Sau đó mới backtest.

Nói ngắn gọn:

`đọc phổ giá trước, đặt DCA sau`

### 4. DCA phải là hàm của thị trường, không phải hàm của sự hy vọng

Khoảng DCA đúng nên được hình thành từ:

- symbol
- timeframe
- session
- signal mode
- volatility regime

Không nên được hình thành từ:

- cảm giác "lần trước để 10 thấy ổn"
- tâm lý muốn vào dày hơn cho nhanh hồi
- thói quen sao chép set giữa các broker

### 5. Khung nghiên cứu đúng cho bot 2.9.8

#### Lớp 1. Symbol profile

Mỗi symbol cần có 1 hồ sơ:

- digits
- point size
- tick size
- spread median
- ATR median
- session behavior

#### Lớp 2. Signal profile

Mỗi signal cần có 1 hồ sơ:

- tần suất vào lệnh
- adverse excursion trung vị
- favorable excursion trung vị
- ratio giữa rung lắc và xu hướng

#### Lớp 3. DCA profile

Sau khi có 2 lớp trên mới được đề xuất:

- DCA start
- DCA ladder
- max layers
- max lots
- TP recovery

#### Lớp 4. Broker profile

Mỗi broker phải có note riêng:

- digits
- spread giờ cao điểm
- spread giờ tin
- slippage cổ điển
- symbol naming

Không có broker profile thì rất dễ test sai và set sai.

### 6. Công cụ đã thêm vào workspace

Để bắt đầu theo hướng này, workspace đã có:

- `.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set`
- `.\scripts\start\qanalyze-symbol-csv.ps1 -CsvFile .\data\XAUUSD_M15.csv`

Script thứ hai dùng để đọc CSV OHLC và đề xuất range biến động, adverse excursion cơ bản, và ladder DCA gợi ý.

### 7. Bài tập về nhà thực chiến

1. Xuất dữ liệu XAUUSD từ broker thành CSV theo khung giờ bạn trade nhiều nhất.
2. Chạy `qanalyze-symbol-csv.ps1`.
3. Ghi kết quả vào `research/xauusd-price-spectrum.md`.
4. Tạo 3 set:
   - set chặt
   - set vừa
   - set rộng
5. Backtest cùng một signal, cùng một khoảng thời gian, chỉ thay `distance ladder`.

Mục tiêu không phải tìm bộ đẹp nhất. Mục tiêu là tìm vùng ổn định nhất.

---

## Phần IX. Tinh thần làm nghề

Hưng muốn chốt tài liệu này bằng một quan điểm rất rõ:

- Thị trường là nơi mình vào học nghề, không phải nơi mình đến để hơn thua với ai.
- Bạn có thể kiếm tiền từ affiliate, từ bot, từ trading, từ đóng gói tri thức. Nhưng nếu bạn không tôn trọng nghề, sớm muộn hệ thống cũng bị hư.
- Người đi được lâu thường không phải người khỏe nhất. Thường là người biết rút bớt cái tôi, bớt chạy theo số đông, và bớt tự lừa mình.

Nếu bạn học hết 30 ngày này một cách nghiêm túc, mục tiêu tốt nhất không phải là "trở thành thần đồng". Mục tiêu tốt nhất là:

- biết mình đang làm gì
- biết mình đang đứng vào loại edge nào
- biết khi nào phải dừng
- biết cách để lại hệ thống cho mình và cho người khác

Đó mới là nền của một trader có tư cách và có đường đi dài hơn.

---

## Phụ lục. Kiến trúc file để bắt đầu ngày

```text
D:\code\trade
|-- SIEU_BAO_CAO_CHIEN_LUOC_2026_V3_FINAL.md
|-- docs\
|   |-- playbooks\
|-- memory\
|   |-- bots\
|   |-- brokers\
|   |-- concepts\
|-- research\
|-- reports\
|-- journals\
|-- scripts\
|   |-- bootstrap\
|   |   `-- windows\
|   `-- start\
`-- templates\
```

### Lệnh khởi động để nhớ

```powershell
.\scripts\bootstrap\windows\setup.ps1
.\scripts\start\qstart.ps1
.\scripts\start\qday.ps1 -Day 8
.\scripts\start\qreview.ps1 -Week 1
```

### Việc cần làm tiếp theo

1. Đọc file `demo.set` và tách bot thành 4 lớp: signal, filter, sizing, recovery.
2. Chạy script setup để tạo bộ khung học.
3. Dùng `.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set` để lấy tổng quan cấu hình.
4. Xuất CSV giá và dùng `.\scripts\start\qanalyze-symbol-csv.ps1 -CsvFile <duong_dan_csv>`.
5. Bắt đầu từ Ngày 1, không nhảy cóc.
