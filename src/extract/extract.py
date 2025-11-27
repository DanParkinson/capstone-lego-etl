from pathlib import Path
from src.extract.kaggle_downloader import download_kaggle_csv
from src.extract.extract_lego import extract_lego_data
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract", "extract.log")

# Constants
RAW_FILE = Path("data/raw/lego_sets_raw.csv")


def extract_data():
    """
    Orchestrates extraction:
    - Checks if raw CSV exists.
    - Downloads from Kaggle if missing
    - Loads dataframe from CSV
    """

    logger.info("Starting Extraction Pipeline...")

    if RAW_FILE.exists():
        logger.info("Raw Lego CSV found Locally - skipping download.")
        csv_path = RAW_FILE
    else:
        logger.info("Raw LEGO CSV Not Found - Downloading from Kaggle.")
        download_path = download_kaggle_csv()
        download_path.rename(RAW_FILE)
        csv_path = RAW_FILE

    df = extract_lego_data(csv_path)

    logger.info("Extraction Pipeline Completed Successfully.")
    return df
