from pathlib import Path
import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("table_writer", "load.log")

OUTPUT_DIR = Path("data/output")


def write_table(
    df: pd.DataFrame,
    columns: list,
    output_name: str,
    deduplication_key,
    add_surrogate_id: str | None = None,
) -> pd.DataFrame:
    """
    Reusable table creation for RDS
    """

    logger.info(f"Creating table: {output_name}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # deduplication key and be string or list
    subset = (
        deduplication_key
        if isinstance(deduplication_key, list)
        else [deduplication_key]
    )

    # select columns
    df = df[columns].copy()

    # drop duplicates
    df = df.drop_duplicates(subset=subset)

    # secodnary key for creating ids for star schema stuff
    if add_surrogate_id:
        df = df.sort_values(by=subset).reset_index(drop=True)
        df[add_surrogate_id] = df.index + 1

    # save CSV
    output_path = OUTPUT_DIR / output_name
    df.to_csv(output_path, index=False)

    logger.info(
        f"Table {output_name} created with {len(df)} rows " f"Saved to {output_path}"
    )

    return df
