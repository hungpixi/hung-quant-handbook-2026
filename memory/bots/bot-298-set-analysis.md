# Bot 2.9.8 Set Analysis

## Tong quan nhanh

- File: `demo.set`
- So tham so doc duoc: `199`
- So nhom chuc nang: `28`
- Bot nay la mot `multi-module execution framework`, khong phai bot mot signal don.
- Cau hinh hien tai cho thay trong tam dang nghieng ve `DCA + sniper/recovery`, khong nghieng ve he filter/hedging phuc tap.

## Nhung module dang bat thuc chat

### Dang bat truc tiep

- `InpUseDCA=true`
- `InpUseSniper=true`

### Bat nhung bi khoa boi module me

- `InpUseLotsDCA2Hedging=true` nhung `InpUseHedging=false`
- `InpStopSniperWhenHedging=true` nhung `InpUseHedging=false`
- `InpStageMagicFilter=true` nhung `InpUseStageTarget=false`
- `InpUseTime1..4=true` nhung `InpUseTradingTime=false`

### Mang tinh hien thi, khong tao alpha

- `InpUTBOT_ShowArrows=true`

## Ket luan quan trong

Neu nhin theo runtime logic, bo set nay dang co 2 module that su chi phoi hanh vi:

1. `Signal engine` duoc quyet dinh chu yeu boi `InpIndiMode`, `InpTFSignal`, va tham so cua indicator duoc mode do su dung.
2. `Recovery engine` duoc quyet dinh chu yeu boi `DCA + Sniper`.

Phan lon cac lop bao ve nang cao hien dang `tat`:

- EMA filter = tat
- MACD filter = tat
- Zone cycle = tat
- Trading time global = tat
- Hedging = tat
- Hedging zone = tat
- Balance lot = tat
- Trailing = tat
- Stage target = tat
- Lottery = tat
- Open opposite = tat

Noi cach khac, bo set nay hien tai khong phai mot he "da filter chat". No gan voi mot he:

`signal mo lenh rong + DCA theo cap so + sniper de tia khoi chuoi`

## 4 lop logic can tach

## 1. Signal layer

Phan nay quyet dinh bot vao lenh vi ly do gi.

Tham so neo:

- `InpIndiMode=0`
- `InpTFSignal=0`
- cum tham so CCI, Stoch, Momentum, Supertrend, UTBOT, RSI, Ichimoku, BB, Pinbar

Luu y:

- Chua co mapping source code nen `InpIndiMode=0` chua du de khang dinh dang chay indicator nao.
- Can EX5 source hoac tai lieu mode map de biet mode `0` tro den nhom logic nao.

## 2. Filter layer

Phan nay hien rat mong trong bo set hien tai.

Tat ca deu dang tat:

- `InpUseEMAFilter=false`
- `InpUseMACDFilter=false`
- `InpUseZoneCycle=false`
- `InpUseTradingTime=false`

He qua:

- Bot dang mo rong vung hoat dong.
- Loi the backtest co the den tu so lan co hoi nhieu, nhung doi lai la nhay cam hon voi regime xau.

## 3. Sizing layer

Tham so dang chu y:

- `InpLots=0.01`
- `InpMaxLots=2.3`
- `InpMultiplier=1.3`
- `InpUseChangeMultiplier=false`
- `InpPlus=0.01`

Doc nhanh:

- `Multiplier 1.3` la kha manh neu chuoi lenh dai.
- `MaxLots=2.3` la gioi han can, nhung phai dat trong boi canh `distance`, `sniper`, va so lenh toi da.
- `InpMaxBuyOrders=100`, `InpMaxSellOrders=100` la tran ly thuyet rat rong, khong nen xem la tran van hanh an toan.

## 4. Recovery layer

Day la trai tim cua bo set nay.

Tham so cot song:

- `InpUseDCA=true`
- `InpDCAMODE=0`
- `InpMultiplier=1.3`
- `InpDistance0=10`
- `InpDistance1..4=15`
- `InpTPDCA=20`
- `InpUseSniper=true`
- `InpOrders2StartSniper=20`
- `InpPercentSniper=10`
- `InpTPSniper=5`
- `InpMuliSniper=1.15`

Doc nhanh:

- Chuoi mo lenh co xu huong vao day hon khi gia di nguoc.
- Khoang cach DCA khong qua lon.
- Sniper bat tu kha muon, quanh vung `15-20 lenh`, nghia la he thong chap nhan vao kha sau trong drawdown truoc khi "tia".

## Nhan dinh chuyen mon

Bo set nay co phong cach rat ro:

- Uu tien cho he thong duoc "song" qua cac dot di nguoc.
- Chap nhan drawdown sau hon de doi mean reversion hoac cho chuoi hoi lai.
- Dung sniper de rut bot can nang chuoi, nhung sniper khong thay the duoc mot signal goc co expectancy.

Neu thi truong co nhung nhat rung lac lien tuc nhung cuoi cung hoi lai, bo set nay co the trong rat dep.
Neu thi truong gap mot phase trend mot chieu dai va moc thanh khoan lien tuc, bo set nay co nguy co gom lenh xau rat sau.

## Gia thuyet lam viec cho XAUUSD

Gia thuyet hop ly nhat hien tai:

- XAUUSD co kha nang tao breakout va continuation ro hon nhieu cap FX trong mot so phase.
- Neu signal mode `0` dang bat dung huong trend va DCA duoc nhe tay, equity curve se dep.
- Neu alpha that den tu trend continuation, thi khi bo DCA, he thong van phai con lai mot phan expectancy.
- Neu bo DCA la sap hoan toan, nghia la alpha dang nam trong recovery, khong nam trong signal.

## Thu tu backtest de dung

Khong duoc backtest ca bot nhu mot khoi den ngay lap tuc.

Thu tu de xuat:

1. Xac dinh `InpIndiMode=0` la logic gi.
2. Test signal goc voi `InpUseDCA=false`, `InpUseSniper=false`.
3. Test signal + DCA, chua co sniper.
4. Test signal + DCA + sniper.
5. Bat tung lop filter de xem cai nao that su giup.
6. Test spread x2, slippage x2, va thu nho session.
7. Kiem tra parameter stability cua `multiplier`, `distance`, `TPDCA`.

## Bien uu tien can test dau tien

### Nhom 1: Xac minh alpha

- `InpUseDCA`
- `InpUseSniper`
- `InpIndiMode`
- `InpTFSignal`

### Nhom 2: Giam tail risk

- `InpMultiplier`
- `InpDistance0`
- `InpDistance1`
- `InpTPDCA`
- `InpMaxLots`

### Nhom 3: Co the them sau

- `InpUseEMAFilter`
- `InpUseMACDFilter`
- `InpUseTradingTime`
- `InpUseHedging`

## Quyet dinh tam thoi

- Khong coi bo set nay la "hop moi moi truong".
- Xem no la mot ung vien nghien cuu cho `XAUUSD trend/continuation + recovery overlay`.
- Uu tien chung minh `signal expectancy` truoc khi toi uu recovery.
- Bo filter hien tai qua mong; neu muon song lau hon, nen uu tien bo sung `regime/session filter` som hon la them mode cuu lenh.

## Lenh goi lai

```powershell
.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set
```

