from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = (len(ordered) - 1) * q
    lo = math.floor(idx)
    hi = math.ceil(idx)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (idx - lo)


def detect_column(row: dict[str, str], names: list[str]) -> str:
    lowered = {k.lower(): k for k in row}
    for name in names:
        if name.lower() in lowered:
            return lowered[name.lower()]
    raise KeyError(f"Missing columns. Tried: {names}")


def read_rows(path: Path) -> list[dict[str, float]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        first = next(reader)
        columns = reader.fieldnames or []
        high_key = detect_column(first, ["high", "<high>"])
        low_key = detect_column(first, ["low", "<low>"])
        open_key = detect_column(first, ["open", "<open>"])
        close_key = detect_column(first, ["close", "<close>"])
        rows = [{
            "open": float(first[open_key]),
            "high": float(first[high_key]),
            "low": float(first[low_key]),
            "close": float(first[close_key]),
        }]
        for row in reader:
            rows.append({
                "open": float(row[open_key]),
                "high": float(row[high_key]),
                "low": float(row[low_key]),
                "close": float(row[close_key]),
            })
        return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--digits", type=int, default=2)
    parser.add_argument("--atr-window", type=int, default=14)
    args = parser.parse_args()

    path = Path(args.csv)
    rows = read_rows(path)
    if len(rows) < args.atr_window + 2:
        raise SystemExit("Not enough rows in CSV.")

    point = 10 ** (-args.digits)
    ranges = [r["high"] - r["low"] for r in rows]
    true_ranges: list[float] = []
    for i, row in enumerate(rows):
        if i == 0:
            true_ranges.append(row["high"] - row["low"])
            continue
        prev_close = rows[i - 1]["close"]
        tr = max(
            row["high"] - row["low"],
            abs(row["high"] - prev_close),
            abs(row["low"] - prev_close),
        )
        true_ranges.append(tr)

    atr_series: list[float] = []
    for i in range(args.atr_window - 1, len(true_ranges)):
        atr_series.append(statistics.mean(true_ranges[i - args.atr_window + 1:i + 1]))

    median_range = statistics.median(ranges)
    p75_range = percentile(ranges, 0.75)
    p90_range = percentile(ranges, 0.90)
    median_atr = statistics.median(atr_series)

    suggested_tight = max(median_range * 0.8, median_atr * 0.6)
    suggested_mid = max(median_range * 1.1, median_atr * 0.9)
    suggested_wide = max(p75_range * 1.1, median_atr * 1.2)

    print("=== Price Spectrum Analysis ===")
    print(f"CSV: {path}")
    print(f"Rows: {len(rows)}")
    print(f"Digits: {args.digits}")
    print(f"Point size: {point}")
    print("")
    print(f"Median range: {median_range:.5f}")
    print(f"P75 range:    {p75_range:.5f}")
    print(f"P90 range:    {p90_range:.5f}")
    print(f"Median ATR:   {median_atr:.5f}")
    print("")
    print("Suggested DCA ladder anchors:")
    print(f"- Tight: {suggested_tight:.5f} ({suggested_tight / point:.1f} points)")
    print(f"- Mid:   {suggested_mid:.5f} ({suggested_mid / point:.1f} points)")
    print(f"- Wide:  {suggested_wide:.5f} ({suggested_wide / point:.1f} points)")
    print("")
    print("Interpretation:")
    print("- Tight is only for calmer regimes and stronger signals.")
    print("- Mid is the default research anchor.")
    print("- Wide is for stress testing and trend shock tolerance.")


if __name__ == "__main__":
    main()

