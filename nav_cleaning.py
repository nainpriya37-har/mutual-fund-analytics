import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# convert date
df["date"] = pd.to_datetime(df["date"])

# sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# remove duplicates
df = df.drop_duplicates()

# fill missing NAV
df["nav"] = df.groupby(
    "amfi_code"
)["nav"].ffill()

# keep only positive nav
df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("NAV cleaned")