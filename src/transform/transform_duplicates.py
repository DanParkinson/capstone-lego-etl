import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("clean_duplicates", "transform.log")


def clean_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicated rows:
        - Drop rows with missing prod_id or country.
        - Drop duplicted rows based on composite key
        - Log row count change

    Returns:
        - Cleaned DataFrame
    """
    initial_rows = df.shape[0]

    # Remove empty prod_id and country
    corrupted_rows = df["prod_id"].isna() | df["country"].isna()
    corrupted_rows_count = corrupted_rows.sum()

    if corrupted_rows_count > 0:
        logger.warning(
            f"Removing {corrupted_rows_count} rows with null prod_id/country."
        )
        df = df[(df["prod_id"].notna()) & (df["country"].notna())]

    # Remove duplicates
    duplicated_rows_count = df.duplicated(subset=["prod_id", "country"]).sum()

    if duplicated_rows_count > 0:
        logger.info(f"Removing {duplicated_rows_count} duplicate_rows.")
        df = df.drop_duplicates(subset=["prod_id", "country"])

    # Log

    final_rows = df.shape[0]
    removed_rows = initial_rows - final_rows

    logger.info(
        f"Duplicate cleaning complete. "
        f"Rows before: {initial_rows}, after: {final_rows} "
        f"Removed: {removed_rows}"
    )

    return df
