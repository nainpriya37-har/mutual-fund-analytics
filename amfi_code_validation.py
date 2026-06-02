import pandas as pd

master = pd.read_csv(
    "data/raw/fund_master.csv"
)

nav = pd.read_csv(
    "data/raw/nav_history.csv"
)

missing = set(master["scheme_code"]) - set(nav["scheme_code"])

print("Missing Codes:", len(missing))

print(missing)