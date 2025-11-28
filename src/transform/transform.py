import pandas as pd
from src.utils.logging_utils import setup_logger

from src.transform.transform_numeric import (
    clean_ages,
    clean_list_price,
    clean_num_reviews,
    clean_piece_count,
    clean_prod_id,
)


logger = setup_logger("transform", "transform.log")


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Orchestrate transformations
    - numeric values
    """

    logger.info("Starting transformation pipeline...")
    df = clean_ages(df)
    df = clean_list_price(df)
    df = clean_num_reviews(df)
    df = clean_piece_count(df)
    df = clean_prod_id(df)

    logger.info("Transformation complete.")
    return df
