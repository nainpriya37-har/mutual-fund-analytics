-- Average NAV by Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM clean_nav_history
GROUP BY month
ORDER BY month;
-- Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM clean_scheme_performance
WHERE expense_ratio_pct < 1;
-- Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM clean_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 4 Highest 5-Year Returns

SELECT
scheme_name,
return_5yr_pct
FROM clean_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 5 Average Return by Fund House

SELECT
fund_house,
AVG(return_3yr_pct)
FROM clean_scheme_performance
GROUP BY fund_house;

-- 6 Transactions by State

SELECT
state,
COUNT(*) total_transactions
FROM clean_investor_transactions
GROUP BY state;

-- 7 Total Investment Amount by State

SELECT
state,
SUM(amount_inr)
FROM clean_investor_transactions
GROUP BY state;

-- 8 KYC Status Distribution

SELECT
kyc_status,
COUNT(*)
FROM clean_investor_transactions
GROUP BY kyc_status;

-- 9 Funds with Highest Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM clean_scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 10 Risk Grade Distribution

SELECT
risk_grade,
COUNT(*)
FROM clean_scheme_performance
GROUP BY risk_grade;