import pandas as pd
from src.utils.logging_utils import setup_logger

from src.transform.transform_numeric import (
    clean_ages,
    clean_list_price,
    clean_num_reviews,
    clean_piece_count,
    clean_prod_id,
)

from src.transform.transform_text import (
    clean_prod_desc,
    clean_prod_long_desc,
    clean_review_difficulty,
    clean_set_name,
    clean_theme_name,
    clean_country,
)


logger = setup_logger("transform", "transform.log")


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Orchestrate transformations
    - numeric values
    - text values
    """

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
    logger.info("Transformation complete.")
    return df
