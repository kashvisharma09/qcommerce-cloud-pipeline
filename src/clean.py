import pandas as pd

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["order_time"] = pd.to_datetime(df["order_time"])

    # 1. drop duplicate orders (keep the first occurrence)
    df = df.drop_duplicates(subset="order_id", keep="first")

    # 2. drop rows with a missing order value
    df = df.dropna(subset=["order_value"])

    # 3. keep only valid delivery times
    df = df[df["delivery_minutes"] > 0]

    # 4. derived time columns
    df["order_date"] = df["order_time"].dt.date
    df["hour"] = df["order_time"].dt.hour

    # 5. SLA flag: delivered in under 20 minutes
    df["sla_met"] = df["delivery_minutes"] < 20

    return df.reset_index(drop=True)