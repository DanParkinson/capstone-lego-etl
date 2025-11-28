# EPICS

## (1) Data Acquisition, Extraction & Validation

### US1 — Fetch LEGO Dataset via Kaggle API
- As a developer, I want to fetch the LEGO dataset automatically from Kaggle if the raw file does not exist,
- So that the ETL pipeline is reproducible.

#### Acceptance Criteria
- [x] Raw CSV downloads if missing
- [x] Appropriate log entry created
- [x] If the file already exists, ETL skips download and logs it
- [x] Data loads into a pandas DataFrame

#### Tests
- [ ] extract_lego.py
  - [x] test_extract_lego_data_returns_dataframe
- [ ] kaggle_downloader.py
  - [x] test_kaggle_downloader_authentication
  - [x] test_kaggle_downloader_download_called
  - [x] test_kaggle_downloader_returned_csv_path
  - [x] test_kaggle_downloader_return_error_for_no_csv
- [ ] extract.py
  - [x] test_extract_data_returns_dataframe

### US2 — Load Raw CSV into DataFrame
- As a developer, I want to load the raw CSV into a DataFrame,
- So that I can inspect and validate the raw dataset.

#### Acceptance Criteria
- [x] DataFrame loads without errors
- [x] Column names match expected structure
- [x] Data types logged for reference
- [x] Missing values summary logged

#### Tests
- [] src/utils/raw_validation.py
  - [x] test_validate_raw_lego_data_structure_ok
  - [x] test_validate_raw_lego_data_structure_fails

---

## (2) Data Cleaning and Transformation

### US3 — Clean Numeric Columns
- As a developer, I want to convert numeric-like columns into numeric types,
- So that aggregations and visualisations work correctly.

#### Acceptance Criteria
- [ ] Convert relevent to properly numeric columns
  - [x] ages -> min age, max age - floats, non missing
  - [x] list price - Rounded float
  - [x] num_reviews - int - Nan -> 0
  - [x] Piece_count - int
  - [x] play_star_rating - Don't need to clean
  - [x] prod_id - int
  - [x] star_rating - Dont need to clean
  - [x] val_star_rating - Dont need to clean
- [x] Invalid numeric values become NaN
- [x] No string values remain in numeric columns

#### Tests
- [ ] src/transform/transform_numeric.py
  - [ ] test_age
    - [x] test_age_range
    - [x] test_age_plus
    - [x] test_age_fractional_values
    - [ ] test_age_invalid
  - [ ] list_price
    - [x] test_list_price_converts_to_float
    - [x] test_list_price_rounds_values
    - [ ] test_list_price_invalid
  - [ ] num_review
    - [x] test_num_reviews_converts_to_int
    - [x] test_num_reviews_replaces_nan_with_zero
    - [ ] test_num_reviews_invalid
  - [ ] piece_count
    - [x] test_piece_count_converts_to_int
    - [ ] test_piece_count_invalid
  - [ ] prod_id
    - [x] test_prod_id_converts_to_int

### US4 — Clean Text Fields
- As a developer, I want to clean text-based columns,
- So that descriptions can be displayed safely in the Streamlit app.

#### Acceptance Criteria
- [ ] prod_desc and prod_long_desc contain no nulls
- [ ] Whitespace trimmed
- [ ] Text preserved (no truncation or corruption)
- [ ] Encoding issues handled if present

#### Tests
- [ ] placeholder

### US5 — Remove Duplicates and Corrupted Rows
- As a developer, I want to remove duplicate and invalid rows,
- So that the dataset is clean and reliable.

#### Acceptance Criteria
- [ ] Duplicate rows removed
- [ ] Row count difference logged
- [ ] No invalid primary keys after cleaning
- [ ] Output dataset falls within expected row count range

#### Tests
- [ ] placeholder

---

## (3) Data Loading and Storage

### US6 — Save Cleaned Dataset to Processed CSV
- As a developer, I want to save the cleaned data to a processed directory,
- So that Streamlit and any other tools can load it reliably.

#### Acceptance Criteria
- [ ] Cleaned CSV saved to `data/processed/lego_clean.csv`
- [ ] Directories created automatically if missing
- [ ] File overwrites safely with logging
- [ ] Saved CSV matches the cleaned DataFrame structure

#### Tests
- [ ] placeholder

---

## (4) Streamlit Application

### US7 — Run ETL Automatically on Streamlit Startup
- As a user, I want the ETL pipeline to run automatically when the Streamlit app starts,
- So that the data is always fresh and processed.

#### Acceptance Criteria
- [ ] ETL runs once per session using caching
- [ ] ETL failures produce readable error messages
- [ ] Cleaned DataFrame available globally in the app

#### Tests
- [ ] placeholder

### US8 — Display Cleaned Dataset
- As a user, I want to preview the cleaned LEGO data,
- So that I can verify the pipeline output in the Streamlit UI.

#### Acceptance Criteria
- [ ] DataFrame preview visible (head or sample)
- [ ] Columns match processed dataset
- [ ] No performance issues on load

#### Tests
- [ ] placeholder

### US10 — Provide Visual Insights Through Charts
- As a user, I want interactive charts showing LEGO trends,
- So that I can explore the cleaned dataset easily.

#### Acceptance Criteria
- [ ] At least 3 charts implemented
- [ ] Sidebar filters update visualisations dynamically
- [ ] Empty filter results handled gracefully

#### Tests
- [ ] placeholder

---

## (5) Developer Documentation

### US11 — Developer-Oriented Documentation
- As a developer, I want clear documentation describing the system,
- So that I can recall key technical decisions for interviews.

#### Acceptance Criteria
- [ ] README explains project purpose, setup, and architecture
- [ ] ETL flow diagram included
- [ ] Developer notes cover challenges, trade-offs, lessons learned
- [ ] Future improvements outlined

#### Tests
- No automated tests — completed via documentation checklist

