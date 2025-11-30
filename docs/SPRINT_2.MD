# Epic 2 – Data Cleaning & Transformation  
## User Story 3 – Clean Numeric Columns

### Overview  
User Story 3 focused on the cleaning and standardisation of numeric columns in the LEGO dataset after successful extraction.  
The goal was to ensure that all numeric-like fields were correctly typed, consistent, and suitable for downstream analysis, aggregation, and visualisation in the Streamlit application.

This user story required function-level cleaning logic, reusable validation utilities, and targeted unit tests for each numeric transformation.

---

## Workflow Summary

### `transform_numeric.py`
This module contains individual cleaning functions for each numeric field. Each function:

- Converts the target column into a valid numeric dtype  
- Handles invalid or malformed values  
- Enforces domain-appropriate behaviour (e.g., NaN → 0 for review counts)  
- Logs column-quality metrics using a shared validation utility  

---

## Cleaning Completed per Column

| Column               | Cleaning Logic                                                                                        | Result                          |
| -------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------- |
| **ages**             | Split “6-12”, “12+”, “1½-3” into `age_min` and `age_max`, handled fractional ages, set `12+` → max 99 | Clean floats, no missing ranges |
| **list_price**       | Convert to numeric, round to 2 decimals                                                               | Clean float64                   |
| **num_reviews**      | Convert to numeric, *NaN → 0*, cast to int                                                            | Clean int64, no missing         |
| **piece_count**      | Convert to numeric, NaN → 0, cast to int                                                              | Clean int64                     |
| **play_star_rating** | Already clean, no action required                                                                     | float64                         |
| **prod_id**          | Convert to numeric, convert to Int64                                                                  | Nullable integer                |
| **star_rating**      | Already clean, no action required                                                                     | float64                         |
| **val_star_rating**  | Already clean, no action required                                                                     | float64                         |

---

## Key Improvements  
- All numeric fields now have deterministic, validated dtypes  
- Strings, malformed values, and non-numeric characters no longer remain  
- Invalid values become NaN (or 0 when domain-appropriate)   
- Logging now provides traceable diagnostics for each cleaned column

---

## Testing Completed

Unit tests were written to validate critical behaviours of each cleaning function.  
Rather than exhaustively testing every edge case, each test focused on:

- Correct dtype conversion  
- Handling of invalid values  
- Expected rounding or coercion behaviour  
- Idempotent transformations  

### `tests/unit_tests/test_transform_numeric.py`

#### Ages  
- ✓ `test_age_range` — parses “6-12” correctly  
- ✓ `test_age_plus` — handles “12+” upper range  
- ✓ `test_age_fractional_values` — manages “1½-3”  
- ☐ `test_age_invalid` — pending

#### list_price  
- ✓ `test_list_price_converts_to_float`  
- ✓ `test_list_price_rounds_values`  
- ☐ `test_list_price_invalid` — pending

#### num_reviews  
- ✓ `test_num_reviews_converts_to_int`  
- ✓ `test_num_reviews_replaces_nan_with_zero`  
- ☐ `test_num_reviews_invalid` — pending  

#### piece_count  
- ✓ `test_piece_count_converts_to_int`  
- ☐ `test_piece_count_invalid` — pending  

#### prod_id  
- ✓ `test_prod_id_converts_to_int`

---

## Status  
**User Story 3 is partially complete.**  
All required numeric columns have been cleaned and integrated into the pipeline, with core tests implemented.  
Additional negative-case tests remain as optional enhancements.

Next step: **User Story 4 – Clean Text Fields**.

## User Story 4 – Clean Text Columns

### Overview  
User Story 4 focused on cleaning and standardising all text-based columns in the LEGO dataset.  
The goal was to ensure that descriptive fields, categorical labels, and country codes are consistent, non-null, and suitable for display within the Streamlit application.

This user story required dedicated cleaning functions for each text column, null-handling, and a comprehensive suite of unit tests validating each transformation.

---

## Workflow Summary

### `transform_text.py`
This module contains individual cleaning functions for text and categorical fields. Each function:

- Replaces missing or null values with a column-appropriate placeholder  
- Converts the column to a consistent string dtype  
- Applies any additional formatting (e.g., lowercase for difficulty categories)  
- Preserves meaningful characters such as ™ and ®  
- Ensures the column is ready for downstream consumption

---

## Cleaning Completed per Column

| Column                | Cleaning Logic                                                                  | Result                               |
| --------------------- | ------------------------------------------------------------------------------- | ------------------------------------ |
| **prod_desc**         | Null → `"No description available"`, convert to string                          | Clean strings, no nulls              |
| **prod_long_desc**    | Null → `"No long description available"`, convert to string, preserve structure | Clean long text, no nulls            |
| **review_difficulty** | Null → `"unrated"`, convert to string, lowercase values                         | Normalised lowercase categories      |
| **set_name**          | Null → `"Unknown Set Name"`, convert to string                                  | Clean strings, consistent formatting |
| **theme_name**        | Null → `"Unknown Theme"`, convert to string                                     | Clean strings, trademarks preserved  |
| **country**           | Null → `"Unknown"`, convert to string                                           | Clean ISO-like country codes         |

---

## Key Improvements  
- All text columns are now guaranteed to be non-null  
- Dtypes are consistent (string across all cleaned fields)  
- Review difficulty categories standardised to lowercase  
- All descriptive fields safe for direct rendering in Streamlit  
- Clean, predictable input for downstream analytics and filtering

---

## Testing Completed  

Unit tests were written to validate each cleaning function.  
Tests focused on key behaviours:

- Correct null replacement  
- String conversion  
- Whitespace removal  
- Lowercasing where applicable  
- Idempotent transformations  

### `tests/unit_tests/test_transform_text.py`

#### prod_desc  
- ✓ `test_clean_prod_desc_fills_nulls`  
- ✓ `test_clean_prod_desc_ensures_string_type`  

#### prod_long_desc  
- ✓ `test_clean_prod_long_desc_fills_nulls`  
- ✓ `test_clean_prod_long_desc_ensures_string_type`  

#### review_difficulty  
- ✓ `test_clean_review_difficulty_fills_nulls`  
- ✓ `test_clean_review_difficulty_ensures_string_type`  
- ✓ `test_clean_review_difficulty_converts_to_lowercase`  

#### set_name  
- ✓ `test_clean_set_name_fills_nulls`  
- ✓ `test_clean_set_name_ensures_string_type`  

#### theme_name  
- ✓ `test_clean_theme_name_fills_nulls`  
- ✓ `test_clean_theme_name_ensures_string_type`  

#### country  
- ✓ `test_clean_country_fills_nulls`  
- ✓ `test_clean_country_ensures_string_type`  

---

## Status  
**User Story 4 is complete.**  
All text columns have been standardised, tested, and integrated into the transformation pipeline.  
The dataset is now consistently structured and ready for feature engineering and Streamlit presentation.

Next step: **User Story 5 – Data Integrity Validation & Structural Testing**.
 
## User Story 5 – Remove Duplicates and Corrupted Rows

### Overview  
User Story 5 focused on strengthening the structural integrity of the cleaned LEGO dataset by removing corrupted rows and eliminating invalid duplicates.  
The raw dataset contains multiple entries for the same product across different countries, so a **composite primary key** (`prod_id`, `country`) was adopted as the correct uniqueness definition.

This cleaning step occurs **after numeric and text cleaning**, ensuring the key fields (`prod_id`, `country`) are properly typed and reliable before enforcing uniqueness.  
The goal is to ensure that only genuinely duplicate or corrupted records are removed, while legitimate per-country entries remain intact.

---

## Workflow Summary

### `transform_duplicates.py`  
A dedicated module responsible for final structural validation:

- Removes rows where `prod_id` is missing  
- Removes rows where `country` is missing  
- Removes true duplicates using the composite key (`prod_id`, `country`)  
- Logs:
  - Number of corrupted rows removed  
  - Number of duplicate rows removed  
- Returns a structurally clean DataFrame suitable for downstream loading

This prevents accidental loss of valid rows while ensuring the dataset is fit for relational modelling.

---

### Integration in `transform.py`
The overall transformation pipeline was updated to run duplicate cleaning **after all core cleaning steps**:

1. Numeric column cleaning  
2. Text column cleaning  
3. **Duplicate and corruption removal (final structural step)**  
4. Return the fully cleaned, validated DataFrame  

Placing this step last ensures:

- Numeric conversions are completed before evaluating uniqueness  
- Text fixes prevent inconsistencies in country names  
- Composite keys are correct and comparable  
- Duplicate detection relies on fully-cleaned data rather than raw Kaggle inconsistencies

---

## Testing Completed

### Duplicate Cleaning Tests  
Focused tests confirm that duplicate removal behaves correctly:

- Removes rows with missing `prod_id`  
- Removes rows with missing `country`  
- Removes only true duplicates based on (`prod_id`, `country`)  
- Preserves legitimate entries representing different countries  

These tests ensure the duplicate-cleaning logic is reliable and safe across varying scenarios.

---

## Status  
**User Story 5 is complete.**  
The dataset is now:

- Free of corrupted rows  
- Free of invalid duplicates  
- Structurally consistent and ready for table modelling  

Next step: **User Story 6 – Save Cleaned Dataset to Processed CSV.**

