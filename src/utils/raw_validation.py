import pandas as pd
import logging
from src.utils.logging_utils import setup_logger

logger = setup_logger("validate_raw", "validate.log")

EXPECTED_COLUMNS = [
    "ages",
    "list_price",
    "num_reviews",
    "piece_count",
    "play_star_rating",
    "prod_desc",
    "prod_id",
    "prod_long_desc",
    "review_difficulty",
    "set_name",
    "star_rating",
    "theme_name",
    "val_star_rating",
    "country",
]


def validate_raw_lego_data(df: pd.DataFrame) -> None:
    """
    Validates the raw LEGO dataset after extraction.

    Checks:
        - All expected columns are present
        - No expected columns are missing
    Warns:
        - Extra unexpected columns
    """

    # Check structure
    df_cols = set(df.columns)
    expected = set(EXPECTED_COLUMNS)

    missing_columns = expected - df_cols
    extra_columns = df_cols - expected

    if missing_columns:
        logger.error(f"Missing expected columns: {missing_columns}")
        raise ValueError(f"Missing expected columns: {missing_columns}")

    if extra_columns:
        logger.warning(f"Unexpected extra columns: {extra_columns}")

    logger.info("Raw data structure validated successfully.")

    # # log dtypes
    # logger.info("Column data types:")
    # logger.info(df.dtypes)

    # # Log missing values
    # missing = df.isna().sum()
    # logger.info("Missing values per column:")
    # logger.info(missing)
