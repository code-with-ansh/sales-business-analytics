
-- =====================================================
-- PROJECT: Sales & Business Performance Analytics
-- ROLE: Member 4 - KPI Calculations and SQL Queries
-- FILE: Sales Performance Analysis
-- =====================================================
USE sales_business_analytics;

-- 1. Sales by Region
SELECT region,ROUND(SUM(sales), 2) AS total_sales
FROM sales_import_check GROUP BY region
ORDER BY total_sales DESC;

-- 2. Profit by Region
SELECT region,ROUND(SUM(profit), 2) AS total_profit
FROM sales_import_check GROUP BY region
ORDER BY total_profit DESC;

-- 3. Sales and Profit by Category
SELECT category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_import_check GROUP BY category
ORDER BY total_sales DESC;

-- 4. Monthly Sales Trends
SELECT DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    ROUND(SUM(sales), 2) AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit
FROM sales_import_check
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- 5. Top 10 Products by Sales
SELECT product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_import_check
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;
