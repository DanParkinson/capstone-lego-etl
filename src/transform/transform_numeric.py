import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("transfrom", "transform.log")


def clean_ages(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean ages columns:
        - ages -> age_min, age_max
    """

    if "age_min" in df.columns and "age_max" in df.columns:
        logger.info("Age columns clean - skipping clean_ages().")
        return df

    logger.info("Cleaning ages...")

    # Make it a string to work on
    ages_clean = df["ages"].astype(str)

    # replace fractionals with decimals
    ages_clean = ages_clean.str.replace("½", ".5", regex=False)

    # Extract Ranges "6-12"
    range_extract = ages_clean.str.extract(
        r"(?P<age_min>\d+\.?\d*)-(?P<age_max>\d+\.?\d*)"
    )

    # Extract single "6+"
    single_extract = ages_clean.str.extract(r"(?P<age_min>\d+\.?\d*)\+?")

    # Build age min
    df["age_min"] = pd.to_numeric(
        range_extract["age_min"].fillna(single_extract["age_min"]), errors="coerce"
    )

    # Build age max
    df["age_max"] = pd.to_numeric(range_extract["age_max"], errors="coerce")

    # Apply '+' rule -> age_max = 99
    plus_mask = ages_clean.str.contains(r"\+$", regex=True)
    df.loc[plus_mask, "age_max"] = 99

    logger.info(
        f"Ages cleaned successfully. "
        f"age_min nulls: {df['age_min'].isna().sum()}, "
        f"age_max nulls: {df['age_max'].isna().sum()}"
    )

    return df


def clean_list_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean list_price:
        - round and ensure numeric
    """

    logger.info("Cleaning list_price...")

    df["list_price"] = pd.to_numeric(df["list_price"], errors="coerce")

    df["list_price"] = df["list_price"].round(2)

    logger.info(
        f"list_price cleaned successfully. "
        f"list_price nulls: {df['list_price'].isna().sum()}"
    )

    return df


def clean_num_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean num_reviews:
        - int
        - Nan -> 0
    """
    logger.info("Cleaning num_reviews...")

    df["num_reviews"] = pd.to_numeric(df["num_reviews"], errors="coerce")

    df["num_reviews"] = df["num_reviews"].fillna(0)

    df["num_reviews"] = df["num_reviews"].astype(int)

    logger.info(
        f"num_reviews cleaner successfully. "
        f"num_reviews nulls: {df['num_reviews'].isna().sum()}"
    )

    return df


def clean_piece_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean piece_count:
        - convert to int
    """

    logger.info("Cleaning piece_count...")

    df["piece_count"] = pd.to_numeric(df["piece_count"], errors="coerce")

    df["piece_count"] = df["piece_count"].astype(int)

    logger.info(
        f"piece_count cleaner successfully. "
        f"piece_count nulls: {df['piece_count'].isna().sum()}"
    )

    return df


def clean_prod_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean prod_id:
        - convert to int
    """

    logger.info("Cleaning prod_id...")

    df["prod_id"] = pd.to_numeric(df["prod_id"], errors="coerce")

    df["prod_id"] = df["prod_id"].astype(int)

    logger.info(
        f"prod_id cleaner successfully. " f"prod_id nulls: {df['prod_id'].isna().sum()}"
    )

    return df
