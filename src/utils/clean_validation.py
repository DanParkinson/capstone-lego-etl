import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("validate_clean", "validate.log")

# Numeric — float
NUMERIC_FLOAT_COLS = [
    "list_price",
    "star_rating",
    "val_star_rating",
    "age_min",
    "age_max",
]

# Numeric — int
NUMERIC_INT_COLS = [
    "num_reviews",
    "piece_count",
    "prod_id",
]

# Text columns — string and non null
TEXT_COLS = [
    "prod_desc",
    "prod_long_desc",
    "set_name",
    "theme_name",
    "review_difficulty",
    "country",
]


def validate_clean_lego_data(df=pd.DataFrame) -> None:
    """
    Validates the clean lego data:
        - Correct dtypes
        - no unexpected missing values
        - text columns are non-null
        - safe table
    """

    # float check
    for col in NUMERIC_FLOAT_COLS:
        if not pd.api.types.is_float_dtype(df[col]):
            raise TypeError(f"Column {col} must be float. Got: {df[col].dtype}")

    # int checks
    for col in NUMERIC_INT_COLS:
        if not pd.api.types.is_integer_dtype(df[col]):
            raise TypeError(f"Column {col} must be int. Got: {df[col].dtype}")

    # text checks
    for col in TEXT_COLS:
        # check null
        if df[col].isna().any():
            raise ValueError(f"Column {col} contains NULLS")

        # check string
        if not pd.api.types.is_string_dtype(df[col]):
            raise TypeError(f"colum {col} must be string. Got: {df[col].dtype}")

    logger.info("Clean Lego dataset Validated successfully.")
