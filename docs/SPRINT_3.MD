# Sprint 3 — Data Loading & Relational Table Creation

## Overview  
Sprint 3 focused on the **Load phase** of the ETL pipeline.  
After extraction, validation, and transformation, the cleaned LEGO dataset was reshaped into a set of relational-style tables designed for efficient querying, reduced redundancy, and improved performance within the Streamlit application.

This sprint introduced a **dimensional model** (similar to a star schema), separating descriptive attributes into dimension tables while storing measurable, country-specific values in a central fact table.

All load logic is contained in:

'''python
src/load/
'''
All output tables are stored in:

'''python
data/output/
'''


---

## Objectives
- Convert the cleaned DataFrame into a structured relational schema.
- Remove repeated text fields by moving them into dimension tables.
- Generate surrogate keys for themes, countries, and review difficulties.
- Produce lightweight, analysis-ready tables.
- Ensure consistent table creation using a reusable `write_table` utility.

---

## Load Pipeline Summary

### 1. `products` (Dimension)
Represents one row per LEGO set.

**Columns**
- `prod_id`
- `set_name`
- `piece_count`
- `age_min`
- `age_max`
- `theme_id` (FK → themes)

**Details**
- Duplicates removed by `prod_id`.
- Theme strings replaced with integer IDs.
- Core product attributes stored without heavy text fields.

---

### 2. `product_descriptions` (Dimension)
Stores large text fields separately to keep product tables lean.

**Columns**
- `prod_id`
- `prod_desc`
- `prod_long_desc`

**Details**
- One row per product.
- Reduces duplication and improves performance in fact table joins.

---

### 3. `themes` (Dimension)
Lookup table for LEGO themes.

**Columns**
- `theme_name`
- `theme_id` (surrogate key)

**Details**
- Stable IDs assigned in deterministic order.
- Avoids repeating theme names across rows.

---

### 4. `countries` (Dimension)
Represents markets in which LEGO products were reviewed.

**Columns**
- `country` (code)
- `country_name` (full name)
- `country_id` (surrogate key)

**Details**
- Country codes mapped to readable names.
- Used later to replace country strings in fact table.

---

### 5. `review_difficulty` (Dimension)
Represents ordered difficulty levels for product reviews.

**Columns**
- `review_difficulty`
- `review_difficulty_id`

**Details**
- IDs follow a deliberate semantic order:
- unrated → very easy → easy → average → challenging → very challenging
- Ensures correct sorting in dashboards and analytics.

### 6. `product_listings` (Fact Table)
Captures measurable, country-specific product information.

**Columns**
- `prod_id` (FK)
- `country` (later replaced by `country_id`)
- `list_price`
- `num_reviews`
- `star_rating`
- `val_star_rating`
- `play_star_rating`
- `review_difficulty`

**Details**
- One row per product per country.
- Composite key (`prod_id`, `country`).
- Stores all numeric measures used in analytics.

---

## Reusable Utility: `write_table`
A shared function responsible for:

- Column selection  
- Deduplication  
- Surrogate key creation  
- CSV saving  
- Ensuring all tables follow the same structure  

This greatly simplified Sprint 3 by removing repeated logic across load functions.

---

## Testing Summary

Only the shared mechanism (`write_table`) requires testing, as all load functions delegate their behaviour to it.

### Tests cover:
- Column selection  
- Deduplication behavior  
- Surrogate key generation  
- File output creation  

This minimal test suite validates the entire load layer effectively.

---

## Status  
**Sprint 3 is complete.**  
The LEGO dataset is now represented as a clear, efficient relational model with dimension tables and a fact table.  
These tables form the foundation for analytical queries and power the Streamlit dashboard in later stages.

