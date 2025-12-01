import pandas as pd
from src.utils.logging_utils import setup_logger
from src.load.load_tables import (
    create_products_table,
    create_product_descriptions_table,
    create_themes_table,
    create_product_listings_table,
    create_country_table,
    create_reviews_table,
)

logger = setup_logger("create_tables", "load.log")


def create_tables(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates tables to be stored in output
    """
    themes_df = create_themes_table(df)
    products_df = create_products_table(df, themes_df)
    countries_df = create_country_table(df)
    reviews_df = create_reviews_table(df)
    product_listings_df = create_product_listings_table(df, countries_df, reviews_df)
    Product_descriptions_df = create_product_descriptions_table(df)
