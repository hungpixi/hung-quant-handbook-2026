# Hưng Quant Handbook 2026

Bộ tài liệu này là một hệ `handbook + workbook` dành cho người đang học trading có hệ thống, nghiên cứu bot MQL5, và muốn biến việc học thành một workflow có thể lặp lại, dùng lại, và chia sẻ lại.

## 1. Vấn đề gì?
Phần lớn retail trader hiện nay gặp khó khăn vì làm sai trình tự học nghề: ưu tiên tìm tín hiệu thay vì xây dựng tư duy kiểm soát rủi ro, backtest sai kỹ thuật và sai môi trường, và bị nhiễu do "chỉnh sửa tham số theo cảm giác" mà không có cơ sở phân tích tĩnh (base theory).

## 2. Giải pháp này hơn cái cũ ở đâu?
Cuốn handbook này không phải lý thuyết suông hay bán tín hiệu. Nó định hình một **hệ sinh thái workflow**:
- **Tư duy Cốt lõi**: Simple systematic trend + Strong risk controls + Disciplined research loop.
- **Workflow tích hợp**: Dùng CLI operations (`qstart`, `qday`, `qanalyze-set`) nhằm ép người dùng vào kỷ luật test và ghi log minh bạch từng phiên làm việc.
- **Hệ thống Design Data-Driven**: Đề xuất khoảng DCA thông qua dữ liệu đọc phổ giá (OHLC CSV/Tick) thay vì cảm tính thị giác.

## 3. Trade-off là gì?
- Cần sự kiên nhẫn: Yêu cầu ít nhất 30 ngày tập trung thực thi theo worksheet & checklist thay vì mì ăn liền.
- Bạn phải làm việc với terminal (CLI) và log text liên tục, không hợp với những ai chỉ thích click chuột UI bóng bẩy.

## 4. Hướng nâng cấp tiếp theo là gì?
- **Excursion Research Engine**: Công cụ tự động đo adverse excursion sau mock entry để xuất parameter DCA (distance, max_layers, multiplier) lý tưởng.
- **Multi-Symbol Coverage**: Update phổ giá và thông số chuẩn (spread/tick size baseline) cho các cặp FX major ngoài XAUUSD.
- **Headless Backtest Automation**: Tích hợp pipeline để gửi parameters vào MetaTester MT5 qua command-line.

---

## Tác giả & Bản Quyền
- Tác giả: Hưng (hungpixi)
- Branding: [https://comarai.com](https://comarai.com)
- Định vị: Comarai - Companion for Marketing & AI Automation

> "Người đi được lâu trong thị trường thường không phải người nói mạnh nhất... thường là người biết mình đang học cái gì, đang test cái gì, đang sống nhờ edge nào."
