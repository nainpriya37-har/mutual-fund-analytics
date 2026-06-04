import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = [
    "clean_nav_history.csv",
    "clean_investor_transactions.csv",
    "clean_scheme_performance.csv"
]

for file in files:

    df = pd.read_csv(
        f"data/processed/{file}"
    )

    table = file.replace(
        ".csv",
        ""
    )

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        table,
        len(df)
    )