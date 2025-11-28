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
