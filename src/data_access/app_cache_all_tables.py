import streamlit as st
from src.data_access.app_data_loader import load_table


@st.cache_data
def get_tables():
    return {
        "products": load_table("products.csv"),
        "themes": load_table("themes.csv"),
        "reviews": load_table("reviews.csv"),
        "countries": load_table("countries.csv"),
        "product_descriptions": load_table("product_descriptions.csv"),
        "product_listings": load_table("product_listings.csv"),
    }
