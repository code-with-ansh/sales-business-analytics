# Sales & Business Performance Analytics Dashboard

An interactive business intelligence project designed to analyze sales data and generate actionable insights into revenue, profitability, customer behavior, product performance, and regional trends. The project combines exploratory data analysis (EDA), SQL-based analysis, and dashboard visualization to support data-driven business decisions.

## 📌 Project Overview

Businesses generate large amounts of sales data, but raw data alone does not explain which products are profitable, which markets perform well, or where business improvements are needed.

This project aims to transform raw sales data into meaningful business insights through data analysis, key performance indicators (KPIs), and interactive visualizations.

The project is being developed collaboratively, with different team members responsible for data documentation, data cleaning, exploratory data analysis, SQL-based KPIs, and dashboard development.

## 🎯 Project Objectives

- Analyze sales, profit, quantity, and order performance.
- Identify high-performing and low-performing product categories.
- Understand customer purchasing patterns.
- Compare performance across markets, regions, and countries.
- Examine sales trends over time.
- Investigate the relationship between discounts and profitability.
- Develop business KPIs to support management decisions.
- Present insights through an interactive analytics dashboard.

## 📊 Dataset

The project uses the Superstore sales dataset covering the period 2011–2015.

**Raw dataset:** `superstore_dataset2011-2015.csv`

**Location:** `data/raw/`

The dataset contains transaction-level information, including:

- Order and shipping dates
- Customer and product details
- Product categories and sub-categories
- Sales, quantity, discount, and profit
- Market, region, country, state, and city
- Shipping mode and order priority

The dataset is used for exploratory analysis, data quality assessment, KPI development, and business performance evaluation.

## 🛠️ Technologies Used

- **Python:** Data analysis and exploratory data analysis
- **Jupyter Notebook:** Interactive analysis and documentation
- **Pandas and NumPy:** Data manipulation and numerical analysis
- **Matplotlib and Seaborn:** Data visualization
- **SQL:** Business queries and KPI calculations
- **Power BI:** Business intelligence dashboard development
- **Git and GitHub:** Version control and team collaboration

## 📁 Project Structure

```text
sales-business-analytics/
│
├── dashboard/       # Dashboard development files
├── data/
│   ├── raw/         # Original dataset
│   └── processed/   # Cleaned and transformed data
├── docs/            # Project documentation
├── notebooks/       # Jupyter notebooks for analysis
├── reports/         # Analysis reports and exported results
├── screenshots/     # Dashboard and analysis screenshots
├── sql/             # SQL queries and KPI calculations
├── .gitignore
└── README.md
```

## 🔍 Exploratory Data Analysis

The EDA stage examines the dataset to understand its structure, quality, and business patterns.

The comprehensive raw-data analysis is documented in:

`notebooks/eda_raw_data_complete.ipynb`

The notebook covers:

1. Dataset loading and structural overview
2. Missing-value and duplicate-record analysis
3. Date parsing and consistency validation
4. Descriptive statistics and numerical distributions
5. Overall business KPI calculations
6. Sales and profit analysis by category and sub-category
7. Market, regional, and country-level comparisons
8. Customer and product performance
9. Monthly and yearly sales and profit trends
10. Discount and profitability analysis

Tables, charts, calculations, and analysis outputs are included in the notebook.

## 📈 Key Performance Indicators

The project examines business metrics such as:

| KPI | Description |
|---|---|
| Total Sales | Total sales value across the dataset |
| Total Profit | Overall profit generated |
| Total Quantity | Total units sold |
| Total Orders | Number of distinct orders |
| Total Customers | Number of distinct customers |
| Average Order Value | Average sales value per order |
| Profit Margin | Profit as a percentage of sales |

These metrics provide a foundation for comparing business performance across products, customers, markets, and time periods.

## 👥 Team Workflow

The project is developed using Git and GitHub with separate branches for different responsibilities.

| Branch | Responsibility |
|---|---|
| `member-1/data-docs` | Data documentation |
| `member-2/data-cleaning` | Data cleaning and preparation |
| `member-3/eda` | Exploratory data analysis |
| `member-4/kpi-sql` | SQL queries and KPI development |
| `member-5/dashboard` | Dashboard development |

Team members develop their work on their assigned branches and use commits to record meaningful changes. Pull requests can be used to review and integrate work into the main branch.

## 🚀 Getting Started

### Prerequisites

Install Python, Git, and Jupyter Notebook or Visual Studio Code with the Python and Jupyter extensions.

### 1. Clone the repository

```bash
git clone https://github.com/code-with-ansh/sales-business-analytics.git
```

### 2. Navigate to the project directory

```bash
cd sales-business-analytics
```

### 3. Install the analysis dependencies

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Open the EDA notebook

```bash
jupyter notebook notebooks/eda_raw_data_complete.ipynb
```

Alternatively, open the repository in VS Code and select the notebook.

### 5. Verify the dataset location

Ensure that the raw CSV file exists at:

`data/raw/superstore_dataset2011-2015.csv`

Run the notebook cells sequentially to reproduce the analysis.

## 💡 Expected Outcomes

The project aims to provide:

- A structured understanding of the sales dataset
- Improved visibility into revenue and profitability
- Identification of product and market performance patterns
- Insights into customer behavior and sales trends
- Reusable KPIs for business reporting
- An interactive dashboard for exploring business performance

## 🔮 Future Scope

Potential enhancements include:

- Additional interactive filters and drill-downs
- Advanced customer segmentation
- Sales forecasting and trend prediction
- Profitability and discount optimization
- Automated data refresh and reporting
- Additional performance metrics and comparative analysis

## Project Status

### Completed
- Repository setup and project structure
- Raw Superstore dataset integration
- Data cleaning and preprocessing
- Data quality checks and validation
- Date standardization and validation
- Raw vs. cleaned dataset comparison
- Overall business KPI analysis
- Category and subcategory analysis
- Regional and market performance analysis
- Customer and product analysis

### Time-Based Sales and Business Performance Analysis
- Yearly sales, profit and growth analysis
- Quarterly sales and profit analysis
- Year-wise quarterly comparisons
- Monthly sales and profit trends
- Month-wise year-over-year growth
- Monthly seasonality analysis
- Average monthly sales, profit and order value

### Shipping Performance Analysis
- Overall shipping performance KPIs
- Shipping mode performance comparison
- Year-wise shipping performance analysis
- Month-wise shipping performance analysis
- Shipping duration distribution
- Delivery speed classification
- Shipping cost and delivery duration visualizations
- Business insights and recommendations

### Discount Impact and Profitability Analysis
- Discount distribution and frequency analysis
- Discount range vs. profitability analysis
- Profit margin comparison across discount ranges
- Category-wise discount impact analysis
- Subcategory-wise profitability analysis
- Furniture-specific discount analysis
- Discount impact visualizations
- Identification of loss-making products and discount ranges
- Business insights and pricing recommendations

### Customer Segmentation and RFM Analysis
- Customer-level Recency, Frequency and Monetary (RFM) calculation
- Quintile-based RFM scoring
- Customer segmentation into 9 behavioral groups
- Champions, Loyal, At Risk and Lost customer identification
- Customer segment revenue and purchase frequency analysis
- Customer revenue concentration and Pareto analysis
- Identification of customers contributing 80% of revenue
- Customer segment visualizations
- Segment-specific business strategies and recommendations
- Export of customer-level RFM and segment summary datasets

### Customer Cohort & Retention Analysis

- Identified customer acquisition cohorts based on first observed purchase month.
- Developed a monthly cohort retention matrix covering 48 months.
- Created cohort retention heatmaps and monthly retention trend visualizations.
- Calculated average, median and weighted customer retention.
- Compared strongest and weakest acquisition cohorts.
- Analyzed retention performance across acquisition years (2011–2014).
- Identified retention improvement opportunities through cohort-level insights.

### Processed Data Outputs

The following analytical datasets are available in `data/processed/`:

- `superstore_cleaned.csv` – Cleaned and validated Superstore dataset containing 51,290 records and 24 columns.
- `customer_rfm_segments.csv` – Customer-level RFM scores and behavioral segment assignments.
- `customer_segment_summary.csv` – Aggregated performance metrics for the nine customer segments.

### Project Progress & Roadmap

#### Week 1 & Week 2 – Completed

- Dataset exploration, profiling and data quality assessment.
- Data cleaning, date standardization and validation.
- Overall business KPI analysis.
- Category, subcategory, regional and customer performance analysis.
- Time-based sales and profit analysis.
- Shipping performance and delivery duration analysis.
- Discount impact and profitability analysis.
- RFM-based customer segmentation into nine behavioral groups.
- Customer revenue concentration and Pareto analysis.
- Customer cohort and retention analysis.
- Export and version control of processed analytical datasets.

#### Week 3 – Planned: Trend Analysis & Business Insights

- Monthly, quarterly and yearly trend analysis.
- Current-period versus previous-period comparisons.
- Performance investigation across products, categories, regions and customer segments.
- Seasonality analysis where sufficient historical data is available.
- Identification of significant business trends and unusual transactions.
- Development of evidence-based business recommendations.
- Supporting visualizations using Matplotlib and Seaborn.

**Expected Deliverables:**
- Trend analysis notebook.
- Supporting visualizations.
- Significant business findings.
- Draft business recommendations.

#### Week 4 – Planned: Interactive Dashboard & Final Documentation

- SQL-based KPI analysis and structured business queries.
- Interactive dashboard development using Power BI or Tableau.
- KPI cards for sales, profit, orders and profitability.
- Revenue and profit trend visualizations.
- Product, category and regional performance comparisons.
- Filters for date, region, product category, customer segment and sales channel where available.
- Dashboard validation against cleaned analytical datasets.
- Preparation of the final analytical report and presentation.

**Expected Deliverables:**
- Interactive dashboard (`.pbix`, Tableau workbook or accessible export).
- Final analytical report with visualizations and recommendations.
- Documented source code and GitHub repository.
- Final project presentation.

---

## Current Project Status

The project has completed its initial data preparation and exploratory analytics phases. The next stages will focus on deeper trend interpretation, SQL-based analysis, interactive business intelligence and final reporting.


## 📄 Data Attribution

The project uses a Superstore dataset sourced from Kaggle. Refer to the original dataset listing for attribution and licensing details.

## 📜 License

A project license has not yet been specified. Dataset usage remains subject to the original source's terms and license.