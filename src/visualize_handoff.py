
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create output folder
Path("outputs/charts").mkdir(parents=True, exist_ok=True)

# Load reports
monthly = pd.read_csv(
    "data/processed/monthly_handoff_report.csv"
)

df = pd.read_csv(
    "data/processed/carrier_handoff_results.csv"
)

sns.set_theme(style="whitegrid")

# CHART 1: Monthly Handoff vs Transit Time
# Exclude months with fewer than 100 orders
monthly_filtered = monthly[
    monthly["total_orders"] >= 100
].copy()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_filtered["month"],
    monthly_filtered["average_handoff_days"],
    marker="o",
    label="Purchase to Carrier Handoff"
)

plt.plot(
    monthly_filtered["month"],
    monthly_filtered["average_transit_days"],
    marker="o",
    label="Carrier to Customer"
)

plt.title("Monthly Delivery Stage Performance")
plt.xlabel("Month")
plt.ylabel("Average Duration (Days)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    "outputs/charts/monthly_handoff_performance.png"
)
plt.close()

# CHART 2: Overall Stage Duration Comparison
stage_data = pd.DataFrame({
    "Delivery Stage": [
        "Purchase to Carrier Handoff",
        "Carrier to Customer"
    ],
    "Average Days": [
        df["handoff_days"].mean(),
        df["carrier_transit_days"].mean()
    ]
})

plt.figure(figsize=(9, 5))

sns.barplot(
    data=stage_data,
    x="Delivery Stage",
    y="Average Days"
)

plt.title("Average Delivery Time by Stage")
plt.xlabel("Delivery Stage")
plt.ylabel("Average Duration (Days)")
plt.xticks(rotation=10)
plt.tight_layout()

plt.savefig(
    "outputs/charts/delivery_stage_comparison.png"
)
plt.close()

print("Handoff performance charts created successfully!")
print("Charts saved in outputs/charts/")
