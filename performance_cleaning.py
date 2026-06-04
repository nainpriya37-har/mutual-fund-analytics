import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert returns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check expense ratio range

anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies)

# Remove duplicate rows

df = df.drop_duplicates()

# Save cleaned file

df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nPerformance cleaned successfully")
print("Rows:", len(df))