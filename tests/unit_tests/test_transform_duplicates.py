import pandas as pd
from src.transform.transform_duplicates import clean_duplicates


def test_clean_duplicates_removes_null_primary_keys():
    """
    Rows with null prod_id or country must be removed.
    """

    # Arrange
    df = pd.DataFrame({"prod_id": [1, None, 2], "country": ["US", "UK", None]})

    # Act
    result = clean_duplicates(df)

    # Assert
    assert len(result) == 1
    assert result.iloc[0]["prod_id"] == 1
    assert result.iloc[0]["country"] == "US"


def test_clean_duplicates_keeps_valid_multi_country_rows():
    """
    Same prod_id but different countries are valid and must NOT be removed.
    """
    # Arrange
    df = pd.DataFrame({"prod_id": [1, 1], "country": ["US", "UK"]})

    # Act
    result = clean_duplicates(df)

    # Assert
    assert len(result) == 2
