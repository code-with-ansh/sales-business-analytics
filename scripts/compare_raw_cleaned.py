
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = (
    PROJECT_ROOT / "data" / "raw" / "superstore_dataset2011-2015.csv"
)
CLEAN_PATH = (
    PROJECT_ROOT / "data" / "processed" / "superstore_cleaned.csv"
)

TOLERANCE = 0.01


def load_datasets():
    """Load raw and cleaned datasets and normalize raw column names."""
    raw = pd.read_csv(RAW_PATH, encoding="cp1252")
    clean = pd.read_csv(CLEAN_PATH, encoding="utf-8-sig")

    raw.columns = (
        raw.columns.str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )

    return raw, clean


def compare_kpis(raw, clean):
    """Compare baseline metrics between raw and cleaned datasets."""
    metrics = {
        "Rows": (len(raw), len(clean)),
        "Columns": (len(raw.columns), len(clean.columns)),
        "Total sales": (raw["sales"].sum(), clean["sales"].sum()),
        "Total profit": (raw["profit"].sum(), clean["profit"].sum()),
        "Total quantity": (
            raw["quantity"].sum(),
            clean["quantity"].sum(),
        ),
        "Unique orders": (
            raw["order_id"].nunique(),
            clean["order_id"].nunique(),
        ),
        "Unique customers": (
            raw["customer_id"].nunique(),
            clean["customer_id"].nunique(),
        ),
        "Missing postal codes": (
            raw["postal_code"].isna().sum(),
            clean["postal_code"].isna().sum(),
        ),
        "Exact duplicate rows": (
            raw.duplicated().sum(),
            clean.duplicated().sum(),
        ),
    }

    result = pd.DataFrame(metrics, index=["Raw", "Cleaned"]).T
    result["Match"] = [
        abs(raw_value - clean_value) < TOLERANCE
        if isinstance(raw_value, (int, float))
        and isinstance(clean_value, (int, float))
        else raw_value == clean_value
        for raw_value, clean_value in zip(
            result["Raw"], result["Cleaned"]
        )
    ]

    print("\nRAW VS CLEANED: BASELINE COMPARISON")
    print("-" * 65)
    print(result.to_string())

    return result["Match"].all()


def compare_grouped_performance(raw, clean, column):
    """Compare sales and profit grouped by a categorical column."""
    results = []

    for df, label in [(raw, "Raw"), (clean, "Cleaned")]:
        temp = df.copy()

        # Normalize capitalization and surrounding whitespace.
        temp[column] = (
            temp[column]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        summary = (
            temp.groupby(column, dropna=False)
            .agg(
                sales=("sales", "sum"),
                profit=("profit", "sum"),
            )
            .reset_index()
        )
        summary["dataset"] = label
        results.append(summary)

    combined = pd.concat(results, ignore_index=True)

    pivot = combined.pivot_table(
        index=column,
        columns="dataset",
        values=["sales", "profit"],
        aggfunc="sum",
        fill_value=0,
    )

    # Ensure expected dataset columns exist.
    for metric in ["sales", "profit"]:
        for dataset in ["Raw", "Cleaned"]:
            if (metric, dataset) not in pivot.columns:
                pivot[(metric, dataset)] = 0.0

    sales_diff = (
        pivot[("sales", "Raw")] - pivot[("sales", "Cleaned")]
    ).abs()
    profit_diff = (
        pivot[("profit", "Raw")] - pivot[("profit", "Cleaned")]
    ).abs()

    max_sales_diff = sales_diff.max()
    max_profit_diff = profit_diff.max()

    passed = (
        max_sales_diff < TOLERANCE
        and max_profit_diff < TOLERANCE
    )

    print(f"\n{column.upper()}: GROUPED COMPARISON")
    print("-" * 65)
    print("Maximum absolute sales difference:", max_sales_diff)
    print("Maximum absolute profit difference:", max_profit_diff)
    print(f"{'PASS' if passed else 'FAIL'}: {column} totals match")

    return passed


def main():
    raw, clean = load_datasets()

    print("RAW VS CLEANED DATA COMPARISON")
    print("=" * 65)

    baseline_passed = compare_kpis(raw, clean)

    group_checks = {}
    for column in ["category", "sub_category", "region"]:
        group_checks[column] = compare_grouped_performance(
            raw, clean, column
        )

    print("\nFINAL VALIDATION")
    print("-" * 65)
    print(f"{'PASS' if baseline_passed else 'FAIL'}: Baseline metrics")

    for column, passed in group_checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {column}")

    if not baseline_passed or not all(group_checks.values()):
        raise SystemExit(
            "\nComparison failed. Investigate the differences."
        )

    print("\nAll comparison checks passed.")
    print("Date parsing remains outside this comparison.")


if __name__ == "__main__":
    main()
