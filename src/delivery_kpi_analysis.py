
import pandas as pd

# Load processed delivery data
df = pd.read_csv("data/processed/delivered_orders.csv")

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# Keep records with the dates needed for analysis
df = df.dropna(subset=date_columns).copy()

# Calculate actual and estimated delivery duration
df["delivery_days"] = (
    df["order_delivered_customer_date"] -
    df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

df["estimated_delivery_days"] = (
    df["order_estimated_delivery_date"] -
    df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Identify on-time and delayed orders
df["delivery_status"] = (
    df["order_delivered_customer_date"] <=
    df["order_estimated_delivery_date"]
).map({True: "On-Time", False: "Delayed"})

# Calculate KPIs
total_orders = len(df)
average_delivery = df["delivery_days"].mean()

on_time_orders = (df["delivery_status"] == "On-Time").sum()
delayed_orders = (df["delivery_status"] == "Delayed").sum()

on_time_rate = (on_time_orders / total_orders) * 100
delay_percentage = (delayed_orders / total_orders) * 100

# Display results
print("\n===== E-COMMERCE DELIVERY KPI REPORT =====")
print("Total Delivered Orders:", total_orders)
print("Average Delivery Duration:", round(average_delivery, 2), "days")
print("On-Time Orders:", on_time_orders)
print("Delayed Orders:", delayed_orders)
print("On-Time Delivery Rate:", round(on_time_rate, 2), "%")
print("Delay Percentage:", round(delay_percentage, 2), "%")

# Save KPI data
df.to_csv("data/processed/delivery_kpi_results.csv", index=False)

print("\nKPI results saved successfully!")
