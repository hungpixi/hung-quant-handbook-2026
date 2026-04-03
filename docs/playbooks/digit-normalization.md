# Digit Normalization Va DCA Distance

## Van de

Bot MQL5 rat de gap loi khi cung mot input duoc hieu khac nhau tren cac broker.

Vi du:

- Broker A quote vang 2 digits
- Broker B quote vang 3 digits

Neu code xu ly khoang cach dua tren `Point()` ma khong normalize, cung mot `distance=10` se cho ket qua khac xa.

## Dieu can ghi lai cho moi broker/symbol

- `_Digits`
- `_Point`
- `SYMBOL_TRADE_TICK_SIZE`
- `SYMBOL_TRADE_TICK_VALUE`
- spread median
- spread max trong gio tin

## Cach nghi dung

Khong nghi theo "10 points" truoc.
Nghi theo:

- `distance = x * ATR`
- hoac `distance = y * median adverse excursion`

Sau do moi quy doi ve point/pip phu hop voi broker do.

## Quy tac thuc chien

1. Xac dinh don vi noi bo cua EA.
2. Xac dinh don vi test trong broker.
3. Viet bang quy doi cho tung symbol.
4. Khong copy set giua broker neu chua quy doi lai.

