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

    # Authentication
    try:
        api.authenticate()
    except Exception as e:
        logger.error("Kaggle authentication failed.")
        raise RuntimeError(f"Kaggle authentication failed: {e}")

    # Download
    logger.info(f"Downloading {DATASET} into{RAW_DIR}")
    try:
        api.dataset_download_files(DATASET, path=str(RAW_DIR), unzip=True)
    except Exception as e:
        logger.error("Kaggle dataset download failed.")
        raise RuntimeError(f"Kaggle dataset download failed: {e}")

    # Locate CSV
    csv_files = list(RAW_DIR.glob("*.csv"))
    if not csv_files:
        logger.error("No CSV found after Kaggle download")
        raise FileNotFoundError("No CSV found after Kaggle download.")

    csv_path = csv_files[0]
    logger.info(f"Found CSV file: {csv_files[0]}")

    return csv_path
