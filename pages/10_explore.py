import streamlit as st
import pandas as pd
from src.data_access.app_cache_all_tables import get_tables

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Choice of Data", layout="wide")
st.markdown("---")
st.markdown("## Relational Output Tables (RDS Style)")

tables = get_tables()

products_df = tables["products"]
descriptions_df = tables["product_descriptions"]
themes_df = tables["themes"]
countries_df = tables["countries"]
reviews_df = tables["reviews"]
listings_df = tables["product_listings"]

# === ROW 1 ===
row1_col1, row1_col2, row1_col3 = st.columns(3, vertical_alignment="top")

with row1_col1:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Products</h3>
            <p>One row per LEGO product.<br>
            Includes set name, age range, and piece count.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(products_df.head(), use_container_width=True)

with row1_col2:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Product Descriptions</h3>
            <p>Text-heavy fields separated to keep things fast.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(descriptions_df.head(), use_container_width=True)

with row1_col3:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Themes</h3>
            <p>Theme dimension with surrogate <code>theme_id</code>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(themes_df.head(), use_container_width=True)

# === ROW 2 ===
row2_col1, row2_col2, row2_col3 = st.columns(3, vertical_alignment="top")

with row2_col1:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Countries</h3>
            <p>ISO country tags mapped to <code>country_id</code>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(countries_df.head(), use_container_width=True)

with row2_col2:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Review Difficulty</h3>
            <p>Difficulty labels mapped to <code>review_difficulty_id</code>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(reviews_df.head(), use_container_width=True)

with row2_col3:
    st.markdown(
        """
        <div class="flexi-card">
            <h3>Product Listings (FACT)</h3>
            <p>The main analytical table linking products, countries, and reviews.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(listings_df.head(), use_container_width=True)
