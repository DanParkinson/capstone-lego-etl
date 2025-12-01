import pandas as pd
from src.load.write_tables import write_table


def create_products_table(df: pd.DataFrame, themes_df: pd.DataFrame) -> pd.DataFrame:

    df_with_theme_ids = df.merge(themes_df, on="theme_name", how="left")

    return write_table(
        df=df_with_theme_ids,
        columns=[
            "prod_id",
            "set_name",
            "piece_count",
            "age_min",
            "age_max",
            "theme_id",
        ],
        output_name="products.csv",
        deduplication_key="prod_id",
    )


def create_product_descriptions_table(df: pd.DataFrame) -> pd.DataFrame:
    return write_table(
        df=df,
        columns=["prod_id", "prod_desc", "prod_long_desc"],
        output_name="product_descriptions.csv",
        deduplication_key="prod_id",
    )


def create_themes_table(df: pd.DataFrame) -> pd.DataFrame:
    return write_table(
        df=df,
        columns=["theme_name"],
        output_name="themes.csv",
        deduplication_key="theme_name",
        add_surrogate_id="theme_id",
    )


def create_reviews_table(df: pd.DataFrame) -> pd.DataFrame:

    DIFFICULTY_ORDER = {
        "unrated": 1,
        "very easy": 2,
        "easy": 3,
        "average": 4,
        "challenging": 5,
        "very challenging": 6,
    }

    difficulty_df = pd.DataFrame(
        DIFFICULTY_ORDER.items(), columns=["review_difficulty", "review_difficulty_id"]
    )

    return write_table(
        df=difficulty_df,
        columns=["review_difficulty", "review_difficulty_id"],
        output_name="reviews.csv",
        deduplication_key="review_difficulty",
        add_surrogate_id=None,
    )


def create_country_table(df: pd.DataFrame) -> pd.DataFrame:

    COUNTRY_NAMES = {
        "US": "United States",
        "DE": "Germany",
        "FR": "France",
        "GB": "United Kingdom",
        "NZ": "New Zealand",
        "IE": "Ireland",
        "IT": "Italy",
        "ES": "Spain",
        "AU": "Australia",
        "CA": "Canada",
        "CH": "Switzerland",
        "CZ": "Czech Republic",
        "AT": "Austria",
        "BE": "Belgium",
        "LU": "Luxembourg",
        "NL": "Netherlands",
        "NO": "Norway",
        "PL": "Poland",
        "PT": "Portugal",
        "FI": "Finland",
        "DN": "Denmark",
    }

    country_names_df = df[["country"]].drop_duplicates().copy()

    country_names_df["country_name"] = country_names_df["country"].map(COUNTRY_NAMES)

    return write_table(
        df=country_names_df,
        columns=["country", "country_name"],
        output_name="countries.csv",
        deduplication_key="country",
        add_surrogate_id="country_id",
    )


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
