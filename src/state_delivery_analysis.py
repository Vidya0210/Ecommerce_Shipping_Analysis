
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create output folder
Path("outputs/charts").mkdir(parents=True, exist_ok=True)

# Load datasets
orders = pd.read_csv("data/processed/delivery_kpi_results.csv")
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")

# Merge orders with customer state
df = orders.merge(
    customers[["customer_id", "customer_state"]],
    on="customer_id",
    how="left"
)

# Calculate state-wise delivery performance
state_report = df.groupby("customer_state").agg(
    total_orders=("order_id", "count"),
    on_time_orders=(
        "delivery_status",
        lambda x: (x == "On-Time").sum()
    ),
    average_delivery_days=("delivery_days", "mean")
).reset_index()

# Calculate on-time delivery rate
state_report["on_time_rate"] = (
    state_report["on_time_orders"] /
    state_report["total_orders"] * 100
)

# Sort by on-time delivery rate
state_report = state_report.sort_values(
    "on_time_rate",
    ascending=False
)

# Save report
state_report.to_csv(
    "data/processed/state_delivery_report.csv",
    index=False
)

# Display results
print("\n===== STATE-WISE DELIVERY REPORT =====")
print(state_report.round(2).to_string(index=False))

# Visualize top 10 states by order volume
top_states = state_report.nlargest(10, "total_orders")

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_states,
    x="customer_state",
    y="on_time_rate"
)

plt.title("On-Time Delivery Rate - Top 10 States by Order Volume")
plt.xlabel("Customer State")
plt.ylabel("On-Time Delivery Rate (%)")
plt.tight_layout()

plt.savefig("outputs/charts/state_delivery_performance.png")
plt.close()

print("\nState report saved successfully!")
print("Chart saved in outputs/charts/")
