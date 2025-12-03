import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("The Loading Process")
st.subheader("Epic 3 — Data Loading and Storage")


st.markdown(
    """
<div class="card">
<h3>US6 — Create Relational Output Tables</h3>

<p>
    As a developer, I want to load the cleaned dataset into separate relational-style tables,
    so that the data can be used efficiently by the application and follow a clear dimensional model.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>All cleaned data is written into well-structured relational tables</li>
    <li>Each dimension table contains one row per unique entity</li>
    <li>Fact table stores one row per product–country combination</li>
    <li>All tables contain appropriate surrogate keys where required</li>
    <li>Relationships between tables follow a clear and consistent schema</li>
    <li>Tables are saved to <code>data/output/</code></li>
</ul>
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.markdown(
        """
<div class="card tall-card">
    <h3>products</h3>
    <ul>
        <li>Contains core product attributes</li>
        <li>One row per product</li>
        <li>Linked to themes using <code>theme_id</code></li>
        <li>Columns include:
            <ul>
                <li>prod_id</li>
                <li>set_name</li>
                <li>piece_count</li>
                <li>age_min</li>
                <li>age_max</li>
                <li>theme_id</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
<div class="card tall-card">
    <h3>product_descriptions</h3>
    <ul>
        <li>Stores all descriptive text fields</li>
        <li>One row per product</li>
        <li>Avoids duplication by separating long text</li>
        <li>Columns include:
            <ul>
                <li>prod_id</li>
                <li>prod_desc</li>
                <li>prod_long_desc</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
<div class="card tall-card">
    <h3>themes</h3>
    <ul>
        <li>One row per unique theme</li>
        <li>Consistent surrogate key: <code>theme_id</code></li>
        <li>Columns include:
            <ul>
                <li>theme_id</li>
                <li>theme_name</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )


col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    st.markdown(
        """
<div class="card tall-card">
    <h3>countries</h3>
    <ul>
        <li>One row per unique country</li>
        <li>Consistent surrogate key: <code>country_id</code></li>
        <li>Columns include:
            <ul>
                <li>country_id</li>
                <li>country</li>
                <li>country_name</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col5:
    st.markdown(
        """
<div class="card tall-card">
    <h3>review_difficulty</h3>
    <ul>
        <li>Represents review challenge level</li>
        <li>Difficulty values intentionally ordered</li>
        <li>Consistent surrogate key: <code>review_difficulty_id</code></li>
        <li>Columns include:
            <ul>
                <li>review_difficulty_id</li>
                <li>review_difficulty</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col6:
    st.markdown(
        """
<div class="card tall-card">
    <h3>product_listings (Fact Table)</h3>
    <ul>
        <li>One row per product per country</li>
        <li>Composite key: <code>prod_id</code> + <code>country</code></li>
        <li>Columns include:
            <ul>
                <li>prod_id</li>
                <li>country_id</li>
                <li>list_price</li>
                <li>num_reviews</li>
                <li>star_rating</li>
                <li>val_star_rating</li>
                <li>play_star_rating</li>
                <li>review_difficulty</li>
            </ul>
        </li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Loading Orchestrator — `create_tables()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

# ============================================================
# COLUMN 1 — EXPLANATION
# ============================================================
with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>What This Function Does</h3>

    <p>
    The <code>create_tables()</code> function orchestrates the entire 
    loading phase of the pipeline.  
    It takes the <strong>fully cleaned and validated</strong> DataFrame and 
    converts it into a set of relational-style CSV tables stored in 
    <code>data/output/</code>.
    </p>

    <p>
    These tables are designed to mimic a real warehouse schema.
    <p>
    The entire purpose of this loading step is to 
    <strong>create a structured analytical dataset</strong> for Streamlit 
    and future SQL analysis.
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
        <li>Keep the loading phase <strong>modular</strong> — each table has its own creator function</li>
        <li>Ensure referential integrity using surrogate keys</li>
        <li>Split text-heavy columns into their own table to improve performance</li>
        <li>Avoid repeating logic by using a generic <code>write_table()</code> helper</li>
        <li>Design the output structure like a simplified star schema</li>
        <li>Prepare the dataset for instant Streamlit loading</li>
    </ul>

    <p>
    This structure mirrors real ETL design patterns used in industry-grade data pipelines.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============================================================
# COLUMN 2 — CODE
# ============================================================
with col2:
    st.code(
        """
def create_tables(df: pd.DataFrame) -> pd.DataFrame:
    \"""
    Creates tables to be stored in output
    \"""

    themes_df = create_themes_table(df)
    products_df = create_products_table(df, themes_df)
    countries_df = create_country_table(df)
    reviews_df = create_reviews_table(df)
    product_listings_df = create_product_listings_table(df, countries_df, reviews_df)
    product_descriptions_df = create_product_descriptions_table(df)
        """,
        language="python",
    )


# ============================================================
# COLUMN 3 — TESTS
# ============================================================
with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>No Direct Tests</h3>

    <p>
    The <code>create_tables()</code> function is an 
    <strong>orchestrator only</strong> — meaning it simply coordinates 
    other functions.
    </p>

    <p>
    Because all logic lives in the individual table-creation functions
    and the shared <code>write_table()</code> helper, 
    testing this orchestration adds no extra coverage.
    </p>

    <p>
    Instead, the underlying table-generation logic is tested independently.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Reusable Table Writer — `write_table()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

# ============================================================
# COLUMN 1 — EXPLANATION
# ============================================================
with col1:

    # Thought Process
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <p>
    The <code>write_table()</code> function is the backbone of the loading phase.
    Rather than writing a new function for every CSV table, this reusable helper 
    handles the shared behaviour needed for all output tables.
    </p>

    <p>
    This dramatically reduces code duplication and ensures every table follows 
    the same consistent structure.
    </p>

    <ul>
        <li>Make table creation <strong>consistent</strong> across the project</li>
        <li>Avoid repeating CSV-writing logic</li>
        <li>Automatically drop duplicates based on a provided key</li>
        <li>Support surrogate key generation for dimension tables</li>
        <li>Guarantee files save to the correct output directory structure</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Key Responsibilities
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Select the desired subset of columns from the cleaned DataFrame</li>
        <li>Drop duplicates using a <strong>configurable deduplication key</strong></li>
        <li>
            Optionally generate surrogate keys 
            (e.g., <code>theme_id</code>, <code>country_id</code>)
        </li>
        <li>Sort tables consistently for reproducibility</li>
        <li>Save each table to <code>data/output/</code></li>
        <li>Return the created table for further processing</li>
    </ul>

    <p>
    This helper ensures every table is produced with the same reliability and structure,
    enabling a proper relational-style layout.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============================================================
# COLUMN 2 — CODE BLOCK
# ============================================================
with col2:
    st.code(
        """
def write_table(
    df: pd.DataFrame,
    columns: list,
    output_name: str,
    deduplication_key,
    add_surrogate_id: str | None = None,
) -> pd.DataFrame:
    \"""
    Reusable table creation for RDS
    \"""

    logger.info(f"Creating table: {output_name}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # deduplication key can be string or list
    subset = (
        deduplication_key
        if isinstance(deduplication_key, list)
        else [deduplication_key]
    )

    # select columns
    df = df[columns].copy()

    # drop duplicates
    df = df.drop_duplicates(subset=subset)

    # secondary key for star-schema tables
    if add_surrogate_id:
        df = df.sort_values(by=subset).reset_index(drop=True)
        df[add_surrogate_id] = df.index + 1

    # save CSV
    output_path = OUTPUT_DIR / output_name
    df.to_csv(output_path, index=False)

    logger.info(
        f"Table {output_name} created with {len(df)} rows "
        f"Saved to {output_path}"
    )

    return df
        """,
        language="python",
    )


# ============================================================
# COLUMN 3 — TESTS
# ============================================================
with col3:

    # Small top card
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 5</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Test block
    st.code(
        """
def test_write_table_selects_columns():
    df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})

    result = write_table(
        df=df,
        columns=["a", "c"],
        output_name="test.csv",
        deduplication_key="a",
        add_surrogate_id=None,
    )

    assert list(result.columns) == ["a", "c"]
        """,
        language="python",
    )

st.markdown("---")

st.markdown("## Fact Table Creation — `create_product_listings_table()`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

# ==============================================================
# COLUMN 1 — EXPLANATION
# ==============================================================
with col1:

    # Thought Process
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <p>
    The <code>create_product_listings_table()</code> function generates the 
    <strong>fact table</strong> of the relational dataset.
    </p>

    <p>
    Each row in this table represents a product in a specific country, 
    enriched with price, rating, and difficulty attributes.
    </p>

    <p>
    This makes it ideal for analytics, visualisations, and filtering in the Streamlit app.
    </p>

    <ul>
        <li>Create a clean, relational-friendly fact table</li>
        <li>Connect products to countries and review difficulties using surrogate IDs</li>
        <li>Reduce text footprint by replacing names with integer keys</li>
        <li>Ensure uniqueness using a composite key (<code>prod_id</code>, <code>country_id</code>)</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Key Responsibilities
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Join the main dataset with <code>countries_df</code> to attach <strong>country_id</strong></li>
        <li>Join with <code>reviews_df</code> to attach <strong>review_difficulty_id</strong></li>
        <li>Select the key analytical fields</li>
        <li>Use <code>write_table()</code> to produce a clean, deduplicated CSV</li>
    </ul>

    <p>
    This function brings together multiple dimensions to create a proper analytical fact table.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ==============================================================
# COLUMN 2 — CODE BLOCK
# ==============================================================
with col2:
    st.code(
        """
def create_product_listings_table(
    df: pd.DataFrame, countries_df: pd.DataFrame, reviews_df: pd.DataFrame
) -> pd.DataFrame:

    df_with_country_ids = df.merge(countries_df, on="country", how="left")
    df_with_reviews_ids = df_with_country_ids.merge(
        reviews_df, on="review_difficulty", how="left"
    )

    return write_table(
        df=df_with_reviews_ids,
        columns=[
            "prod_id",
            "country_id",
            "list_price",
            "num_reviews",
            "star_rating",
            "val_star_rating",
            "play_star_rating",
            "review_difficulty_id",
        ],
        output_name="product_listings.csv",
        deduplication_key=[
            "prod_id",
            "country_id",
        ],
    )
        """,
        language="python",
    )

# ==============================================================
# COLUMN 3 — TESTS
# ==============================================================
with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>No Direct Tests</h3>

    <p>
    This function relies entirely on previously tested logic:
    </p>

    <ul>
        <li><code>write_table()</code> — tested</li>
        <li>joining via pandas <code>merge()</code> — reliable internal behaviour</li>
        <li>cleaned and validated inputs — guaranteed by earlier stages</li>
    </ul>

    <p>
    Since this function is a thin orchestration layer with no custom logic, 
    additional testing would not provide meaningful coverage.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.markdown("## Relational Database Schema")


st.markdown(
    """
    <div class="flexi-card">
        <h3>Star Schema Overview</h3>
        <p>
        This diagram shows the final relational design of the cleaned LEGO dataset.
        It follows a star-schema pattern with dimension tables for products, themes,
        countries, and review difficulty — all linked through the 
        <strong>product_listings</strong> fact table.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

image = Image.open("docs/erd.png")
st.image(image, use_container_width=True, caption="Relational Database Schema")
