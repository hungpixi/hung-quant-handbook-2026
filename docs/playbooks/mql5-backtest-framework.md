# MQL5 Backtest Framework Cho Bot Multi-Logic

## Muc tieu

Khung nay dung de nghien cuu cac EA kieu:

- nhieu signal
- nhieu filter
- co DCA
- co sniper, hedging, recovery

Nhiem vu cua khung nay la tach:

- alpha that
- bo loc thuc su co gia tri
- sizing / DCA / recovery

## Nguyen tac cot loi

1. Khong toi uu toan bo set cung luc.
2. Khong dung duong von dep lam bang chung dau tien.
3. Khong giu tham so khong giai thich duoc.
4. Moi bien so duoc doi phai co ly do nghien cuu ro rang.

## Thu tu test de xuat

### Buoc 1. Chuan hoa moi truong

- Broker nao
- Symbol nao
- Digits bao nhieu
- Tick size bao nhieu
- Spread trung binh va spread xau
- Khung gio nao

### Buoc 2. Xac minh signal

- Tat DCA
- Tat sniper
- Tat hedging
- Tat trailing

Chi giu:

- signal
- stop / take profit toi thieu neu can

Neu buoc nay khong co gia tri, can rat than trong.

### Buoc 3. Them filter

Bat tung lop:

- trading time
- EMA filter
- MACD filter
- zone cycle

Muc tieu:

- giam DD
- khong lam sap expectancy

### Buoc 4. Them sizing / DCA

Sau khi signal co can cu, moi test:

- multiplier
- distance ladder
- TPDCA
- max lots

### Buoc 5. Them recovery nang cao

Sau cung moi test:

- sniper
- hedging
- open opposite
- balance lot

## KPI bat buoc

- Net profit
- Profit factor
- Max drawdown
- Recovery factor
- Longest adverse run
- Max concurrent orders
- Time in drawdown

## Quy tac ra quyet dinh

- Neu signal only am sau, dung xem recovery la bang chung he thong manh.
- Neu filter giup DD giam nhieu ma profit giam it, giu filter.
- Neu tham so chi dep trong mot diem hep, khong dung.
- Neu ket qua doi khac manh giua broker 2-digit va 3-digit, chua duoc phep live rong.

