
-- =====================================================
-- PROJECT: Sales & Business Performance Analytics
-- ROLE: Member 4 - KPI Calculations and SQL Queries
-- DATABASE: sales_business_analytics
-- TABLE: sales_import_check
-- DESCRIPTION: Core Business KPI Calculations
-- =====================================================

USE sales_business_analytics;

-- KPI 1: Total Sales
SELECT SUM(sales) AS total_sales FROM sales_import_check;

-- KPI 2: Total Profit
SELECT SUM(profit) AS total_profit FROM sales_import_check;

-- KPI 3: Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders FROM sales_import_check;

-- KPI 4: Unique Customers
SELECT COUNT(DISTINCT customer_id) AS unique_customers FROM sales_import_check;

-- KPI 5: Average Order Value (AOV)
SELECT ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM sales_import_check;

-- KPI 6: Profit Margin
SELECT ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_percentage
FROM sales_import_check;
