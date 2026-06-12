# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project is an end-to-end Mutual Fund Analytics Platform built using Python, SQL, SQLite, Jupyter Notebook, and Power BI. The objective is to analyze mutual fund performance, investor behavior, industry trends, and portfolio risk through data analytics and visualization.

---

## Project Features

* ETL Pipeline for data processing
* Data Cleaning and Validation
* SQLite Database Integration
* Exploratory Data Analysis (EDA)
* Performance Analytics (CAGR, Sharpe Ratio, Alpha, Beta, etc.)
* Advanced Risk Analytics (VaR, CVaR, HHI)
* Interactive Power BI Dashboard
* Fund Recommendation Engine

---

## Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── charts
│   ├── csv outputs
│   ├── dashboard screenshots
│   └── Final_Report.pdf
│
├── scripts/
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* SQL
* Jupyter Notebook
* Power BI

---

## Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd mutual_fund_analytics
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Data Processing

Run the following scripts in order:

```bash
python data_ingestion.py
python nav_cleaning.py
python transaction_cleaning.py
python performance_cleaning.py
python load_sqlite.py
```

### Open Analytics Notebooks

```bash
jupyter notebook
```

Run:

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

---

## Power BI Dashboard

Open the dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

Dashboard Pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends

---

## Key Insights

* SIP inflows increased consistently from 2022–2025.
* Equity funds remained the most preferred investment category.
* SBI Mutual Fund maintained the highest AUM.
* Investors aged 25–40 dominated transaction activity.
* Diversified portfolios showed lower risk exposure.
* Risk-adjusted metrics helped identify top-performing funds.

---

## Deliverables

* ETL Pipeline
* SQLite Database
* EDA Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Report
* Presentation Slides

---

## Author

**Priya Nain**

Bluestock Mutual Fund Analytics Capstone Project
