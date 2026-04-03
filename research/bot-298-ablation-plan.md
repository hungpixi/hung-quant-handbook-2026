# Bot 2.9.8 Ablation Plan

## Muc tieu

Tra loi 3 cau hoi:

1. Alpha nam o signal hay nam o recovery?
2. DCA giup toi uu hay chi tri hoan thua lo?
3. Bo filter nao neu bat len se giam drawdown ma khong giet expectancy?

## Chuoi test toi thieu

### Test A. Signal only

- `InpUseDCA=false`
- `InpUseSniper=false`

Neu test nay am sau va on dinh am, can rat than trong.

### Test B. Signal + DCA

- `InpUseDCA=true`
- `InpUseSniper=false`

Muc dich:

- xem DCA them gia tri hay chi them drawdown.

### Test C. Signal + DCA + Sniper

- `InpUseDCA=true`
- `InpUseSniper=true`

Muc dich:

- xem sniper la alpha hay chi la equity smoother.

### Test D. Them filter

Lan luot bat:

- `InpUseTradingTime=true`
- `InpUseEMAFilter=true`
- `InpUseMACDFilter=true`

Khong bat cung luc ngay tu dau.

## KPI bat buoc

- Net profit
- Profit factor
- Max drawdown
- Longest losing run
- Average adverse excursion
- Time to recovery

## Quyet dinh

- Neu Test A van chap nhan duoc, bot co nen.
- Neu chi Test C dep, bot dang phu thuoc recovery.
- Neu bat them filter ma PF tang va DD giam, nen xay bo filter truoc khi toi uu multiplier.

