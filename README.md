# sales-business-analytics
An interactive analytics dashboard that transforms sales data into actionable insights by tracking revenue, profit, order trends, and regional performance. Built using Python, SQL, and Power BI to identify growth opportunities and support data-driven business decisions.

## SQL Analysis 

This section covers KPI calculations and SQL-based business performance analysis using MySQL.

### SQL Files

1. **01_core_kpi_calculations.sql**
   - Total Sales
   - Total Profit
   - Total Orders
   - Unique Customers
   - Average Order Value (AOV)
   - Profit Margin

2. **02_sales_performance_analysis.sql**
   - Sales and Profit by Region
   - Sales and Profit by Category
   - Monthly Sales Trends
   - Top 10 Products by Sales

3. **03_customer_and_discount_analysis.sql**
   - Customer-wise Sales and Profit
   - Top 10 Customers by Sales
   - Customer Order Frequency
   - Discount-wise Sales and Profit
   - Profitability by Discount Band

### Tools Used
- MySQL
- MySQL Workbench
- SQL Aggregation Functions
- GROUP BY, ORDER BY, CASE and Subqueries

### Key Insights
- No-discount transactions generated the highest total profit.
- Higher discount levels were associated with lower profitability.
- Regional, category-wise and customer-wise analysis helps identify business performance patterns.
# Sales & Business Performance Analytics Dashboard

An end-to-end data analytics project focused on transforming raw retail transaction data into meaningful business insights through data cleaning, exploratory data analysis, customer segmentation, profitability analysis, and business intelligence.

## Project Overview

Businesses generate large volumes of sales data, but raw transactional records do not automatically reveal what drives revenue, where profitability is declining, or which customers contribute the most value.

This project aims to analyze historical retail sales data and develop a data-driven business performance analytics solution that helps identify sales trends, profitability patterns, customer behavior, and potential business improvement opportunities.

The project follows a structured four-week development approach, progressing from data preparation and analytical exploration to business insights and interactive dashboard development.

## Problem Statement

The objective is to analyze historical retail sales transactions to answer important business questions:

- How are sales and profits performing over time?
- Which product categories and subcategories contribute most to revenue and profitability?
- Which regions and markets perform better or worse?
- How do discounts affect business profitability?
- Which customers generate the highest revenue?
- What does customer purchasing and retention behavior reveal?
- Where should the business focus its improvement efforts?

The ultimate goal is to transform transactional data into actionable business intelligence.

## Dataset Information

**Dataset:** Superstore transaction dataset (`superstore_dataset2011-2015.csv`; observed dates 2011–2014)
**Source:** Kaggle
**Format:** CSV

| Attribute | Details |
|---|---|
| Original records | 51,290 |
| Original columns | 24 |
| Cleaned records | 51,290 |
| Cleaned columns | 24 |
| Data granularity | Order-line level |
| Historical period | 2011–2014 |

The dataset contains information about orders, customers, products, sales, discounts, profits, shipping costs, geographical locations, and order priorities.

**Important:** Each row represents an order line, not necessarily a unique order. Distinct `order_id` values are therefore used when calculating order volume.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas & NumPy | Data manipulation and numerical analysis |
| Matplotlib & Seaborn | Data visualization |
| Jupyter Notebook | Exploratory analysis and documentation |
| Git & GitHub | Version control and team collaboration |
| SQL | MySQL KPI calculations and grouped sales analysis |
| Power BI / Tableau | Planned interactive dashboard development |

## Repository Structure

```text
sales-business-analytics/
│
├── dashboard/                  # Dashboard development
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Cleaned and analytical datasets
│
├── docs/                       # Project documentation
├── notebooks/                  # Data analysis notebooks
├── reports/                    # Analytical reports
├── screenshots/                # Project visualizations
├── scripts/                    # Data processing and validation scripts
├── sql/                        # SQL queries and KPI analysis
│
├── README.md
└── .gitignore
```

## Project Development & Progress

### Week 1 – Data Exploration, Cleaning & Validation

<ins>Objective:</ins> Establish a reliable and consistent data foundation for further analysis.

**Work completed:**

- Integrated the original Superstore dataset into the project.
- Explored dataset structure, dimensions, column names, and data types.
- Performed missing-value and duplicate-value analysis.
- Investigated data granularity and unique order identifiers.
- Standardized inconsistent date formats.
- Validated order dates and shipping dates.
- Checked shipping duration, sales, quantity, discount, profit, and shipping cost values.
- Preserved meaningful negative-profit transactions for profitability analysis.
- Investigated missing postal codes without unnecessarily deleting records.
- Created a reusable data inspection, cleaning, and validation script at `scripts/data_cleaning.py`.
- Generated the cleaned dataset.

**Key outcome:**

The cleaned dataset retains all 51,290 records and all 24 original columns, with standardized dates and validated data quality.

### Week 2 – Exploratory Data Analysis & Business KPI Development

<ins>Objective:</ins> Understand business performance through quantitative analysis and visual exploration.

**1. Overall Business KPI Analysis**

- Total sales, total profit, and order volume.
- Average order value.
- Overall profit margin.
- Year-over-year business growth.
- Category, subcategory, regional, market, customer, and product performance.

**2. Time-Based Sales Analysis**

- Yearly, quarterly, and monthly sales and profit analysis.
- Year-wise quarterly comparisons.
- Month-over-month and year-over-year comparisons.
- Monthly performance patterns and seasonality exploration.

**3. Shipping Performance Analysis**

- Average and median shipping duration.
- Shipping mode comparisons.
- Shipping cost analysis.
- Delivery duration distribution.
- Fast, standard, and slow delivery classification.

**4. Discount Impact & Profitability Analysis**

- Discount distribution and frequency.
- Profit margin across discount ranges.
- Category-wise and subcategory-wise discount analysis.
- Identification of loss-making discount ranges.
- Furniture profitability investigation.

**5. Customer Segmentation Using RFM Analysis**

Implemented Recency, Frequency, and Monetary analysis to understand customer purchasing behavior.

Customers were classified into nine behavioral segments:

- Champions
- Loyal Customers
- Recent Customers
- Promising Customers
- Potential High Value
- At Risk Customers
- At Risk High Value
- Lost Customers
- Need Attention

Additional analysis included customer revenue contribution, purchase frequency, and Pareto analysis.

**6. Customer Cohort & Retention Analysis**

- Identified customer acquisition cohorts based on first observed purchase month.
- Developed a monthly cohort retention matrix covering 48 months.
- Calculated average, median, and weighted retention.
- Compared acquisition cohorts across different years.
- Identified stronger and weaker retention patterns.

## SQL Analysis 

This section covers KPI calculations and SQL-based business performance analysis using MySQL.

### SQL Files

1. **01_core_kpi_calculations.sql**
   - Total Sales
   - Total Profit
   - Total Orders
   - Unique Customers
   - Average Order Value (AOV)
   - Profit Margin

2. **02_sales_performance_analysis.sql**
   - Sales and Profit by Region
   - Sales and Profit by Category
   - Monthly Sales Trends
   - Top 10 Products by Sales

3. **03_customer_and_discount_analysis.sql**
   - Customer-wise Sales and Profit
   - Top 10 Customers by Sales
   - Customer Order Frequency
   - Discount-wise Sales and Profit
   - Profitability by Discount Band

### Tools Used
- MySQL
- MySQL Workbench
- SQL Aggregation Functions
- GROUP BY, ORDER BY, CASE and Subqueries

### Key Insights
- No-discount transactions generated the highest total profit.
- Higher discount levels were associated with lower profitability.
- Regional, category-wise and customer-wise analysis helps identify business performance patterns.

## Week 3 – Trend Analysis & Business Insight Development

<badge>Planned</badge>

**Engineering Focus:** Understand changes over time and translate observed patterns into testable business explanations.

**Planned implementation:**

- Analyze monthly, quarterly, and yearly sales and profit trends.
- Compare current periods against equivalent previous periods.
- Investigate performance changes across products, categories, regions, and customer segments.
- Examine seasonality where sufficient historical cycles are available.
- Investigate declining sales and low-profitability areas.
- Evaluate the influence of low-volume periods, missing periods, and unusual transactions.
- Develop visualizations using Matplotlib and Seaborn.
- Translate significant findings into evidence-based business recommendations.

**Expected Deliverables:**

- Trend analysis notebook.
- Supporting visualizations.
- Documented significant business findings.
- Draft business recommendations.

## Key Business Findings

The following findings have emerged from the completed analysis.

| Metric | Analytical Result |
|---|---:|
| Total Sales | $12.64 Million |
| Total Profit | $1.47 Million |
| Unique Orders | 25,035 |
| Overall Profit Margin | ~11.61% |
| Total Customers | 1,590 |
| Average Discount | 14.29% |
| Average Shipping Duration | ~3.97 Days |

**Important analytical insights:**

1. **Business Growth:** Sales increased consistently across the four historical years, with the highest yearly sales recorded in 2014.

2. **Discount Profitability:** Profitability declines as discount levels increase. The 20–30% discount band already shows a negative profit margin, highlighting the importance of profitability-aware discounting.

3. **Product Profitability:** The Tables subcategory records a negative profit margin, identifying an area that deserves further investigation.

4. **Customer Value:** Champions form the largest revenue-generating customer segment, contributing approximately $5.44 million in sales.

5. **Revenue Concentration:** Approximately 42.58% of customers contribute 80.07% of total customer revenue, demonstrating substantial revenue concentration.

6. **Customer Retention:** Weighted Month 1 cohort retention is approximately 18.82%, indicating an opportunity to improve repeat purchasing behavior.

7. **Shipping Performance:** Standard Class accounts for the largest order volume, while Same Day shipping has the shortest average delivery duration.

*Note: These are observational findings from historical data. Associations should not automatically be interpreted as causal relationships. Cohort retention measures observed monthly purchasing activity, not confirmed customer churn.*

## Analysis Methodology & Business Interpretation

This section explains how to present the analysis, why the metrics were selected, and what conclusions the data can and cannot support.

### Business problem and decision context

The analysis addresses a practical retail management problem: headline sales can grow while profit, product mix, customer repeat purchasing, or regional performance deteriorates. A business therefore needs to monitor both scale and return, locate where performance varies, and decide where further investigation or a controlled intervention is worthwhile.

The dataset supports descriptive questions such as “where and when were sales and profit higher?” and “which customers or products contributed most?” It does not by itself establish why a change occurred or predict what will happen next. Treat the results as decision signals for pricing, merchandising, and customer-retention investigations—not as proof that a particular action will cause improvement.

### Source, grain, and data quality

The project uses the Kaggle-distributed Superstore CSV in `data/raw/`. The supplied filename suggests 2011–2015, but the observed order dates run from 2011-01-01 through 2014-12-31. The analysis period is therefore four calendar years (2011–2014), not 2011–2015. The repository does not record a direct Kaggle listing URL or a dataset license; verify the original listing and its attribution terms before redistributing the data.

The dataset has 51,290 rows and 24 fields. A row is an order line, so summing sales/profit is appropriate for line-level totals, but counting rows would overstate orders. Order counts use distinct `order_id`; customer-level metrics use distinct `customer_id`. The records include order and shipping dates, product/category, customer, geography, sales, quantity, discount, profit, and shipping cost. These are historical transactions, not a live feed.

`scripts/data_cleaning.py` runs raw-data inspection, cleaning, validation, and raw-versus-cleaned comparisons in sequence. It standardizes column names and text, removes exact duplicate rows, parses mixed date strings using the verified day-first formats, preserves missing postal codes and negative-profit records, and stops if dates cannot be parsed or a ship date precedes its order date. It reports numeric anomalies (for example nonpositive sales/quantity and discounts outside 0–1) rather than silently deleting them. Retaining loss-making rows is essential because removing them would bias profitability upward.

The combined script validates expected row and column counts, duplicate rows, missing values outside postal code, and string date columns. It also compares totals for sales/profit/quantity, distinct orders/customers, missing postal codes, duplicate counts, and category/subcategory/region sales and profit aggregates with a $0.01 tolerance. Date equivalence is explicitly outside the raw-versus-cleaned comparison.

These are useful transformation and reconciliation checks, not a guarantee that the source is complete or that every business rule is correct. The script requires pandas. Run `python scripts/data_cleaning.py` to regenerate the cleaned file and perform the checks; if results differ, investigate before using the dashboard figures.

### KPI definitions and rationale

Unless a view explicitly says otherwise, calculations use the cleaned order-line data and the selected date/filter context:

| KPI | Definition | Why it is useful / interpretation |
|---|---|---|
| Sales | Sum of `sales` | Measures transaction value and business scale; not the same as cash collected or net revenue after returns. |
| Profit | Sum of `profit` | Tracks the dataset’s recorded profit contribution and surfaces loss-making areas. |
| Orders | Count of distinct `order_id` | Counts transactions at order level instead of treating each order line as an order. |
| Customers | Count of distinct `customer_id` | Describes the observed customer base in the selected period; it is not a measure of active or retained customers by itself. |
| Average order value (AOV) | Total sales ÷ distinct orders | Shows average sales value per order; it can move because of order mix or order size. |
| Profit margin | Total profit ÷ total sales × 100 | Compares profit with sales on a consistent basis. Use the ratio of totals, not the average of row-level margins. |
| Average discount | Mean of line-level `discount` | Summarizes the recorded discount rate; it is not a sales-weighted discount unless explicitly recalculated that way. |
| Shipping duration | Difference between ship and order dates | Describes elapsed calendar days in the records; it is not a carrier service-level measure without promised delivery dates. |
| RFM | Recency: days since the customer’s last observed order at the dataset end; Frequency: distinct observed orders; Monetary: observed sales sum | Provides a relative customer-value/engagement view for prioritizing follow-up, not a prediction of lifetime value or churn. |
| Cohort retention | Share of customers first observed in a cohort who place an order again in a later observed month | Shows repeat purchasing in the available history; it does not confirm customer churn when no later order is observed. |

Profitability should be read alongside sales: a high-sales segment can still have low or negative profit. The discount analysis groups line items into discount bands and compares sales, profit, and aggregate margin. The bands are descriptive; discount levels may be associated with other factors such as category or product mix, so the results do not isolate the causal effect of a discount.

### Analysis choices and validation of conclusions

- **Time trends:** Aggregate by month/year to expose seasonality and compare periods. Because the history spans only four years, apparent seasonal patterns are tentative and should not be treated as a stable forecast.
- **Product and geography:** Compare sales and profit by category, subcategory, and region to distinguish volume from profitability and identify where a deeper operational review may be warranted.
- **Customer analysis:** Rank customers and summarize RFM segments to focus attention on observed high-value, frequent, or recently inactive customers. Segment names are behavioral labels based on this dataset’s scoring, not permanent customer attributes.
- **Discounts:** Compare profitability by discount band, then review category/product mix before changing pricing. The analysis is observational and is vulnerable to confounding (for example, larger discounts may be used on different products or situations).
- **Cohorts:** Assign customers to their first observed purchase month and examine subsequent observed months. Early cohorts have more time to accumulate later activity than recent cohorts; compare only equivalent cohort ages and account for incomplete periods.
- **Cross-checks:** Reconcile headline KPIs against the SQL aggregations and cleaned-data totals; confirm orders use distinct IDs; compare grouped totals across raw and cleaned files; and sanity-check trends against the underlying period/category summaries. For a dashboard release, test filter interactions and verify displayed totals under both an unfiltered view and selected slices.

These methods validate arithmetic consistency and expose patterns; they do not prove representativeness, causality, or statistical significance. The checks in `scripts/data_cleaning.py` cover data transformation consistency and grouped sales/profit totals, while business interpretation still requires context and follow-up analysis.

### Dashboard design (proposed)

The repository does not yet contain a finished interactive dashboard. A useful first page should have:

1. **KPI cards:** Sales, profit, profit margin, distinct orders, customers, and AOV, all responding consistently to filters.
2. **Trend panel:** Monthly sales and profit over time, with a year/month selector and clear date range (2011–2014).
3. **Profitability panel:** Sales versus profit by category/subcategory, plus a discount-band view that makes negative profit or margin visible.
4. **Geography and product panels:** Regional performance and ranked product/category tables, showing profit as well as sales.
5. **Customer panel:** RFM segment size and sales contribution, with cohort retention available as a separate view so customer value and repeat activity are not conflated.

Use shared date, region, market, category, and segment filters where supported by the model. The dataset does not contain a sales-channel field, so do not offer a channel filter. Include units, metric definitions, date coverage, and a note that discount and retention results are observational. Validate each dashboard measure against the SQL/Python totals before release, and retain the same order-line versus distinct-order definitions throughout.

### Recommendations to investigate

1. **Review high-discount loss areas:** Examine products and categories in the loss-making discount bands and assess margin, volume, and customer context together. Test any revised discount policy on a controlled subset and monitor both profit and sales before broad rollout.
2. **Protect profitable customer value:** Prioritize service and relevant offers for high-value RFM groups, while measuring incremental repeat orders and profit rather than campaign response alone.
3. **Test reactivation thoughtfully:** Pilot targeted outreach to customers with high recency and/or historical spend. Compare against a holdout group to distinguish campaign impact from customers who would have returned anyway.
4. **Investigate weak product/category performance:** Review product costs, returns, pricing, and assortment decisions for low- or negative-profit areas before discontinuing products or changing prices.
5. **Use shipping findings as a prompt, not an SLA score:** Compare observed transit durations with carrier commitments and delivery outcomes before making service-level or carrier decisions.

Track changes in profit, margin, repeat purchasing, and sales together. Set a baseline and evaluation period before each intervention; the historical dataset can inform hypotheses, but ongoing or experimental data is needed to measure impact.

### Dataset limitations

- The data is historical and ends in 2014; it cannot represent current customer behavior, current prices, or present-day market conditions.
- It is a transaction/order-line sample. Order lines within the same order are not independent observations, and customer identities are limited to the identifiers supplied.
- Missing postal codes are retained; geography analyses at postal-code level may therefore be incomplete. The existence of a field does not imply it is reliable at every geographic granularity.
- Profit is supplied by the source rather than recomputed from detailed costs. The dataset does not provide all operational context (such as marketing spend, inventory availability, return reasons, or promised delivery dates) needed to explain profit or fulfillment outcomes.
- There is no sales-channel field, experimental assignment, or external market context. The analysis cannot attribute changes to a promotion, channel, policy, or market event.
- RFM and cohort labels depend on the observed window and scoring choices. A customer’s first recorded order is only their first observed order in this file, and absence of a later order is not proof of churn.
- Aggregated patterns can conceal product, customer, or regional mix effects. Treat findings as hypotheses to investigate, not causal claims or guaranteed forecasts.

## Processed Data Outputs

The following datasets are available in `data/processed/`:

| File | Description |
|---|---|
| `superstore_cleaned.csv` | Cleaned and validated Superstore dataset |
| `customer_rfm_segments.csv` | Customer-level RFM scores and segment assignments |
| `customer_segment_summary.csv` | Aggregated performance metrics for the nine customer segments |

## Week 4 – Interactive Dashboard, Final Report & Presentation

<badge>Planned</badge>

**Engineering Focus:** Communicate commercial performance through an interactive business intelligence solution.

**Planned implementation:**

- Develop an interactive dashboard using Power BI or Tableau.
- Integrate KPI cards for sales, profit, orders, and profitability.
- Visualize revenue and profit trends.
- Develop product and category performance rankings.
- Compare regional business performance.
- Implement filters for date, region, market, product category, and customer segment where available. The dataset has no sales-channel field.
- Include indicators for declining sales and low profitability.
- Validate dashboard calculations against cleaned analytical datasets.
- Prepare final analytical documentation and presentation.

**SQL Integration:**

The repository includes MySQL queries for core KPIs, sales performance, customer analysis, and discount analysis. Reconcile dashboard measures with these queries and the cleaned dataset before release.

**Expected Deliverables:**

- Interactive Power BI or Tableau dashboard.
- Final analytical report with visualizations and recommendations.
- Documented code and GitHub repository.
- Final project presentation.

## Team Collaboration & Version Control

The project is being developed collaboratively by a team of five members using Git and GitHub.

Dedicated branches were created to organize individual responsibilities:

| Branch | Responsibility |
|---|---|
| `member-1/data-docs` | Data documentation |
| `member-2/data-cleaning` | Data cleaning and preprocessing |
| `member-3/eda` | Exploratory data analysis |
| `member-4/kpi-sql` | KPI development and SQL analysis |
| `member-5/dashboard` | Dashboard development |

Feature branches, commits, and GitHub collaboration help maintain a structured development workflow and track project progress.

## Future Scope

Beyond the initial four-week development plan, potential enhancements include:

- Automated data refresh and reporting.
- Advanced sales forecasting.
- Customer churn prediction.
- Product demand analysis.
- Profitability optimization.
- Customer lifetime value estimation.
- Automated business performance alerts.

## Conclusion

The project aims to bridge the gap between raw transactional data and meaningful business decisions.

The first two weeks established a reliable data foundation and generated insights into sales performance, discount profitability, shipping efficiency, customer value, and retention behavior.

The upcoming phases will focus on deeper trend interpretation, structured SQL analysis, and interactive business intelligence, ultimately transforming the analytical work into a practical business performance dashboard.

---

## Data Attribution

The project uses a Superstore dataset sourced from Kaggle. Dataset usage is subject to the original source's licensing and attribution requirements.