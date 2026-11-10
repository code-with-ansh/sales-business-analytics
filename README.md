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

**Dataset:** Superstore Dataset (2011–2015)
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
| SQL | Planned structured querying and KPI analysis |
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
- Created reusable data cleaning and validation scripts.
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

## Processed Data Outputs

The following datasets are available in `data/processed/`:

| File | Description |
|---|---|
| `superstore_cleaned.csv` | Cleaned and validated Superstore dataset |
| `customer_rfm_segments.csv` | Customer-level RFM scores and segment assignments |
| `customer_segment_summary.csv` | Aggregated performance metrics for the nine customer segments |

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

## Week 4 – Interactive Dashboard, Final Report & Presentation

<badge>Planned</badge>

**Engineering Focus:** Communicate commercial performance through an interactive business intelligence solution.

**Planned implementation:**

- Develop an interactive dashboard using Power BI or Tableau.
- Integrate KPI cards for sales, profit, orders, and profitability.
- Visualize revenue and profit trends.
- Develop product and category performance rankings.
- Compare regional business performance.
- Implement filters for date, region, product category, customer segment, and sales channel where available.
- Include indicators for declining sales and low profitability.
- Validate dashboard calculations against cleaned analytical datasets.
- Prepare final analytical documentation and presentation.

**SQL Integration:**

Structured SQL queries will be developed for business KPI calculations, aggregations, and analytical validation.

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

## License

A project license has not yet been specified. Dataset usage remains subject to the original source's terms and license.
