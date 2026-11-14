
import pandas as pd

# Load datasets
orders = pd.read_csv(
    "data/processed/delivery_kpi_results.csv"
)

items = pd.read_csv(
    "data/raw/olist_order_items_dataset.csv"
)

# Remove duplicate order-seller combinations
items = items[["order_id", "seller_id"]].drop_duplicates()

# Merge datasets
merged = orders.merge(
    items,
    on="order_id",
    how="inner"
)

# Create numeric on-time indicator
merged["on_time_flag"] = (
    merged["delivery_status"] == "On-Time"
).astype(int)

# Group by seller
seller_report = merged.groupby("seller_id").agg(
    total_orders=("order_id", "nunique"),
    average_delivery_days=("delivery_days", "mean"),
    on_time_orders=("on_time_flag", "sum")
).reset_index()

# Calculate delayed orders
seller_report["delayed_orders"] = (
    seller_report["total_orders"] -
    seller_report["on_time_orders"]
)

# Calculate delivery percentages
seller_report["on_time_rate"] = (
    seller_report["on_time_orders"] /
    seller_report["total_orders"] * 100
).round(2)

# Filter sellers with at least 20 orders
seller_report = seller_report[
    seller_report["total_orders"] >= 20
].copy()

# Sort results
seller_report = seller_report.sort_values(
    "on_time_rate",
    ascending=False
)

# Display top sellers
print("\n===== TOP 10 SELLERS =====")
print(seller_report.head(10).to_string(index=False))

# Display bottom sellers
print("\n===== BOTTOM 10 SELLERS =====")
print(
    seller_report.tail(10)
    .sort_values("on_time_rate")
    .to_string(index=False)
)

# Save report
seller_report.to_csv(
    "data/processed/seller_performance_report.csv",
    index=False
)

print("\nSeller performance report saved successfully!")
