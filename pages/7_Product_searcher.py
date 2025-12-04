import pandas as pd
import streamlit as st
from src.data_access.app_cache_all_tables import get_tables

st.set_page_config(page_title="Choice of Data", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

tables = get_tables()

products_df = tables["products"]
descriptions_df = tables["product_descriptions"]
themes_df = tables["themes"]
countries_df = tables["countries"]
reviews_df = tables["reviews"]
listings_df = tables["product_listings"]

st.markdown("## Product Viewer")

selected_product = st.selectbox(
    "Select a LEGO product", products_df["set_name"].sort_values(ascending=True)
)

product_id = products_df.loc[
    products_df["set_name"] == selected_product, "prod_id"
].iloc[0]

product_data = (
    products_df[products_df["prod_id"] == product_id]
    .merge(themes_df, on="theme_id")
    .merge(descriptions_df, on="prod_id")
)[["prod_id", "set_name", "theme_name", "prod_long_desc", "age_min", "age_max"]]

product_reviews = listings_df[listings_df["prod_id"] == product_id]

# Averages
avg_star = product_reviews["star_rating"].mean()
avg_value = product_reviews["val_star_rating"].mean()
avg_play = product_reviews["play_star_rating"].mean()
total_reviews = product_reviews["num_reviews"].sum()

# Replace NaN values with "unrated" only for output display
avg_star = "unrated" if pd.isna(avg_star) else f"{avg_star:.2f}"
avg_value = "unrated" if pd.isna(avg_value) else f"{avg_value:.2f}"
avg_play = "unrated" if pd.isna(avg_play) else f"{avg_play:.2f}"
total_reviews = int(total_reviews) if total_reviews > 0 else "unrated"

col_left, col_right = st.columns([2, 1], vertical_alignment="top")

with col_left:
    st.markdown(f"### {selected_product}")
    st.markdown(f"**Product ID:** {product_data['prod_id'].iloc[0]}")
    st.markdown(f"**Theme:** {product_data['theme_name'].iloc[0]}")

    st.markdown("#### Description")
    st.write(product_data["prod_long_desc"].iloc[0])

with col_right:
    st.markdown(
        f"""
        <div class="card">
            <h3> Product Details </h3>
            <p><b>Age Range:</b> {product_data['age_min'].iloc[0]} - {product_data['age_max'].iloc[0]}</p>
            <p><b>Avg Star Rating:</b> {avg_star}</p>
            <p><b>Avg Value Rating:</b> {avg_value}</p>
            <p><b>Avg Play Rating:</b> {avg_play}</p>
            <p><b>Total Reviews:</b> {total_reviews}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
