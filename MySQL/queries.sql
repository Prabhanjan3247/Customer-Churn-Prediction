SELECT COUNT(*) AS customers_left
FROM customer_churn
WHERE Churn = 'Yes';

SELECT
    ContractType,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge
FROM customer_churn
GROUP BY ContractType
ORDER BY avg_monthly_charge DESC;

SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END AS age_group,
    COUNT(*) AS customer_count
FROM customer_churn
GROUP BY age_group
ORDER BY customer_count DESC;

SELECT *
FROM customer_churn
WHERE Rating < 3
ORDER BY Rating ASC, CustomerID;

SELECT *
FROM customer_churn
WHERE TenureMonths > 24
ORDER BY TenureMonths DESC;
