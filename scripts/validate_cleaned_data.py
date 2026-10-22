
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "superstore_dataset2011-2015.csv"
CLEAN_PATH = PROJECT_ROOT / "data" / "processed" / "superstore_cleaned.csv"


def main():
    raw = pd.read_csv(RAW_PATH, encoding="cp1252")
    clean = pd.read_csv(CLEAN_PATH, encoding="utf-8-sig")

    print("CLEANED DATA VALIDATION")
    print("-" * 50)

    checks = {
        "Expected row count preserved": len(clean) == len(raw),
        "Expected 24 columns": len(clean.columns) == 24,
        "No exact duplicate rows": not clean.duplicated().any(),
        "No missing values outside postal_code": (
            int(clean.drop(columns=["postal_code"]).isna().sum().sum()) == 0
        ),
        "Dates preserved as original strings": (
            clean["order_date"].dtype == "object"
            and clean["ship_date"].dtype == "object"
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


if __name__ == "__main__":
    main()
