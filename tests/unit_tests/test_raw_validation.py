import pandas as pd
import pytest

from src.utils.raw_validation import validate_raw_lego_data, EXPECTED_COLUMNS


# ===============
# src/utils/raw_validation.py
# ===============
def test_validate_raw_lego_data_structure_ok():
    """
    Test validation passes when columns match expected structure.
    """
    df = pd.DataFrame(columns=EXPECTED_COLUMNS)

    # Should not raise error
    validate_raw_lego_data(df)


def test_validate_raw_lego_data_structure_fails():
    """
    Test validation raises ValueError for incorrect column names.
    """

    df = pd.DataFrame(columns=["wrong", "columns"])

    with pytest.raises(ValueError):
        validate_raw_lego_data(df)
