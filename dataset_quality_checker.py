import pandas as pd

# Load the dataset
df = pd.read_csv("ai_training_data.csv")

print("===== AI DATASET QUALITY REPORT =====")

# Total records
print("\nTotal records:", len(df))

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Duplicate image IDs
if "image_id" in df.columns:
    print("Duplicate image IDs:", df["image_id"].duplicated().sum())

# Category distribution
if "category" in df.columns:
    print("\nCategory distribution:")
    print(df["category"].value_counts())


# Annotation consistency check
expected_categories = {
    "cat": "animal",
    "dog": "animal",
    "bird": "animal",
    "car": "vehicle",
    "bus": "vehicle"
}

expected = df["label"].astype("string").str.strip().str.lower().map(expected_categories)
actual = df["category"].astype("string").str.strip().str.lower()

invalid = expected.isna() | (actual != expected)

print("\nAnnotation consistency:")
print("Incorrect or unknown combinations:", int(invalid.sum()))

if invalid.any():
    print(df.loc[invalid, ["image_id", "label", "category"]])
else:
    print("All label-category combinations are valid.")

# Overall quality status
missing_total = int(df.isnull().sum().sum())
duplicate_rows = int(df.duplicated().sum())
duplicate_ids = int(df["image_id"].duplicated().sum())
invalid_count = int(invalid.sum())

if (missing_total == 0 and duplicate_rows == 0
        and duplicate_ids == 0 and invalid_count == 0):
    print("\nOVERALL STATUS: PASS")
else:
    print("\nOVERALL STATUS: REVIEW REQUIRED")

# Generate quality report
report_status = (
    "PASS"
    if missing_total == 0
    and duplicate_rows == 0
    and duplicate_ids == 0
    and invalid_count == 0
    else "REVIEW REQUIRED"
)

report = f"""
===== AI TRAINING DATASET QUALITY REPORT =====

Total records: {len(df)}

Missing values:
{df.isnull().sum().to_string()}

Duplicate rows: {duplicate_rows}
Duplicate image IDs: {duplicate_ids}

Category distribution:
{df['category'].value_counts().to_string()}

Annotation consistency:
Incorrect or unknown combinations: {invalid_count}

OVERALL STATUS: {report_status}

===== END OF REPORT =====
"""

with open("dataset_quality_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nQuality report saved as dataset_quality_report.txt")
print("\n===== QUALITY CHECK COMPLETED =====")