import pandas as pd

perf = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

print("\nAvailable Risk Grades:")
print(perf["risk_grade"].unique())

risk = input(
    "\nEnter Risk (Low/Moderate/High): "
)

result = (
    perf[
        perf["risk_grade"].str.lower()
        == risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    result[
        [
            "scheme_name",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]
)