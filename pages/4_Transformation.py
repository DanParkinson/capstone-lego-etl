import streamlit as st

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("The Transformation Process")
st.subheader("Epic 2 — Data Cleaning and Transformation")

# 3-column layout
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
<div class="card tall-card">
<h3>US3 — Clean Numeric Columns</h3>

<p>
    As a developer, I want to ensure that all numeric-like fields are converted into appropriate
    numeric types, so that calculations, aggregations, and visualisations work correctly.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>All numeric-like fields are identified and converted to the correct numeric type (e.g., int, float)</li>
    <li>Invalid or malformed numeric values are cleaned, coerced, or replaced appropriately</li>
    <li>All numeric fields support downstream analytical operations without errors</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )


with col2:
    st.markdown(
        """
<div class="card tall-card">
<h3>US4 — Clean Text Columns</h3>

<p>
    As a developer, I want to clean and standardise all text-based fields,
    so that names, descriptions, and classifications display correctly and consistently in the application.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>All text fields are converted to a consistent text/string type</li>
    <li>Missing or empty values are replaced with meaningful defaults</li>
    <li>Text is normalised (spacing, casing, safe characters preserved)</li>
    <li>Important symbols (e.g., ™, ®) are preserved when present</li>
    <li>All text fields are validated to ensure compatibility with the UI and database</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
<div class="card tall-card">
<h3>US5 — Remove Duplicates & Validate Clean Data</h3>

<p>
    As a developer, I want to remove duplicates and validate the cleaned dataset,
    so that the data is reliable and ready for further processing.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>All duplicate rows are removed based on defined business rules</li>
    <li>Row count changes are logged for transparency</li>
    <li>The final dataset falls within the expected size range</li>
    <li>All cleaned fields meet structural validation requirements</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Transformation Orchestrator — `transform.py`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Centralise all transformation logic into a single pipeline function</li>
        <li>Ensure transformations occur in a predictable, controlled order</li>
        <li>Separate numeric, text, and structural transformations for clarity</li>
        <li>Keep each transformation step small and testable on its own</li>
    </ul>

    <p>
    The orchestrator coordinates the flow, but the work is
    performed by dedicated cleaning functions. This ensures 
    maintainability and simplifies debugging.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Run numeric cleaning functions (ages, prices, counts, IDs)</li>
        <li>Run text cleaning functions (descriptions, names, categories)</li>
        <li>Remove duplicates using a dedicated cleaning stage</li>
        <li>Drop the now-redundant <code>ages</code> column</li>
        <li>Return the fully cleaned DataFrame for loading</li>
    </ul>

    <p>
    The transformation orchestrator ensures that all cleaning 
    functions run in the correct sequence.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    \"""
    Orchestrate transformations
    - numeric values
    - text values
    \"""

    logger.info("Starting transformation pipeline...")

    # numeric
    df = clean_ages(df)
    df = clean_list_price(df)
    df = clean_num_reviews(df)
    df = clean_piece_count(df)
    df = clean_prod_id(df)

    # text
    df = clean_prod_desc(df)
    df = clean_prod_long_desc(df)
    df = clean_review_difficulty(df)
    df = clean_set_name(df)
    df = clean_theme_name(df)
    df = clean_country(df)

    # duplicates
    df = clean_duplicates(df)

    # drop ages column
    df = df.drop(columns=["ages"], errors="ignore")

    logger.info("Transformation complete.")
    return df
        """,
        language="python",
    )

with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 0</h3>

    <p>
    No direct tests are required for the orchestrator function because 
    each individual cleaning function is tested independently.
    The orchestrator simply sequences already-tested components.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Example Transformation Function — `clean_ages()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <p>
    <strong><code>clean_ages()</code></strong> is one of the most complex 
    cleaning functions in the pipeline. The raw dataset stores ages in mixed
    formats such as:
    </p>

    <ul>
        <li><code>6-12</code> → a proper range</li>
        <li><code>12+</code> → minimum only</li>
        <li><code>1½-3</code> → includes fractions</li>
        <li><code>NaN</code> or malformed text</li>
    </ul>

    <p>The goal is to convert all of these into two clean numeric columns:</p>

    <ul>
        <li><strong>age_min</strong></li>
        <li><strong>age_max</strong></li>
    </ul>
    </div>
    <div class="flexi-card">
    <h4>Key Responsibilites</h4>
    <ul>
        <li>Standardise formats by converting everything to a string first</li>
        <li>Replace fractional unicode (½) with decimals</li>
        <li>Use regex to extract ranges and single values</li>
        <li>Handle <code>+</code> ages by assigning <code>age_max = 99</code></li>
        <li>Ensure numeric types using <code>pd.to_numeric()</code></li>
    </ul>

    <p>
    This function demonstrates how inconsistent real-world data can be,
    and why strong parsing logic is essential in ETL pipelines.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def clean_ages(df: pd.DataFrame) -> pd.DataFrame:
    \"""
    Clean ages columns:
        - ages -> age_min, age_max
    \"""

    if "age_min" in df.columns and "age_max" in df.columns:
        logger.info("Age columns clean - skipping clean_ages().")
        return df

    logger.info("Cleaning ages...")

    ages_clean = df["ages"].astype(str)

    ages_clean = ages_clean.str.replace("½", ".5", regex=False)

    range_extract = ages_clean.str.extract(
        r"(?P<age_min>\\d+\\.?\\d*)-(?P<age_max>\\d+\\.?\\d*)"
    )

    single_extract = ages_clean.str.extract(r"(?P<age_min>\\d+\\.?\\d*)\\+?")

    df["age_min"] = pd.to_numeric(
        range_extract["age_min"].fillna(single_extract["age_min"]),
        errors="coerce"
    )

    df["age_max"] = pd.to_numeric(
        range_extract["age_max"],
        errors="coerce"
    )

    plus_mask = ages_clean.str.contains(r"\\+$", regex=True)
    df.loc[plus_mask, "age_max"] = 99

    logger.info(
        f"Ages cleaned successfully. "
        f"age_min nulls: {df['age_min'].isna().sum()}, "
        f"age_max nulls: {df['age_max'].isna().sum()}"
    )

    return df
        """,
        language="python",
    )

with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests Completed: 22</h3>

    <p>This includes all tests throughout numeric and text column transformations</p>
    <ul>
        <li>Ranges like <code>6-12</code> correctly split</li>
        <li>Both <code>age_min</code> and <code>age_max</code> assigned correctly</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
def test_clean_age_range():
    \"""
    Test age ranges are split up 6-12 -> "6" "12"
    \"""

    df = pd.DataFrame({"ages": ["6-12", "10-16"]})

    result = clean_ages(df)

    assert result.loc[0, "age_min"] == 6
    assert result.loc[0, "age_max"] == 12

    assert result.loc[1, "age_min"] == 10
    assert result.loc[1, "age_max"] == 16
        """,
        language="python",
    )

st.markdown("---")

st.markdown("## Duplicate & Corruption Cleaning — `clean_duplicates()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <p>
    The LEGO dataset contains many repeated products across different countries,
    which is <strong>valid</strong> — one product may have one row per country.
    </p>

    <p>
    However, there are also:
    </p>
    <ul>
        <li>Corrupted rows (missing <code>prod_id</code> or <code>country</code>)</li>
        <li>True duplicates where both fields match</li>
    </ul>

    <p>
    <code>clean_duplicates()</code> ensures the final dataset is structurally clean
    and ready for relational table creation.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Use <strong>prod_id + country</strong> as a composite natural key</li>
        <li>Remove <strong>only</strong> rows missing key identifiers</li>
        <li>Preserve legitimate multi-country entries</li>
        <li>Drop exact duplicates to avoid overcounting or broken joins</li>
        <li>Log the number of rows removed for transparency</li>
    </ul>

    <p>
    This keeps the dataset structurally sound while respecting its real-world shape.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:

    st.code(
        """
def clean_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    \"""
    Remove duplicated rows:
        - Drop rows with missing prod_id or country.
        - Drop duplicated rows based on composite key.
        - Log row count change.
    \"""

    initial_rows = df.shape[0]

    corrupted_rows = df["prod_id"].isna() | df["country"].isna()
    corrupted_rows_count = corrupted_rows.sum()

    if corrupted_rows_count > 0:
        logger.warning(
            f"Removing {corrupted_rows_count} rows with null prod_id/country."
        )
        df = df[(df["prod_id"].notna()) & (df["country"].notna())]

    duplicated_rows_count = df.duplicated(subset=["prod_id", "country"]).sum()

    if duplicated_rows_count > 0:
        logger.info(f"Removing {duplicated_rows_count} duplicate_rows.")
        df = df.drop_duplicates(subset=["prod_id", "country"])

    final_rows = df.shape[0]
    removed_rows = initial_rows - final_rows

    logger.info(
        f"Duplicate cleaning complete. "
        f"Rows before: {initial_rows}, after: {final_rows} "
        f"Removed: {removed_rows}"
    )

    return df
        """,
        language="python",
    )

with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests Completed: 3</h3>

    <p>The following behaviours are validated:</p>


    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
def test_clean_duplicates_keeps_valid_multi_country_rows():
    \"""
    Same prod_id but different countries are valid and must NOT be removed.
    \"""

    df = pd.DataFrame({"prod_id": [1, 1], "country": ["US", "UK"]})

    result = clean_duplicates(df)

    assert len(result) == 2
        """,
        language="python",
    )

st.markdown("---")

st.markdown("## Clean Dataset Validation — `validate_clean_lego_data()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>What This Function Does</h3>

    <p>
    After transformation, we need to ensure the cleaned dataset is 
    <strong>structurally safe</strong> before loading it into
    relational tables.
    </p>

    <p>
    <code>validate_clean_lego_data()</code> performs strict checks on:
    </p>

    <ul>
        <li><strong>Numeric dtypes</strong> (float / int)</li>
        <li><strong>Text columns</strong> being non-null</li>
        <li><strong>No unexpected missing values</strong></li>
        <li><strong>Correct string types</strong> for text fields</li>
    </ul>

    <p>
    This ensures the data is fully prepared for table creation,
    joins, and safe loading into the final analytical dataset.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Fail fast — catch errors <strong>before</strong> writing CSV outputs</li>
        <li>Prevent silent corruption in relational tables</li>
        <li>Guarantee consistent types for Streamlit & SQL analysis</li>
        <li>Mirror real-world data warehouse validation rules</li>
        <li>Keep validation modular and reusable</li>
    </ul>

    <p>
    This step enforces data contract rules and protects downstream logic.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:

    st.code(
        """
def validate_clean_lego_data(df=pd.DataFrame) -> None:
    \"""
    Validates the clean lego data:
        - Correct dtypes
        - No unexpected missing values
        - Text columns are non-null
        - Safe table
    \"""

    # float check
    for col in NUMERIC_FLOAT_COLS:
        if not pd.api.types.is_float_dtype(df[col]):
            raise TypeError(f"Column {col} must be float. Got: {df[col].dtype}")

    # int checks
    for col in NUMERIC_INT_COLS:
        if not pd.api.types.is_integer_dtype(df[col]):
            raise TypeError(f"Column {col} must be int. Got: {df[col].dtype}")

    # text checks
    for col in TEXT_COLS:
        if df[col].isna().any():
            raise ValueError(f"Column {col} contains NULLS")

        if not pd.api.types.is_string_dtype(df[col]):
            raise TypeError(f"colum {col} must be string. Got: {df[col].dtype}")

    logger.info("Clean Lego dataset Validated successfully.")
        """,
        language="python",
    )

with col3:

    st.markdown(
        """
    <div class="flexi-card">
        <h3>Tests Completed: 5</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
def test_validate_clean_data_fails_for_non_string_text_column():
    \"""
    Test text columns:
        - Change strings to ints
        - Should raise error
    \"""

    df = valid_df()
    df["theme_name"] = [1, 2]

    with pytest.raises(TypeError):
        validate_clean_lego_data(df)
        """,
        language="python",
    )
