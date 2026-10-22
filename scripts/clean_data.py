
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

    # 8. Keep dates as original strings for now
    # Date parsing will be handled separately after format verification.

    # 9. Save processed data
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print("Final shape:", df.shape)
    print("Rows removed:", original_rows - len(df))
    print("Saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
