import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("transform", "transform.log")


def clean_prod_desc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean prod_desc:
        - replace nulls with default message
        - concert to string
    """

    logger.info("Cleaning prod_desc...")

    default_msg = "No description available"

    df["prod_desc"] = df["prod_desc"].fillna(default_msg)

    df["prod_desc"] = df["prod_desc"].astype(str)

    logger.info(
        f"prod_desc cleaned successfully. "
        f"prod_desc nulls: {df['prod_desc'].isna().sum()}"
    )

    return df


def clean_prod_long_desc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean prod_long_desc:
        - replace nulls with default message
        - concert to string
    """

    logger.info("Cleaning prod_long_desc...")

    default_msg = "No long description available"

    df["prod_long_desc"] = df["prod_long_desc"].fillna(default_msg)

    df["prod_long_desc"] = df["prod_long_desc"].astype(str)

    logger.info(
        f"prod_long_desc cleaned successfully. "
        f"prod_long_desc nulls: {df['prod_long_desc'].isna().sum()}"
    )

    return df


def clean_review_difficulty(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean review_difficulty:
        - replace nulls with default message
        - Convert to lower case
        - concert to string
    """

    logger.info("Cleaning review_difficulty...")

    default_msg = "Unrated"

    df["review_difficulty"] = df["review_difficulty"].fillna(default_msg)

    df["review_difficulty"] = df["review_difficulty"].astype(str)

    df["review_difficulty"] = df["review_difficulty"].str.lower()

    logger.info(
        f"review_difficulty cleaned successfully. "
        f"review_difficulty nulls: {df['review_difficulty'].isna().sum()}"
    )

    return df


def clean_set_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean set_name:
        - replace nulls with default message
        - convert to string
    """

    logger.info("Cleaning set_name...")

    default_msg = "Unknown Set Name"

    df["set_name"] = df["set_name"].fillna(default_msg)
    df["set_name"] = df["set_name"].astype(str)

    logger.info(
        f"set_name cleaned successfully. "
        f"set_name nulls: {df['set_name'].isna().sum()}"
    )

    return df


def clean_theme_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean theme_name:
        - replace nulls with default message
        - convert to string
    """

    logger.info("Cleaning theme_name...")

    default_msg = "Unknown Theme"

    df["theme_name"] = df["theme_name"].fillna(default_msg)
    df["theme_name"] = df["theme_name"].astype(str)

    logger.info(
        f"theme_name cleaned successfully. "
        f"theme_name nulls: {df['theme_name'].isna().sum()}"
    )

    return df


def clean_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean country:
        - replace nulls with default message
        - convert to string
    """

    logger.info("Cleaning country...")

    default_msg = "Unknown"

    df["country"] = df["country"].fillna(default_msg)
    df["country"] = df["country"].astype(str)

    logger.info(
        f"country cleaned successfully. " f"country nulls: {df['country'].isna().sum()}"
    )

    return df
