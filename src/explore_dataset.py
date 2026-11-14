
import pandas as pd
import os

# Dataset location
DATA_PATH = "data/raw"

# Load datasets
orders = pd.read_csv(
    os.path.join(DATA_PATH, "olist_orders_dataset.csv")
)

items = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_items_dataset.csv")
)

customers = pd.read_csv(
    os.path.join(DATA_PATH, "olist_customers_dataset.csv")
)

sellers = pd.read_csv(
    os.path.join(DATA_PATH, "olist_sellers_dataset.csv")
)

# Store datasets
datasets = {
    "Orders": orders,
    "Order Items": items,
    "Customers": customers,
    "Sellers": sellers
}

print("=" * 60)
print("       E-COMMERCE DATASET EXPLORATION")
print("=" * 60)

for name, df in datasets.items():

    print(f"\n\nDATASET: {name}")
    print("-" * 60)

    # Dataset dimensions
    print("Number of Rows:", df.shape[0])
    print("Number of Columns:", df.shape[1])

    # Display first 5 records
    print("\nFirst 5 Records:")
    print(df.head())

    # Column information
    print("\nColumn Information:")
    print(df.dtypes)

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate records
    print("\nDuplicate Rows:", df.duplicated().sum())

print("\n\nDATASET EXPLORATION COMPLETED!")
