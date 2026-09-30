from pathlib import Path
import pandas as pd
from clean import clean_orders

RAW_PATH = Path("data/raw/orders.csv")
OUT_PATH = Path("data/processed/orders_clean.csv")

def main():
    raw = pd.read_csv(RAW_PATH)
    clean = clean_orders(raw)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(OUT_PATH, index=False)

    print(f"Rows in:  {len(raw)}")
    print(f"Rows out: {len(clean)}")
    print(f"SLA compliance: {clean['sla_met'].mean():.1%}")
    print(f"Wrote {OUT_PATH}")

if __name__ == "__main__":
    main()