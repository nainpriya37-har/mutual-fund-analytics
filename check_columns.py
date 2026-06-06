import pandas as pd

print("NAV HISTORY COLUMNS")
df = pd.read_csv("data/raw/02_nav_history.csv")
print(df.columns.tolist())

print("\nINVESTOR TRANSACTIONS COLUMNS")
df = pd.read_csv("data/raw/08_investor_transactions.csv")
print(df.columns.tolist())

print("\nSCHEME PERFORMANCE COLUMNS")
df = pd.read_csv("data/raw/07_scheme_performance.csv")
print(df.columns.tolist())