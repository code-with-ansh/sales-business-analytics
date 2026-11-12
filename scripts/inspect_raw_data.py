
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "superstore_dataset2011-2015.csv"

# Load raw dataset without modifying the original file
df = pd.read_csv(DATA_PATH, encoding="cp1252")

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
missing_report = pd.DataFrame({
    "Missing Count": missing,
    "Missing Percentage": (missing / len(df) * 100).round(2)
})
print(missing_report[missing_report["Missing Count"] > 0].to_string())

print("\n--- Exact Duplicate Rows ---")
print(f"Duplicate rows: {df.duplicated().sum():,}")

print("\n--- Numeric Column Summary ---")
print(df.describe().to_string())

print("\n--- First 5 Rows ---")
print(df.head().to_string(index=False))

print("\n--- Inspection Complete ---")
