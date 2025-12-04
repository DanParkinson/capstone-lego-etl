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
- As a developer, I want to convert numeric-like fields into proper numeric types,
- So that calculations, aggregations, and visualisations work correctly.

#### Acceptance Criteria

- [ ] Clean and validate the following numeric-like columns:
  - **ages**
    - [x] Extract `age_min` and `age_max` into separate numeric columns
    - [x] Ensure both are numeric (float)
    - [x] No nulls after extraction
    - [ ] Drop the original `ages` column
  - **list_price**
    - [x] Convert to float
    - [x] Round to 2 decimal places
    - [x] Replace invalid values with NaN
    - [x] Convert dtype to float64
  - **num_reviews**
    - [x] Convert to int
    - [x] Replace nulls with 0 (no reviews)
    - [x] Remove or coerce invalid values
    - [x] Ensure dtype is int64
  - **piece_count**
    - [x] Convert to int
    - [x] Ensure dtype is int64
  - **play_star_rating**
    - [x] Convert to float
    - [x] Allow NaN (not all sets are rated)
    - [x] Ensure dtype is float64
  - **prod_id**
    - [x] Convert to int
    - [x] Coerce invalid entries to NaN
    - [x] Ensure dtype is int64
    - [x] Note: `prod_id` is **not unique** (varies by country)

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

### US4 — Clean Text Columns
- As a developer, I want to clean all text-based columns,
- So that descriptions, names, and categories display correctly in the Streamlit app.

#### Acceptance Criteria
- [ ] Clean and validate the following text columns:
  - **prod_desc**
    - [x] Replace nulls with "No description available"
    - [x] Ensure dtype is string
  - **prod_long_desc**
    - [x] Replace nulls with "No long description available"
    - [x] Ensure dtype is string
  - **review_difficulty**
    - [x] Replace nulls with "Unrated"
    - [x] Convert to lower case
    - [x] Ensure dtype is string
  - **set_name**
    - [x] Replace nulls with "Unknown Set Name"
    - [x] Ensure dtype is string
  - **theme_name**
    - [x] Replace nulls with "Unknown Theme"
    - [x] Preserve trademarks (™, ®)
    - [x] Ensure dtype is string
  - **country**
    - [x] Replace nulls with "Unknown"
    - [x] Ensure dtype is string

#### Tests
- [ ] src/transform/transform_text.py
  - [ ] prod_desc
    - [x] test_clean_prod_desc_fills_nulls
    - [x] test_clean_prod_desc_ensures_string_type
  - [ ] prod_long_desc
    - [x] test_clean_prod_long_desc_fills_nulls
    - [x] test_clean_prod_long_desc_ensures_string_type
  - [ ] review_difficulty
    - [x] test_clean_review_difficulty_fills_nulls
    - [x] test_clean_review_difficulty_ensures_string_type
    - [x] test_clean_review_difficulty_converts_to_lowercase
  - [ ] set_name
    - [x] test_clean_set_name_fills_nulls
    - [x] test_clean_set_name_ensures_string_type
  - [ ] theme_name
    - [x] test_clean_theme_name_fills_nulls
    - [x] test_clean_theme_name_ensures_string_type
  - [ ] country
    - [x] test_clean_country_fills_nulls
    - [x] test_clean_country_ensures_string_type

### US5 — Remove Duplicates and Corrupted Rows + cleaning validation
- As a developer, I want to remove duplicates and validate clean data,
- So that the dataset is clean and reliable.

#### Acceptance Criteria
- [x] Duplicate rows removed
- [x] Row count difference logged
- [x] No invalid primary keys after cleaning
- [x] Output dataset falls within expected row count range

#### Tests
- [ ] test_clean_duplicates.py
  - [x] test_clean_duplicates_keeps_valid_multi_country_rows
  - [x] test_clean_duplicates_removes_null_primary_keys
- [ ] test_clean_validation.py
  - [x] test_validate_clean_data_passes_for_valid_df
  - [x] test_validate_clean_data_fails_for_non_float_column
  - [x] test_validate_clean_data_fails_for_non_int_column
  - [x] test_validate_clean_data_fails_for_null_text_column
  - [x] test_validate_clean_data_fails_for_non_string_text_column

---

## (3) Data Loading and Storage

### US6 — Create Relational Output Tables  
- As a developer, I want to load the cleaned dataset into separate relational-style tables,
- So that the data can be used efficiently by the application and follow a clear dimensional model.

#### Acceptance Criteria  
Create the following output tables in `data/output/`:

- **products**
  - [x] Columns: `prod_id`, `set_name`, `piece_count`, `age_min`, `age_max`, `theme_id`
  - [x] One row per product (`prod_id`)
  - [x] Linked to themes via `theme_id`

- **product_descriptions**
  - [x] Columns: `prod_id`, `prod_desc`, `prod_long_desc`
  - [x] One row per product
  - [x] Stores large text fields separately to avoid duplication

- **themes**
  - [x] Columns: `theme_name`, `theme_id`
  - [x] One row per unique theme
  - [x] Surrogate key `theme_id` assigned in consistent order

- **countries**
  - [x] Columns: `country`, `country_name`, `country_id`
  - [x] One row per unique country
  - [x] Full country names mapped from country codes
  - [x] Surrogate key `country_id` assigned

- **review_difficulty**
  - [x] Columns: `review_difficulty`, `review_difficulty_id`
  - [x] Difficulty values ordered intentionally (unrated → very challenging)
  - [x] Surrogate key preserved (not regenerated)

- **product_listings** (Fact Table)
  - [x] Columns:  
        `prod_id`, `country`, `list_price`, `num_reviews`,  
        `star_rating`, `val_star_rating`, `play_star_rating`, `review_difficulty`
  - [x] One row per product per country
  - [x] Composite key (`prod_id`, `country`)
  - [x] Clean measures used from transform stage

#### Tests  
- [ ] src/load/write_table.py
  - [x] test_write_table_selects_columns  
  - [x] test_write_table_deduplicates  
  - [x] test_write_table_adds_surrogate_key  


---

## (4) Streamlit Application

### US7 — Streamlit App Loads the data
- As a user, I want the ETL pipeline to run automatically when the Streamlit app starts,
- So that the data is always fresh and processed.

#### Acceptance Criteria
- [x] ETL failures produce readable error messages
- [x] Cleaned DataFrame available globally in the app

#### Tests
- [ ] placeholder

### US8 — Display Cleaned Dataset
- As a user, I want to preview the cleaned LEGO data,
- So that I can verify the pipeline output in the Streamlit UI.

#### Acceptance Criteria
- [x] DataFrame preview visible (head or sample)
- [x] Columns match processed dataset
- [x] No performance issues on load

#### Tests
- [ ] placeholder

### US10 — Provide Visual Insights Through Charts
- As a user, I want interactive charts showing LEGO trends,
- So that I can explore the cleaned dataset easily.

#### Acceptance Criteria
- [x] At least 3 charts implemented
- [x] Sidebar filters update visualisations dynamically
- [x] Empty filter results handled gracefully

#### Tests
- [ ] placeholder

---

## (5) Developer Documentation

### US11 — Developer-Oriented Documentation
- As a developer, I want clear documentation describing the system,
- So that I can recall key technical decisions for interviews.

#### Acceptance Criteria
- [x] README explains project purpose, setup, and architecture
- [x] ETL flow diagram included
- [x] Developer notes cover challenges, trade-offs, lessons learned
- [x] Future improvements outlined

#### Tests
- No automated tests — completed via documentation checklist

