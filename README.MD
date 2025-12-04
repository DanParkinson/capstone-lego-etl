## Project Overview

This project ingests a LEGO dataset from Kaggle, cleans and transforms it into well-structured relational tables, and exposes the result through a Streamlit dashboard for interactive exploration.

Workflow Summary:

Extract

- Download raw dataset automatically via Kaggle API

- If dataset already exists locally, avoid re-download

- Log ETL progress & performance

- Validate Raw

- Check column schema health

- Warn on unexpected columns

- Raise on missing expected columns

Transform

- Clean numeric fields → convert to numeric, impute, split ages

- Clean text fields → null handling, dtype enforcement, lowercasing

- Remove corrupt rows and duplicates using composite key (prod_id, country)

- Validate cleaned schema before loading

Load

- Convert dataset into relational star-schema style tables

- Create output CSVs under /data/output

- Surrogate keys generated where appropriate

Explore

- Streamlit UI to present the project

- Load relational tables for browsing

- Cached reads for performance

---

## Testing Summary

| Area               | Coverage                          |
| ------------------ | --------------------------------- |
| Kaggle extraction  | Authentication + file detection   |
| CSV loading        | DataFrame returned correctly      |
| Raw validation     | Column schema enforcement         |
| Numeric cleaning   | dtype + parsing + rounding        |
| Text cleaning      | Null handling + dtype + lowercase |
| Duplicate cleaning | Multi-country allowed             |
| Load utilities     | Writes correct table structure    |

Testing focused on reliability of critical logic rather than blanket coverage.

---

[docs\erd.png]

---

## Running the ETL

Install dependencies:
pip install -r requirements.txt

Authenticate with Kaggle:
kaggle login

Run pipeline:
python src/run_etl.py

---

##  Launch the Streamlit App

streamlit run homepage.py

## Future Enhancements

- Incremental ETL updates
- PostgreSQL warehouse integration
- Data visualization dashboards
- CI/CD pipeline for automated testing
- Automated documentation generation