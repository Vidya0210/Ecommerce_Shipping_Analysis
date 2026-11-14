
import pandas as pd

# Load processed delivery data
df = pd.read_csv(
    "data/processed/delivery_kpi_results.csv"
)

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_delivered_carrier_date",
    "order_delivered_customer_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column], errors="coerce"
    )

# Remove records with missing dates
df = df.dropna(subset=date_columns).copy()

# Calculate purchase-to-carrier handoff duration
df["handoff_days"] = (
    df["order_delivered_carrier_date"] -
    df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Calculate carrier-to-customer delivery duration
df["carrier_transit_days"] = (
    df["order_delivered_customer_date"] -
    df["order_delivered_carrier_date"]
).dt.total_seconds() / 86400

# Remove invalid negative durations
df = df[
    (df["handoff_days"] >= 0) &
    (df["carrier_transit_days"] >= 0)
].copy()

# Display report
print("\n===== CARRIER HANDOFF ANALYSIS =====")

print("Orders Analyzed:", len(df))

print(
    "Average Purchase-to-Carrier Handoff:",
    round(df["handoff_days"].mean(), 2),
    "days"
)

print(
    "Average Carrier-to-Customer Transit:",
    round(df["carrier_transit_days"].mean(), 2),
    "days"
)

print(
    "Fastest Handoff:",
    round(df["handoff_days"].min(), 2),
    "days"
)

print(
    "Slowest Handoff:",
    round(df["handoff_days"].max(), 2),
    "days"
)

# Monthly handoff analysis
df["month"] = (
    df["order_purchase_timestamp"]
    .dt.to_period("M").astype(str)
)

monthly_report = df.groupby("month").agg(
    total_orders=("order_id", "count"),
    average_handoff_days=("handoff_days", "mean"),
    average_transit_days=("carrier_transit_days", "mean")
).round(2).reset_index()

print("\n===== MONTHLY HANDOFF REPORT =====")
print(monthly_report.to_string(index=False))

# Save reports
df.to_csv(
    "data/processed/carrier_handoff_results.csv",
    index=False
)

monthly_report.to_csv(
    "data/processed/monthly_handoff_report.csv",
    index=False
)

print("\nCarrier handoff reports saved successfully!")
