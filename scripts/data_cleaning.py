from pathlib import Path

import pandas as pd
from pandas.api.types import is_string_dtype


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "superstore_dataset2011-2015.csv"
)
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
CLEAN_PATH = OUTPUT_DIR / "superstore_cleaned.csv"
TOLERANCE = 0.01


def inspect_raw_data() -> None:
    """Print a profile of the unmodified raw dataset."""
    df = pd.read_csv(RAW_PATH, encoding="cp1252")

    print("=" * 60)
    print("RAW DATASET INSPECTION REPORT")
    print("=" * 60)
    print(f"\nDataset shape: {df.shape[0]:,} rows x {df.shape[1]} columns")
    print("\n--- Column Names ---")
    print(df.columns.tolist())
    print("\n--- Data Types ---")
    print(df.dtypes.to_string())

    print("\n--- Missing Values ---")
    missing = df.isnull().sum()
    missing_report = pd.DataFrame(
        {
            "Missing Count": missing,
            "Missing Percentage": (missing / len(df) * 100).round(2),
        }
    )
    print(
        missing_report[missing_report["Missing Count"] > 0].to_string()
    )

    print("\n--- Exact Duplicate Rows ---")
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print("\n--- Numeric Column Summary ---")
    print(df.describe().to_string())
    print("\n--- First 5 Rows ---")
    print(df.head().to_string(index=False))
    print("\n--- Inspection Complete ---")


def parse_mixed_date_column(
    series: pd.Series,
    column_name: str,
) -> pd.Series:
    """Parse supported day-first date strings, raising on invalid patterns."""
    values = series.astype("string").str.strip()
    parsed = pd.Series(pd.NaT, index=series.index, dtype="datetime64[ns]")

    slash_mask = values.str.contains("/", regex=False, na=False)
    hyphen_mask = values.str.contains("-", regex=False, na=False)
    other_mask = values.notna() & ~(slash_mask | hyphen_mask)

    if other_mask.any():
        examples = values.loc[other_mask].drop_duplicates().head(10).tolist()
        raise ValueError(
            f"{column_name}: unsupported date patterns found: {examples}"
        )

    if slash_mask.any():
        parsed.loc[slash_mask] = pd.to_datetime(
            values.loc[slash_mask],
            format="%d/%m/%Y",
            errors="coerce",
        )

    if hyphen_mask.any():
        parsed.loc[hyphen_mask] = pd.to_datetime(
            values.loc[hyphen_mask],
            format="%d-%m-%Y",
            errors="coerce",
        )

    invalid_mask = values.notna() & parsed.isna()
    if invalid_mask.any():
        examples = values.loc[invalid_mask].drop_duplicates().head(10).tolist()
        raise ValueError(
            f"{column_name}: {int(invalid_mask.sum())} value(s) could not be "
            f"parsed. Examples: {examples}"
        )

    return parsed


def clean_data() -> None:
    """Standardize, validate, and save the processed transaction dataset."""
    df = pd.read_csv(RAW_PATH, encoding="cp1252")
    original_rows = len(df)

    print("\nDATA CLEANING")
    print("Original shape:", df.shape)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )

    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()
    print("Exact duplicates removed:", duplicate_count)

    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns
    for column in text_columns:
        df[column] = df[column].str.strip()

    categorical_columns = [
        "ship_mode",
        "segment",
        "city",
        "state",
        "country",
        "market",
        "region",
        "category",
        "sub_category",
        "order_priority",
    ]
    for column in categorical_columns:
        if column in df.columns:
            df[column] = df[column].str.lower()

    missing_postal_codes = int(df["postal_code"].isna().sum())
    print("Missing postal codes preserved:", missing_postal_codes)
    print("Remaining missing values:", int(df.isna().sum().sum()))
    print("Sales <= 0:", int((df["sales"] <= 0).sum()))
    print("Quantity <= 0:", int((df["quantity"] <= 0).sum()))
    print(
        "Discount outside 0 to 1:",
        int(((df["discount"] < 0) | (df["discount"] > 1)).sum()),
    )
    print("Negative shipping costs:", int((df["shipping_cost"] < 0).sum()))
    print("Negative-profit rows preserved:", int((df["profit"] < 0).sum()))

    df["order_date"] = parse_mixed_date_column(
        df["order_date"], "order_date"
    )
    df["ship_date"] = parse_mixed_date_column(
        df["ship_date"], "ship_date"
    )

    print("Missing order dates:", int(df["order_date"].isna().sum()))
    print("Missing ship dates:", int(df["ship_date"].isna().sum()))

    invalid_shipping_order = df["ship_date"] < df["order_date"]
    invalid_shipping_count = int(invalid_shipping_order.sum())
    print("Ship dates before order dates:", invalid_shipping_count)

    if invalid_shipping_count:
        examples = df.loc[
            invalid_shipping_order, ["order_date", "ship_date"]
        ].head(10)
        raise ValueError(
            "Found shipping dates earlier than order dates. Examples:\n"
            f"{examples.to_string(index=False)}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(
        CLEAN_PATH,
        index=False,
        encoding="utf-8-sig",
        date_format="%Y-%m-%d",
    )

    print("Final shape:", df.shape)
    print("Rows removed:", original_rows - len(df))
    print("Saved to:", CLEAN_PATH)


def validate_cleaned_data() -> None:
    """Check basic expectations for the saved cleaned dataset."""
    raw = pd.read_csv(RAW_PATH, encoding="cp1252")
    clean = pd.read_csv(CLEAN_PATH, encoding="utf-8-sig")

    print("\nCLEANED DATA VALIDATION")
    print("-" * 50)

    checks = {
        "Expected row count preserved": len(clean) == len(raw),
        "Expected 24 columns": len(clean.columns) == 24,
        "No exact duplicate rows": not clean.duplicated().any(),
        "No missing values outside postal_code": (
            int(clean.drop(columns=["postal_code"]).isna().sum().sum()) == 0
        ),
        "Dates stored as strings": (
            is_string_dtype(clean["order_date"].dtype)
            and is_string_dtype(clean["ship_date"].dtype)
        ),
    }

    print("Shape:", clean.shape)
    print("Missing postal codes:", clean["postal_code"].isna().sum())
    print("Negative-profit rows:", (clean["profit"] < 0).sum())
    print("\nCheck results:")
    for label, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {label}")

    if not all(checks.values()):
        raise SystemExit("\nValidation failed. Review the cleaning pipeline.")

    print("\nAll validation checks passed.")


def load_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load raw and cleaned datasets and normalize raw column names."""
    raw = pd.read_csv(RAW_PATH, encoding="cp1252")
    clean = pd.read_csv(CLEAN_PATH, encoding="utf-8-sig")
    raw.columns = (
        raw.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )
    return raw, clean


def compare_kpis(
    raw: pd.DataFrame,
    clean: pd.DataFrame,
) -> bool:
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
    return bool(result["Match"].all())


def compare_grouped_performance(
    raw: pd.DataFrame,
    clean: pd.DataFrame,
    column: str,
) -> bool:
    """Compare sales and profit grouped by a categorical column."""
    results = []

    for df, label in [(raw, "Raw"), (clean, "Cleaned")]:
        temp = df.copy()
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
    return bool(passed)


def compare_raw_and_cleaned() -> None:
    """Reconcile baseline and grouped metrics, exiting if a check fails."""
    raw, clean = load_datasets()

    print("\nRAW DATA VS CLEANED DATA COMPARISON")
    print("=" * 65)
    baseline_passed = compare_kpis(raw, clean)
    group_checks = {
        column: compare_grouped_performance(raw, clean, column)
        for column in ["category", "sub_category", "region"]
    }

    print("\nFINAL VALIDATION")
    print("-" * 65)
    print(f"{'PASS' if baseline_passed else 'FAIL'}: Baseline metrics")
    for column, passed in group_checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {column}")

    if not baseline_passed or not all(group_checks.values()):
        raise SystemExit("\nComparison failed. Investigate the differences.")

    print("\nAll comparison checks passed.")
    print("Date parsing remains outside this comparison.")


def main() -> None:
    """Run inspection, cleaning, validation, and comparison in order."""
    inspect_raw_data()
    clean_data()
    validate_cleaned_data()
    compare_raw_and_cleaned()


if __name__ == "__main__":
    main()
