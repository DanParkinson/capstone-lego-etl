from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("data/output")


def load_table(table_name: str) -> pd.DataFrame:
    """
    Load a table from local output folder
    """

    path = OUTPUT_DIR / table_name

    if not path.exists():
        raise FileNotFoundError(f"Table not found: {path}")

    return pd.read_csv(path)
