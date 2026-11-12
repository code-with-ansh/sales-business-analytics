from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "superstore_dataset2011-2015.csv"
)
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_PATH = OUTPUT_DIR / "superstore_cleaned.csv"


def parse_mixed_date_column(series: pd.Series, column_name: str) -> pd.Series:
    """
    Parse source date strings using explicit, day-first formats:
    - DD/MM/YYYY for slash-separated dates
    - DD-MM-YYYY for hyphen-separated dates

    Raises an error if any non-empty value cannot be parsed.
    """
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


def main():
    # 1. Load raw data
    df = pd.read_csv(RAW_PATH, encoding="cp1252")
    original_rows = len(df)

    print("Original shape:", df.shape)

    # 2. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )

    # 3. Remove exact duplicate rows
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()

    print("Exact duplicates removed:", duplicate_count)

    # 4. Trim whitespace from text columns
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # 5. Standardize categorical values to lowercase
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

    # 6. Preserve missing postal codes
    missing_postal_codes = int(df["postal_code"].isna().sum())

    # 7. Report numeric quality checks
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

    # 8. Parse dates using the verified day-first convention.
    # Slash dates use DD/MM/YYYY; hyphen dates use DD-MM-YYYY.
    df["order_date"] = parse_mixed_date_column(df["order_date"], "order_date")
    df["ship_date"] = parse_mixed_date_column(df["ship_date"], "ship_date")

    print("Missing order dates:", int(df["order_date"].isna().sum()))
    print("Missing ship dates:", int(df["ship_date"].isna().sum()))

    # Shipping dates should not precede order dates.
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

    # 9. Save processed data. Dates are written as YYYY-MM-DD.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig",
        date_format="%Y-%m-%d",
    )

    print("Final shape:", df.shape)
    print("Rows removed:", original_rows - len(df))
    print("Saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
