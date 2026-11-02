# AI Training Dataset Quality Checker

## Project Overview
A beginner-friendly Python project that checks the quality and consistency of AI training datasets using Pandas.

The project uses a sample image-annotation dataset containing image IDs, labels, and categories.

## Features
- Counts total dataset records.
- Detects missing values.
- Identifies duplicate rows.
- Detects duplicate image IDs.
- Checks label-category consistency.
- Displays category distribution.
- Generates an automatic quality report.
- Displays an overall PASS or REVIEW REQUIRED status.

## Technologies Used
- Python 3.10
- Pandas 2.3.3
- CSV datasets

## Project Structure
```text
ai-training-dataset-quality-checker/
├── ai_training_data.csv
├── dataset_quality_checker.py
├── dataset_quality_report.txt
└── README.md
```

## How to Run

1. Install Python.
2. Install Pandas:

```bash
pip install pandas
```

3. Run the program:

```bash
python dataset_quality_checker.py
```

4. View the generated `dataset_quality_report.txt` file.

## Sample Dataset
The practice dataset contains five image records in two categories:
- Animal: 3 records
- Vehicle: 2 records

## Learning Outcomes
- Python programming fundamentals
- Pandas DataFrame operations
- Data validation
- Missing-value detection
- Duplicate detection
- Annotation quality checks
- Automated report generation

## Important Note
The dataset is a small practice dataset. Annotation consistency is checked against predefined label-category rules; the program does not independently inspect images.

## Author
Jagadish Kumar