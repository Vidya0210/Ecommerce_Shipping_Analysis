
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create chart folder
Path("outputs/charts").mkdir(parents=True, exist_ok=True)

# Load seller report
df = pd.read_csv(
    "data/processed/seller_performance_report.csv"
)

sns.set_theme(style="whitegrid")

# Shorten seller IDs for chart readability
df["seller_short_id"] = df["seller_id"].str[:8]

# TOP 10 SELLERS
top_10 = df.nlargest(10, "on_time_rate").sort_values(
    "on_time_rate"
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_10,
    x="on_time_rate",
    y="seller_short_id"
)

plt.title("Top 10 Sellers - On-Time Delivery Rate")
plt.xlabel("On-Time Delivery Rate (%)")
plt.ylabel("Seller ID (first 8 characters)")
plt.xlim(0, 105)
plt.tight_layout()
plt.savefig("outputs/charts/top_sellers.png")
plt.close()

# BOTTOM 10 SELLERS
bottom_10 = df.nsmallest(10, "on_time_rate").sort_values(
    "on_time_rate"
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=bottom_10,
    x="on_time_rate",
    y="seller_short_id"
)

plt.title("Bottom 10 Sellers - On-Time Delivery Rate")
plt.xlabel("On-Time Delivery Rate (%)")
plt.ylabel("Seller ID (first 8 characters)")
plt.xlim(0, 105)
plt.tight_layout()
plt.savefig("outputs/charts/bottom_sellers.png")
plt.close()

print("Seller performance charts created successfully!")
print("Charts saved in outputs/charts/")

