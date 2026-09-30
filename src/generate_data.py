import numpy as np
import pandas as pd
from pathlib import Path

def generate_orders(n=50_000, seed=42):
    rng = np.random.default_rng(seed)
    start = pd.Timestamp("2026-01-01")
    df = pd.DataFrame({
        "order_id": np.arange(1, n + 1),
        "store_id": rng.integers(1, 21, n),
        "order_time": start + pd.to_timedelta(rng.integers(0, 90 * 24 * 3600, n), unit="s"),
        "items": rng.integers(1, 15, n),
        "order_value": rng.gamma(shape=3, scale=180, size=n).round(2),
        "delivery_minutes": rng.normal(18, 6, n).round(1),
    })
    # inject mess: nulls, negatives, duplicates
    df.loc[rng.choice(n, 400, replace=False), "order_value"] = np.nan
    df.loc[rng.choice(n, 200, replace=False), "delivery_minutes"] = -1
    df = pd.concat([df, df.sample(300, random_state=1)])
    return df

if __name__ == "__main__":
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    generate_orders().to_csv("data/raw/orders.csv", index=False)
    print("Wrote data/raw/orders.csv")