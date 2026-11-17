# Superstore Sales & Profit Business Analytics

An end-to-end sales analysis project: KPIs calculated in **MySQL** and visualized in an interactive **Power BI** dashboard.

## Project Overview

| Item | Details |
|---|---|
| Dataset | `superstore_cleaned.csv` |
| Records | 51,290 rows (2011–2014) |
| Currency | USD ($) |
| Database | `sales_business_analytics` |
| Table | `sales_import_check` |
| SQL tool | MySQL Workbench |
| Dashboard tool | Power BI (DAX) |

## Key KPIs

| KPI | Value |
|---|---|
| Total Sales | $12,642,501.91 |
| Total Profit | $1,467,457.29 |
| Total Orders | 25,035 |
| Unique Customers | 1,590 |
| Average Order Value | $504.99 |
| Profit Margin | 11.61% |

## Key Insights

- **Top region:** Central, with $2,822,302.52 in sales and $311,403.98 in profit.
- **Top category:** Technology, with $4,744,557.50 in sales.
- **Peak month:** November 2014, with $555,279.03 in sales.
- **Top product:** Apple Smart Phone, Full Size ($86,935.78).
- **Top customer:** Tom Ashbrook ($35,668.12). **Most frequent:** Patrick O'Brill (41 orders).
- **Discounts hurt profit:** No discount earns $1,770,695.27, while discounts above 40% lose $627,411.02.

## Dataset Columns

`row_id`, `order_id`, `order_date`, `ship_date`, `ship_mode`, `customer_id`, `customer_name`, `segment`, `city`, `state`, `country`, `postal_code`, `market`, `region`, `product_id`, `category`, `sub_category`, `product_name`, `sales`, `quantity`, `discount`, `profit`, `shipping_cost`, `order_priority`

## Dashboard Features

- Six KPI cards (sales, profit, orders, customers, average order value, profit margin)
- Monthly sales and profit trend
- Sales by region and by category
- Profit by sub-category
- Profit by discount level
- Top products and top customers
- Slicers for year, region, category and segment, plus a Reset button

## DAX Measures

```DAX
Total Sales = SUM(superstore_cleaned[sales])
Total Profit = SUM(superstore_cleaned[profit])
Total Orders = DISTINCTCOUNT(superstore_cleaned[order_id])
Unique Customers = DISTINCTCOUNT(superstore_cleaned[customer_id])
Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

Discount Level =
SWITCH(
    TRUE(),
    superstore_cleaned[discount] = 0, "1. No Discount",
    superstore_cleaned[discount] <= 0.2, "2. 1-20%",
    superstore_cleaned[discount] <= 0.4, "3. 21-40%",
    "4. Above 40%"
)
```

`Discount Level` is a calculated column. The others are measures.

## How to Use

1. Open the Power BI file (`.pbix`) in Power BI Desktop.
2. If the data source path is different on your computer, go to **Transform data > Data source settings** and point it to `superstore_cleaned.csv`.
3. Use the slicers to filter the report. Click **Reset** (Ctrl+click in Desktop) to clear all filters.

## Team

| Member | Contribution |
|---|---|
| Member 4 | SQL KPI calculations and business analysis (PR #24, `member-4/kpi-sql`) |
| Member 5 (Abhijit Todmal) | Power BI dashboard development |

## Repository Structure

```
├── data/        superstore_cleaned.csv
├── dashboard/   Power BI report (.pbix) and background image
└── README.md
```

Adjust the folder names to match your repository.
