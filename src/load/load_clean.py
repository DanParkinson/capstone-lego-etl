from pathlib import Path
import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("load_clean", "load.log")

PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def save_clean_data(df: pd.DataFrame, filename: str) -> Path:
    """
    Saves clean csv to data/processed
    """
    file_path = PROCESSED_DIR / filename
    df.to_csv(file_path, index=False)
    logger.info(f"Saved clean LEGO data: {file_path}")
    return file_path
