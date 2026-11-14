
import pandas as pd
import os

# Folder paths
DATA_PATH = "data/raw"
OUTPUT_PATH = "data/processed"

os.makedirs(OUTPUT_PATH, exist_ok=True)

print("=" * 60)
print("       E-COMMERCE DATA PREPROCESSING")
print("=" * 60)

# Load orders dataset
orders = pd.read_csv(
    os.path.join(DATA_PATH, "olist_orders_dataset.csv")
)

# Convert date columns into datetime format
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(
        orders[col], errors="coerce"
    )

print("\n1. Date conversion completed!")

# Check order statuses
print("\n2. Order Status Summary:")
print(orders["order_status"].value_counts())

# Check missing delivery dates
print("\n3. Missing Delivery Dates:")
print(
    orders[
        ["order_delivered_carrier_date",
         "order_delivered_customer_date"]
    ].isnull().sum()
)

# Check duplicate order IDs
print("\n4. Duplicate Order IDs:")
print(orders["order_id"].duplicated().sum())

# Calculate delivery duration for delivered orders
delivered = orders[
    orders["order_status"] == "delivered"
].copy()

delivered["delivery_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Remove invalid delivery durations from analysis
valid_deliveries = delivered[
    delivered["delivery_days"].notna()
    & (delivered["delivery_days"] >= 0)
].copy()

print("\n5. Delivery Analysis:")
print("Delivered orders:", len(delivered))
print("Valid delivery records:", len(valid_deliveries))
print(
    "Average delivery days:",
    round(valid_deliveries["delivery_days"].mean(), 2)
)

# Save processed datasets
orders.to_csv(
    os.path.join(OUTPUT_PATH, "orders_processed.csv"),
    index=False
)

valid_deliveries.to_csv(
    os.path.join(OUTPUT_PATH, "delivered_orders.csv"),
    index=False
)

print("\n6. Processed files saved successfully!")
print("\nPREPROCESSING COMPLETED!")
