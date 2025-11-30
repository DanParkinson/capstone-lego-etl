import pandas as pd
import pytest

from src.utils.clean_validation import validate_clean_lego_data


def valid_df():
    return pd.DataFrame(
        {
            "list_price": [9.99, 12.50],
            "star_rating": [4.5, 4.0],
            "val_star_rating": [4.7, 4.2],
            "age_min": [6.0, 8.0],
            "age_max": [12.0, 14.0],
            "num_reviews": [50, 100],
            "piece_count": [100, 200],
            "prod_id": pd.Series([1234, 5678], dtype="Int64"),
            "prod_desc": ["desc1", "desc2"],
            "prod_long_desc": ["long1", "long2"],
            "set_name": ["set1", "set2"],
            "theme_name": ["theme1", "theme2"],
            "review_difficulty": ["easy", "average"],
            "country": ["US", "UK"],
        }
    )


def test_validate_clean_data_passes_for_valid_df():
    """
    Test it works:
        - Should not raise error
    """
    df = valid_df()
    validate_clean_lego_data(df)


def test_validate_clean_data_fails_for_non_float_column():
    """
    Test float columns:
        - Change expected float to string
        - should raise error
    """
    df = valid_df()
    df["list_price"] = df["list_price"].astype(str)
    with pytest.raises(TypeError):
        validate_clean_lego_data(df)


def test_validate_clean_data_fails_for_non_int_column():
    """
    Test int columns:
        - Change expected int to float
        - should raise error
    """
    df = valid_df()
    df["num_reviews"] = df["num_reviews"].astype(float)
    with pytest.raises(TypeError):
        validate_clean_lego_data(df)


def test_validate_clean_data_fails_for_null_text_column():
    """
    Test text columns:
        - Put in null value
        - should raise error
    """
    df = valid_df()
    df.loc[0, "prod_desc"] = None
    with pytest.raises(ValueError):
        validate_clean_lego_data(df)


def test_validate_clean_data_fails_for_non_string_text_column():
    """
    Test text columns:
        - Change strings to ints
        - should raise error
    """
    df = valid_df()
    df["theme_name"] = [1, 2]
    with pytest.raises(TypeError):
        validate_clean_lego_data(df)
