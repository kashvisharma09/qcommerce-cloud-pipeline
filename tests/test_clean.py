import pandas as pd
from clean import clean_orders

def make_df():
    return pd.DataFrame({
        "order_id": [1, 1, 2, 3, 4],
        "store_id": [1, 1, 2, 3, 4],
        "order_time": ["2026-01-01 10:00:00"] * 5,
        "items": [2, 2, 3, 1, 4],
        "order_value": [100.0, 100.0, None, 250.0, 300.0],
        "delivery_minutes": [15.0, 15.0, 12.0, -1.0, 25.0],
    })

def test_duplicates_removed():
    out = clean_orders(make_df())
    assert out["order_id"].is_unique

def test_no_missing_values_or_bad_times():
    out = clean_orders(make_df())
    assert out["order_value"].notna().all()
    assert (out["delivery_minutes"] > 0).all()

def test_sla_flag():
    out = clean_orders(make_df())
    assert out.loc[out["order_id"] == 1, "sla_met"].iloc[0]
    assert not out.loc[out["order_id"] == 4, "sla_met"].iloc[0]