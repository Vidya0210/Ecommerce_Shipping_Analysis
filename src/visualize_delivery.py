
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create output folder
Path("outputs/charts").mkdir(parents=True, exist_ok=True)

# Load KPI data
df = pd.read_csv("data/processed/delivery_kpi_results.csv")

# Convert dates
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"]
)

df["order_delivered_customer_date"] = pd.to_datetime(
    df["order_delivered_customer_date"]
)

sns.set_theme(style="whitegrid")

# CHART 1: On-time vs Delayed Orders
status_counts = df["delivery_status"].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(
    x=status_counts.index,
    y=status_counts.values
)
plt.title("On-Time vs Delayed Orders")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("outputs/charts/delivery_status.png")
plt.close()

# CHART 2: Monthly Delivery Performance
df["month"] = (
    df["order_purchase_timestamp"].dt.to_period("M").astype(str)
)

monthly = df.groupby("month").agg(
    total_orders=("order_id", "count"),
    on_time_orders=("delivery_status",
                    lambda x: (x == "On-Time").sum())
)

monthly["on_time_rate"] = (
    monthly["on_time_orders"] / monthly["total_orders"] * 100
)

plt.figure(figsize=(12, 5))
sns.lineplot(
    data=monthly,
    x=monthly.index,
    y="on_time_rate",
    marker="o"
)
plt.title("Monthly On-Time Delivery Rate")
plt.xlabel("Month")
plt.ylabel("On-Time Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/charts/monthly_delivery.png")
plt.close()

# CHART 3: Weekday vs Weekend Delivery Duration
df["purchase_day"] = (
    df["order_purchase_timestamp"].dt.dayofweek
)

df["day_type"] = df["purchase_day"].apply(
    lambda day: "Weekend" if day >= 5 else "Weekday"
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="day_type",
    y="delivery_days"
)
plt.title("Average Delivery Duration: Weekday vs Weekend")
plt.xlabel("Purchase Day Type")
plt.ylabel("Average Delivery Days")
plt.tight_layout()
plt.savefig("outputs/charts/weekday_weekend.png")
plt.close()

print("All three charts created successfully!")

print("\nCharts saved in outputs/charts/")
