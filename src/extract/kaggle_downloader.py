from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from src.utils.logging_utils import setup_logger

logger = setup_logger("kaggle_downloader", "extract.log")

RAW_DIR = Path("data/raw")
DATASET = "mterzolo/lego-sets"


def download_kaggle_csv() -> Path:
    """
    Downloads and unzips the LEGO dataset from kaggle into RAW_DIR
    returns the path to the csv file.
    """

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Authenticating with KAGGLE API...")
    api = KaggleApi()
    api.authenticate()

    logger.info(f"Downloading {DATASET} into{RAW_DIR}")
    api.dataset_download_files(DATASET, path=str(RAW_DIR), unzip=True)

    # After Unzip find the csv file
    csv_files = list(RAW_DIR.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV found after Kaggle download.")

    logger.info(f"Found CSV file: {csv_files[0]}")
    return csv_files[0]
