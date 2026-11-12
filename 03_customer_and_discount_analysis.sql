
-- =====================================================
-- PROJECT: Sales & Business Performance Analytics
-- ROLE: Member 4 - KPI Calculations and SQL Queries
-- FILE: Customer and Discount Analysis
-- =====================================================

USE sales_business_analytics;

-- 1. Customer-wise Sales and Profit
SELECT customer_id, customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_import_check
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC;

-- 2. Top 10 Customers by Sales
SELECT customer_id,customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_import_check
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- 3. Customer Order Frequency
SELECT customer_id,customer_name,
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_import_check
GROUP BY customer_id, customer_name
ORDER BY total_orders DESC
LIMIT 10;

-- 4. Discount-wise Sales and Profit
SELECT discount,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit), 2) AS average_profit
FROM sales_import_check
GROUP BY discount
ORDER BY discount;

-- 5. Profitability by Discount Band
SELECT CASE
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount <= 0.10 THEN '0-10%'
        WHEN discount <= 0.20 THEN '10-20%'
        WHEN discount <= 0.30 THEN '20-30%'
        WHEN discount <= 0.40 THEN '30-40%'
        ELSE 'Above 40%'
    END AS discount_band,
    COUNT(*) AS total_records,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        (SUM(profit) / NULLIF(SUM(sales), 0)) * 100, 2
    ) AS profit_margin_percentage
FROM sales_import_check
GROUP BY discount_band
ORDER BY MIN(discount);
