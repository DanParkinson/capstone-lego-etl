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
    Validation function.
    Validates the raw LEGO file after extraction.

    Logs:
        column names, dtypes, missing values.

    Raises:
        Errors for structural mismatch
    """

    # Check structure
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(
            f"Column mismatch.\nExpected: {EXPECTED_COLUMNS}.\nGot: {list(df.columns)}"
        )

    logger.info("Raw data structure validated successfully.")

    # # log dtypes
    # logger.info("Column data types:")
    # logger.info(df.dtypes)

    # # Log missing values
    # missing = df.isna().sum()
    # logger.info("Missing values per column:")
    # logger.info(missing)
