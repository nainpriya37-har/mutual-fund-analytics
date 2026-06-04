import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.upper()
    .str.strip()
)

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Fix date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Valid KYC values
print("\nUnique KYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nTransactions cleaned successfully")
print("Rows:", len(df))