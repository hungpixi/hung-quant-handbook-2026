# Hưng Quant Handbook 2026

Bộ tài liệu này là một hệ `handbook + workbook` dành cho người đang học trading có hệ thống, nghiên cứu bot MQL5, và muốn biến việc học thành một workflow có thể lặp lại, dùng lại, và chia sẻ lại.

## Thành phần chính

- `docs/HUNG_QUANT_HANDBOOK_2026.md`: bản sách chính.
- `docs/HUNG_QUANT_HANDBOOK_2026.pdf`: bản PDF để đọc và chia sẻ.
- `docs/HUNG_QUANT_WORKSHEETS_2026.md`: bộ worksheet riêng để làm bài tập.
- `docs/HUNG_QUANT_WORKSHEETS_2026.pdf`: bản PDF worksheet để in hoặc giao bài.
- `SIEU_BAO_CAO_CHIEN_LUOC_2026_V3_FINAL.md`: báo cáo chiến lược nền.
- `scripts/bootstrap/windows/setup.ps1`: bootstrap workspace.
- `scripts/start/*.ps1`: các lệnh workflow hằng ngày.

## Cách dùng nhanh

```powershell
.\scripts\bootstrap\windows\setup.ps1
.\scripts\start\qstart.ps1
.\scripts\start\qday.ps1 -Day 1
```

## Build lại PDF

```powershell
python .\scripts\build_handbook_pdf.py
python .\scripts\build_worksheets_pdf.py
```

## Khi đưa lên GitHub

- Đặt repo public nếu muốn chia sẻ rộng.
- Pin hai file PDF ở phần Releases hoặc README.
- Không đưa thông tin nhạy cảm, auth, hay dữ liệu tài khoản broker vào repo.
- Nếu cần, có thể thêm screenshot bìa PDF vào README để repo nhìn chuyên nghiệp hơn.

