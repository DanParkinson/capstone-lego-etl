import pandas as pd
from pathlib import Path
from src.utils.logging_utils import setup_logger, log_extract_success
import timeit

logger = setup_logger("extract_lego", "extract.log")

EXPECTED_PERFORMANCE = 0.0001


def extract_lego_data(file_path: Path) -> pd.DataFrame:
    start = timeit.default_timer()

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"Failed to read CSV from {file_path}.")
        raise RuntimeError(f"Failed to read CSV file: {file_path}: {e}")

    duration = timeit.default_timer() - start
    log_extract_success(
        logger, "LEGO Dataset", df.shape, duration, EXPECTED_PERFORMANCE
    )

    return df
