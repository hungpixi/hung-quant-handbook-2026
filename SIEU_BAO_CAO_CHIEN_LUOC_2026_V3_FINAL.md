# BAO CAO CHIEN LUOC 2026 CUA HUNG

> Tai lieu goc duoc viet lai ngay 03/04/2026.
> 
> Ban nay khong dung lai van phong content gay soc. Noi dung duoc sap xep lai theo huong kinh nghiep, ton trong thi truong, ton trong nguoi hoc, va uu tien kha nang van hanh that.

---

## Loi mo dau

Tai lieu nay duoc viet lai tu mot nguon cam hung cua mot nguoi chi lam content. Phan anh huong ve goc nhin van con, nhung gioi thieu, cach lap luan, va cach hanh dong da duoc chuyen thanh giong cua Hung: di thang vao van de, giu long ton trong thi truong, va xem trading la mot nghe can hoc bai ban.

Neu mot tai lieu chi lam nguoi doc thay hung phan, tai lieu do chua du. Neu mot tai lieu chi dua ra du bao ma khong day cach tu kiem chung, tai lieu do cung chua du. Ban nay co 3 muc tieu:

1. Day nguoi moi hieu ban chat viec giao dich co loi nhuan.
2. Xay mot lo trinh 30 ngay de di tu hoc lan man sang hoc co he thong.
3. Dung mot bo moi truong one-click de qua trinh hoc, nghien cuu, viet note, backtest, va van hanh khong bi dut quang.

Trading la mot nghe can su ton nghiem. Thi truong khong no ai ca, nhung cung khong doi xu te voi nguoi biet hoc va biet giu minh.

---

## Phan I. Ban chat nghe trading

### 1. Vi sao da so trader khong co loi nhuan

Da so trader thua khong phai vi kem thong minh. Ho thua vi lam sai thu tu:

- Tim entry truoc khi hieu edge.
- Tim indicator truoc khi hieu thi truong dang co regime gi.
- Tim cach nhan doi tai khoan truoc khi hoc cach song sot.
- Dung DCA de keo dai thoi gian den luc gap mot nhat cat duoc toan bo loi nhuan.
- Nhieu nguoi nham drawdown tam thoi voi kha nang song sot dai han.

Neu phai gom gon trong mot cong thuc, trading co loi nhuan ben vung la:

`Expectancy x Position Sizing x Regime Fit x Execution Quality x Survival`

Trong do:

- `Expectancy`: ve dai han, moi lenh co gia tri ky vong duong.
- `Position Sizing`: danh dung kich thuoc de khi sai van con song.
- `Regime Fit`: dung chien luoc dung luc.
- `Execution Quality`: spread, slippage, session, tin tuc khong pha nat he thong.
- `Survival`: song du lau de edge duoc bieu lo.

### 2. Hai thu Hung xem la loi cua nghe

- `Long tham`: nguoi trong thi truong luon chay theo ky vong loi nhuan, FOMO, va ham muon gia di tiep.
- `Thang du`: mot cap giao dich hay mot thi truong chi co the cho xu huong ben khi dong tien, nhu cau, hoac ap luc dinh gia thuc su con du dia de di them.

Noi ngan gon:

- Khong co dong co tiep dien, trend yeu.
- Khong co thang du, gia de tro lai can bang.
- Khong co ky luat, trader se tu huy edge cua chinh minh.

### 3. Dieu trader moi can hieu som

- Thi truong khong thuong su tu tin vo can cu.
- Mot robot co winrate cao khong co nghia la mot he thong manh.
- Mot backtest dep chua chac la mot bo may co the live.
- DCA co the la cong cu quan tri vi the co dieu kien, nhung neu no la ly do duy nhat equity curve dep thi do la tin hieu canh bao.

### Bai tap ve nha 01

Viet file note dau tien voi ten `memory/concepts/edge-definition.md` tra loi 5 cau:

1. Toi dang co the kiem tien tu dau?
2. Toi dang co the mat tien vi dau?
3. Neu bo DCA thi he thong con gi?
4. Thi truong nao hop voi toi nhat hien tai?
5. Toi muon hoc de song sot, hay hoc de thang nhanh?

---

## Phan II. Huong di tot nhat trong trading nam 2026

### 1. Khong can danh bai moi bot AI

Thi truong thay doi vi AI va bot manh hon la that. Thanh khoan bi quet nhanh hon, breakout gia xuat hien nhieu hon, va nhung vung sideway ngắn han kho nhai hon. Nhung dieu do khong xoa bo toan bo edge cua retail.

Thu retail van con co the lam tot:

- Chon thi truong va khung gio dung.
- Dung he trend-following va continuation.
- Them regime filter de tranh chop.
- Giam tan suat, tang chat luong lenh.
- Lay risk engine lam cot song.

### 2. Nhung ho chien luoc dang con gia tri

#### Trend-following

Day la ho chien luoc dang de nghien cuu nhat cho retail.

- De giai thich.
- De backtest hon so voi signal huy hoc.
- Co tinh ben tren nhieu thi truong.
- Phu hop voi XAUUSD va mot so cap forex thanh khoan cao.

#### Breakout / Continuation

Phu hop khi:

- thi truong co dong luc thuc su
- co nhip nen truoc do
- thanh khoan du day
- session va vol ung ho

#### Regime-aware systems

Khong hoi "signal nao ngon nhat", ma hoi:

- Hom nay la trend day hay chop day?
- Session nay co thich hop de bat breakout khong?
- Luc nao phai giam size?
- Luc nao phai tat may?

#### Volatility-aware sizing

Khong phai lenh nao cung dat cung mot lot. Thi truong bien dong khac nhau can size khac nhau.

### 3. Nhung huong khong nen lay lam cot song thang dau

- Indicator soup.
- Chieu tro chon le, me tin pattern, vao lenh vi thay "co ve dung".
- SMC neu chua viet thanh rule co the test duoc.
- Martingale vo han.
- Toi uu tham so chi de dep duong von qua khu.

### Bai tap ve nha 02

Viet file `memory/concepts/why-trend-still-works.md` tra loi:

- Vi sao trend van ton tai du AI manh hon?
- Dieu gi lam trend fail?
- Toi se nhan dien chop bang cach nao?
- Toi co chap nhan bo qua nhieu lenh de doi lenh dep hon khong?

---

## Phan III. Bot 2.9.8 va bai toan "nhieu signal, hon 200 input"

### 1. Nhin dung van de

Mot bot co 4 nhom logic va hon 200 input khong mac dinh la xau. Nhung no chi tot khi moi input thuoc mot vai ro ro rang.

Neu khong, no se tao ra 3 ao giac:

- `Ao giac bao phu`: tuong nhu danh duoc moi moi truong.
- `Ao giac tinh chinh`: tuong nhu chi can vặn tham so la ra loi.
- `Ao giac an toan`: tuong nhu DCA la lam giam rui ro.

### 2. Cac nhom input can tach ra

Khi co file `.set`, phan tich can tach thanh 4 tang:

- `Signal`: vao lenh vi ly do gi?
- `Filter`: moi truong nao moi duoc vao?
- `Sizing`: vao bao nhieu?
- `Recovery`: sai thi xu ly ra sao?

### 3. Cac cau hoi phai tra loi

- Neu chi giu signal ma bo DCA, bot con co expectancy duong khong?
- Neu bo mot nhom filter, equity curve xau len bao nhieu?
- Neu doi tu XAUUSD sang EURUSD hay GBPUSD, logic con giu duoc khong?
- Neu gap giai doan sideway dai, bot song duoc khong?

### 4. Nhan dinh tam thoi ve truong hop XAUUSD + Ichimoku breakout

Truong hop ban neu ra rat dang dao sau. Gia thuyet lam viec tot nhat hien tai la:

- Ichimoku breakout co the khong phai alpha duy nhat.
- Alpha that co the den tu trend persistence va continuation cua vang.
- DCA dang co the dong vai tro lam mem duong von nhieu hon la tao edge.
- Vang co nhung phase co narrative va dong tien ro hon nen breakout de "song" hon nhieu cap khac.

Khong nen ket luan som la "Ichimoku than ky". Viec dung can lam la `ablation test`.

### 5. Framework backtest dung cho bot 2.9.8

Khong co cach backtest nao hop cho moi moi truong. Co `framework backtest` hop cho nhieu loai moi truong:

1. Test signal goc, khong DCA.
2. Test signal goc + filter.
3. Test signal goc + filter + sizing.
4. Test them recovery nhu mot lop bo sung.
5. Chay stress test spread/slippage/session/news.
6. Chay out-of-sample.
7. Chay parameter stability, khong tim diem dep nhat.

Neu buoc 1-3 khong co edge ma buoc 4 moi dep, thi he thong dang ban tail risk.

### Bai tap ve nha 03

Khi bo file `.set` vao workspace, tao bang:

| Input | Nhom | Gia thuyet tac dung | Muc do quan trong | Co the bo? |
| --- | --- | --- | --- | --- |

Muc tieu cua bai tap nay la ep hon 200 input xuong:

- 10-15 input cot song
- 20-30 input phu
- phan con lai dua vao nhom "chua chung minh duoc gia tri"

---

## Phan IV. Bon co may kiem tien

### 1. Co may 1: Trader Engine

Day la he thong ra tien truc tiep tu trading.

Muc tieu:

- 1 engine chu luc cho XAUUSD
- 1 engine phu cho mot ro FX nho
- MQL5 de live
- co risk engine ro rang

Output bat buoc:

- strategy spec
- setfile chinh
- dashboard ket qua
- nhat ky theo ngay

### 2. Co may 2: Research Engine

Day la bo may giup ban khong dung yen o mot phien ban bot.

Muc tieu:

- moi ngay 1 note gia thuyet
- moi tuan 1 report
- moi thang 1 danh sach giu/bo

Khong co research engine, trader engine se dan tro nen me tin va bi thi truong "lay lai hoc phi".

### 3. Co may 3: Product Engine

Day la cach dong goi nhung thu ban da xay:

- bo setfile
- bo playbook
- bo bao cao
- bo giao trinh cho nguoi hoc

Neu lam dung, day la cau noi giua trading thuc chien va viec mo rong thu nhap.

### 4. Co may 4: Distribution Engine

Day la affiliate, referral, content, case study, va onboarding.

Hung de xuat xem day la mot nghe phu hop neu ban giu dung tinh than:

- khong lua nguoi moi vao overtrade
- khong ban giac mo giau nhanh
- khong dung ref nhu KPI duy nhat
- lay `trader survival` lam KPI hang dau

Ref broker nhu Exness, XM, hoac cac san khac co the la mot "chanh nghiep" neu vai tro cua ban la:

- giup trader vao dung loai tai khoan
- giup ho hieu risk
- giup ho co quy trinh giao dich ro rang
- giup ho song sot lau hon trong thi truong

### Bai tap ve nha 04

Viet file `memory/brokers/affiliate-manifesto.md` tra loi:

- Toi dang giup trader dieu gi?
- Toi tu choi lam nhung dieu gi?
- Trader nao phu hop vao he thong cua toi?
- KPI thanh cong cua toi co nhung gi ngoai volume?

---

## Phan V. One-click setup xuyen suot qua trinh hoc

### 1. Muc tieu cua one-click

One-click khong chi de cai may. One-click phai giup:

- vao bai hoc hom nay ngay lap tuc
- mo dung note can viet
- nho minh dang hoc den dau
- tao report dung mau
- giam ma sat trong viec hoc va nghien cuu

Neu moi ngay ban phai tu nho "hom nay mo file nao", "viet vao dau", "prompt nao dung", thi he thong chua tot.

### 2. Kien truc moi truong

Workspace phai co 6 nhom:

- `docs/`: tai lieu goc, bao cao, playbook
- `memory/`: tri thuc da duoc chot
- `research/`: gia thuyet, ket qua test, bang so sanh
- `journals/`: nhat ky giao dich va nhat ky hoc
- `reports/`: tong ket tuan, tong ket thang
- `scripts/`: lenh khoi dong va bootstrap

### 3. Luong one-click tu dau den cuoi

#### Luc moi cai may

Chay:

```powershell
.\scripts\bootstrap\windows\setup.ps1
```

Script nay phai:

- kiem tra `git`
- kiem tra `python`
- kiem tra `uv`
- kiem tra `node`
- kiem tra `codex`
- kiem tra `antigravity`
- tao cay thu muc
- tao cac file mau neu chua co
- tao alias PowerShell cho workflow

#### Luc bat dau ngay hoc

Chay:

```powershell
.\scripts\start\qstart.ps1
```

Script nay phai:

- in ra bai hoc hom nay
- nhac 4 buoc trong 90 phut
- chi duong den file note can viet
- chi duong den command review

#### Luc vao bai hoc cu the

Chay:

```powershell
.\scripts\start\qday.ps1 -Day 8
```

Script nay phai:

- mo template note cua ngay do
- nhac bai tap ve nha
- chi file can doc
- tao output file neu chua ton tai

#### Luc tong ket tuan

Chay:

```powershell
.\scripts\start\qreview.ps1 -Week 1
```

Script nay phai:

- tao file report tuan
- tong hop bai hoc
- ep ban ra quyet dinh giu/bo

### 4. Memory phai duoc luu the nao

Moi file trong `memory/` phai co 6 muc:

1. Gia thuyet
2. Ly do tin
3. Cach kiem chung
4. Ket qua hien tai
5. Quyet dinh
6. Lenh goi lai

Vi du:

```md
# XAUUSD Trend Persistence

## Gia thuyet
Vang co xu huong duy tri breakout tot hon mot so cap FX trong nhung giai doan co dong luc va vol hop le.

## Ly do tin
...

## Cach kiem chung
...

## Ket qua hien tai
...

## Quyet dinh
Tam giu de test tiep.

## Lenh goi lai
qday 08
```

---

## Phan VI. Lo trinh 30 ngay

Moi ngay co 4 tru cot:

- `Hoc`: khong hoc rong, chi hoc mot concept.
- `Lam`: phai dong tay vao chart, bot, hay he thong.
- `Viet`: de lai dau vet tri thuc.
- `Goi lenh`: dung one-click de giam ma sat.

### Tuan 1. Xay nen tu duy dung

#### Ngay 1. Dinh nghia nghe

- Hoc:
  - Expectancy la gi.
  - Vi sao winrate cao chua chac la tot.
- Lam:
  - Viet lai dinh nghia ca nhan ve trading co loi nhuan.
- Viet:
  - `memory/concepts/edge-definition.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 1`

#### Ngay 2. Cung cau va dong luc

- Hoc:
  - Thi truong la mot auction.
- Lam:
  - Nhin 10 chart XAUUSD va note nhung doan co dong luc ro.
- Viet:
  - `memory/concepts/auction-logic-xauusd.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 2`

#### Ngay 3. Trend ton tai vi sao

- Hoc:
  - Trend persistence.
  - Dong tien va vi the.
- Lam:
  - Giai thich trend cho mot nguoi moi trong 15 dong.
- Viet:
  - `memory/concepts/why-trend-still-works.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 3`

#### Ngay 4. Bot cua minh dang lam gi

- Hoc:
  - Signal, filter, sizing, recovery la 4 tang khac nhau.
- Lam:
  - Ve so do bot 2.9.8 bang tay.
- Viet:
  - `memory/bots/bot-298-architecture.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 4`

#### Ngay 5. Tu phan bien bot minh

- Hoc:
  - Tail risk va risk of ruin.
- Lam:
  - Viet 5 cach bot co the chet.
- Viet:
  - `memory/bots/bot-298-antithesis.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 5`

#### Ngay 6. Don dep signal

- Hoc:
  - Signal nao co logic kinh te, signal nao chi la trigger.
- Lam:
  - Xep hang cac signal hien co.
- Viet:
  - `research/signal-scorecard.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 6`

#### Ngay 7. Chot thesis tuan 1

- Hoc:
  - Lam it hon nhung chat hon.
- Lam:
  - Chon truc nghien cuu thang dau.
- Viet:
  - `reports/week-01-review.md`
- Goi lenh:
  - `.\scripts\start\qreview.ps1 -Week 1`

### Tuan 2. Xay engine co the song

#### Ngay 8. Dao sau XAUUSD + Ichimoku breakout

- Hoc:
  - Breakout va continuation.
- Lam:
  - Chon 20 lenh thang, 20 lenh thua de doi chieu.
- Viet:
  - `research/xauusd-ichimoku-hypothesis.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 8`

#### Ngay 9. Viet strategy spec XAUUSD

- Hoc:
  - Entry khong du, can invalidation.
- Lam:
  - Viet rule set du ro de nguoi khac test duoc.
- Viet:
  - `docs/playbooks/xauusd-trend-engine.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 9`

#### Ngay 10. Dung regime filter

- Hoc:
  - Trend day, chop day, news day.
- Lam:
  - Gan moi ngay giao dich mau vao mot regime.
- Viet:
  - `memory/concepts/regime-map.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 10`

#### Ngay 11. Dung risk engine

- Hoc:
  - Risk per trade, per campaign, per day.
- Lam:
  - Dat hard stop cho tai khoan va cho he thong.
- Viet:
  - `docs/playbooks/risk-engine.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 11`

#### Ngay 12. Dat DCA dung cho

- Hoc:
  - DCA la overlay, khong phai alpha.
- Lam:
  - Thiet ke 3 mode:
    - no DCA
    - capped scale-in
    - limited recovery
- Viet:
  - `docs/playbooks/dca-safety-framework.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 12`

#### Ngay 13. Guard execution

- Hoc:
  - Spread, slippage, news blackout.
- Lam:
  - Liet ke 10 truong hop backtest dep nhung live te.
- Viet:
  - `memory/concepts/execution-guard.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 13`

#### Ngay 14. Chot 2 engine tam thoi

- Hoc:
  - It nhung ro hon.
- Lam:
  - Chot engine A va B.
- Viet:
  - `reports/week-02-review.md`
- Goi lenh:
  - `.\scripts\start\qreview.ps1 -Week 2`

### Tuan 3. Backtest nhu nguoi nghien cuu

#### Ngay 15. Protocol

- Hoc:
  - In-sample, out-of-sample, stress assumptions.
- Lam:
  - Viet protocol test.
- Viet:
  - `research/backtest-protocol.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 15`

#### Ngay 16. Test signal goc

- Hoc:
  - Signal phai tu dung duoc.
- Lam:
  - Test signal khong DCA.
- Viet:
  - `research/signal-alone-test.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 16`

#### Ngay 17. Test filter

- Hoc:
  - Filter that su co tac dung gi.
- Lam:
  - Bat tat tung filter.
- Viet:
  - `research/filter-ablation.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 17`

#### Ngay 18. Test sizing

- Hoc:
  - Size sai co the giet mot edge tot.
- Lam:
  - So sanh fixed lot, fixed fractional, vol-adjusted.
- Viet:
  - `research/sizing-comparison.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 18`

#### Ngay 19. Stress test

- Hoc:
  - Thi truong thuc te xau hon backtest.
- Lam:
  - Spread x2, slippage x2, session shift.
- Viet:
  - `research/stress-test.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 19`

#### Ngay 20. Parameter stability

- Hoc:
  - Dung tim vung on dinh, khong tim diem dep.
- Lam:
  - Ghi nhan tham so nhay cam.
- Viet:
  - `research/parameter-stability.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 20`

#### Ngay 21. Chot nguoi o lai

- Hoc:
  - He thong nao song duoc moi xung dang duoc scale.
- Lam:
  - Chon he thong giu lai.
- Viet:
  - `reports/week-03-review.md`
- Goi lenh:
  - `.\scripts\start\qreview.ps1 -Week 3`

### Tuan 4. Tu trader thanh operator

#### Ngay 22. Live ops

- Hoc:
  - Van hanh quan trong ngang entry.
- Lam:
  - Viet SOP live.
- Viet:
  - `docs/playbooks/live-ops-sop.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 22`

#### Ngay 23. Research loop

- Hoc:
  - Nghien cuu khong co nhip se tro thanh tich note vo nghia.
- Lam:
  - Dat lich moi ngay 1 note, moi tuan 1 review.
- Viet:
  - `docs/playbooks/research-loop.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 23`

#### Ngay 24. Product hoa

- Hoc:
  - Tai san tri tue cung can dong goi.
- Lam:
  - Xac dinh bo tai lieu, bo setfile, bo report.
- Viet:
  - `docs/playbooks/product-engine.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 24`

#### Ngay 25. Affiliate dung nghia

- Hoc:
  - Ref cung la nghe dich vu.
- Lam:
  - Thiet ke onboarding cho trader moi.
- Viet:
  - `docs/playbooks/affiliate-engine.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 25`

#### Ngay 26. Day duoc cho nguoi khac

- Hoc:
  - Cai gi day duoc moi la cai hieu that.
- Lam:
  - Viet de cuong 3 bai:
    - edge la gi
    - vi sao 95% trader thua
    - DCA cuu hay giet
- Viet:
  - `docs/playbooks/teaching-outline.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 26`

#### Ngay 27. Chuan hoa memory

- Hoc:
  - Tri thuc muon dung lai duoc phai co taxonomy.
- Lam:
  - Don dep va di chuyen file note ve dung cho.
- Viet:
  - `docs/playbooks/knowledge-base-map.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 27`

#### Ngay 28. Kiem tra one-click tren thuc te

- Hoc:
  - He thong tot phai khoi dong nhanh.
- Lam:
  - Chay thu setup tren may sach hoac user moi.
- Viet:
  - `reports/bootstrap-test.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 28`

#### Ngay 29. Nhip 90 phut moi ngay

- Hoc:
  - Ban khong can ca ngay de tien bo.
- Lam:
  - Chot routine 90 phut:
    - 15 phut review
    - 25 phut nghien cuu
    - 25 phut test/ghi chep
    - 25 phut tong ket
- Viet:
  - `docs/playbooks/daily-rhythm.md`
- Goi lenh:
  - `.\scripts\start\qday.ps1 -Day 29`

#### Ngay 30. Lenh cho thang 2

- Hoc:
  - Cat bo va chon loc la nang luc quan trong.
- Lam:
  - Chot:
    - engine nao scale
    - engine nao dung
    - san pham nao dong goi
    - kenh nao tiep tuc xay
- Viet:
  - `reports/month-02-order.md`
- Goi lenh:
  - `.\scripts\start\qreview.ps1 -Week 4`

---

## Phan VII. Tieu chuan ra quyet dinh

Mot chien luoc duoc phep song tiep chi khi dat du 5 cong:

1. Co logic kinh te hoac microstructure toi thieu.
2. Co ket qua chap nhan duoc khi bo recovery.
3. Co stress test khong gay vo toan bo thesis.
4. Co tham so tuong doi on dinh.
5. Co risk of ruin phu hop voi quy mo von that.

Neu thieu 1 trong 5 cong nay, chien luoc chua duoc phep goi la cot song.

---

## Phan VIII. Tu duy backtest MQL5 cho bot multi-logic

### 1. Khong backtest theo kieu "nap set va xem loi nhuan"

Voi mot bot nhu 2.9.8, backtest theo kieu nap set vao roi xem duong von la cach nhanh nhat de tu lua minh.

Ly do:

- Bot co nhieu lop logic.
- Nhieu lop dang tat, nhieu lop dang bat.
- DCA va sniper co the che mat alpha that.
- Ket qua dep co the chi den tu viec thi truong lich su chua gap dung pha xau nhat.

Backtest dung phai tra loi duoc:

1. Signal nay co expectancy rieng khong?
2. DCA dang giup toi uu hay che bai?
3. Khoang cach DCA dang dung co phu hop voi bien dong that cua symbol khong?
4. Bo set co nhay voi digit, spread, session, va broker config khong?

### 2. Digit sensitivity la bai toan phai xu ly som

Day la mot diem rat thuc chien. Cung mot tham so `10` nhung:

- san 2 digit
- san 3 digit
- san 5 digit

co the cho ra y nghia hoan toan khac nhau neu code dang xu ly theo `point`, `pip`, hay `gia tri gia truc tiep`.

Vi vay, khi doc bat ky set nao, phai tu hoi:

- Bien khoang cach nay dang tinh theo `Point`, `Pip`, hay `Price`?
- Broker nay quote bao nhieu digits?
- Symbol nay co tick size la bao nhieu?
- Vang, forex, crypto, index co chung mot quy tac chuyen doi khong?

Neu khong co lop chuan hoa digit, set rat de:

- qua chat tren san nay
- qua rong tren san khac
- backtest dep nhung live te

### 3. Cach dung de chon khoang DCA

Khong chon khoang cach DCA bang cam giac. Cung khong chon bang mot con so "nhin thay hay".

Thu tu dung:

1. Lay du lieu lich su cua symbol theo khung gio dang dung.
2. Do phan bo bien dong:
   - median range
   - ATR
   - adverse excursion
   - khoang gia giua cac lan swing nguoc
3. Chuan hoa ve cung mot don vi:
   - point
   - pip
   - ATR multiple
4. Dung phan bo nay de de xuat:
   - `distance0`
   - `distance ladder`
   - `hard stop zone`
5. Sau do moi backtest.

Noi ngan gon:

`doc pho gia truoc, dat DCA sau`

### 4. DCA phai la ham cua thi truong, khong phai ham cua su hy vong

Khoang DCA dung nen duoc hinh thanh tu:

- symbol
- timeframe
- session
- signal mode
- volatility regime

Khong nen duoc hinh thanh tu:

- cam giac "lan truoc de 10 thay on"
- tam ly muon vao day hon cho nhanh hoi
- thoi quen sao chep set giua cac broker

### 5. Khung nghien cuu dung cho bot 2.9.8

#### Lop 1. Symbol profile

Moi symbol can co 1 ho so:

- digits
- point size
- tick size
- spread median
- ATR median
- session behavior

#### Lop 2. Signal profile

Moi signal can co 1 ho so:

- tan suat vao lenh
- adverse excursion trung vi
- favorable excursion trung vi
- ratio giua rung lac va xu huong

#### Lop 3. DCA profile

Sau khi co 2 lop tren moi duoc de xuat:

- DCA start
- DCA ladder
- max layers
- max lots
- TP recovery

#### Lop 4. Broker profile

Moi broker phai co note rieng:

- digits
- spread gio cao diem
- spread gio tin
- slippage co dien
- symbol naming

Khong co broker profile thi rat de test sai va set sai.

### 6. Cong cu da them vao workspace

De bat dau theo huong nay, workspace da co:

- `.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set`
- `.\scripts\start\qanalyze-symbol-csv.ps1 -CsvFile .\data\XAUUSD_M15.csv`

Script thu hai dung de doc CSV OHLC va de xuat range bien dong, adverse excursion co ban, va ladder DCA goi y.

### 7. Bai tap ve nha thuc chien

1. Xuat du lieu XAUUSD tu broker thanh CSV theo khung gio ban trade nhieu nhat.
2. Chay `qanalyze-symbol-csv.ps1`.
3. Ghi ket qua vao `research/xauusd-price-spectrum.md`.
4. Tao 3 set:
   - set chat
   - set vua
   - set rong
5. Backtest cung mot signal, cung mot khoang thoi gian, chi thay `distance ladder`.

Muc tieu khong phai tim bo dep nhat. Muc tieu la tim vung on dinh nhat.

---

## Phan IX. Tinh than lam nghe

Hung muon chot tai lieu nay bang mot quan diem rat ro:

- Thi truong la noi minh vao hoc nghe, khong phai noi minh den de hon thua voi ai.
- Ban co the kiem tien tu affiliate, tu bot, tu trading, tu dong goi tri thuc. Nhung neu ban khong ton trong nghe, som muon he thong cung bi hu.
- Nguoi di duoc lau thuong khong phai nguoi khoe nhat. Thuong la nguoi biet rut bot cai toi, bot chay theo so dong, va bot tu lua minh.

Neu ban hoc het 30 ngay nay mot cach nghiem tuc, muc tieu tot nhat khong phai la "tro thanh than dong". Muc tieu tot nhat la:

- biet minh dang lam gi
- biet minh dang dung vao loai edge nao
- biet khi nao phai dung
- biet cach de lai he thong cho minh va cho nguoi khac

Do moi la nen cua mot trader co tu cach va co duong di dai hon.

---

## Phu luc. Kien truc file de bat dau ngay

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

### Lenh khoi dong de nho

```powershell
.\scripts\bootstrap\windows\setup.ps1
.\scripts\start\qstart.ps1
.\scripts\start\qday.ps1 -Day 8
.\scripts\start\qreview.ps1 -Week 1
```

### Viec can lam tiep theo

1. Doc file `demo.set` va tach bot thanh 4 lop: signal, filter, sizing, recovery.
2. Chay script setup de tao bo khung hoc.
3. Dung `.\scripts\start\qanalyze-set.ps1 -SetFile .\demo.set` de lay tong quan cau hinh.
4. Xuat CSV gia va dung `.\scripts\start\qanalyze-symbol-csv.ps1 -CsvFile <duong_dan_csv>`.
5. Bat dau tu Ngay 1, khong nhay coc.
