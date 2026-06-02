import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("Fund Houses")
print(df["fund_house"].unique())

print("Categories")
print(df["category"].unique())

print("Sub Categories")
print(df["subcategory"].unique())

print("Risk Grades")
print(df["risk_grade"].unique())