import pandas as pd


from src.transform.transform_numeric import (
    clean_ages,
    clean_list_price,
    clean_num_reviews,
    clean_piece_count,
    clean_prod_id,
)


# ==============
# test_age
# ==============
def test_clean_age_range():
    """
    Test age ranges are split up 6-12 -> "6" "12"
    """

    # Arrange
    df = pd.DataFrame({"ages": ["6-12", "10-16"]})

    # Act
    result = clean_ages(df)

    # Assert
    assert result.loc[0, "age_min"] == 6
    assert result.loc[0, "age_max"] == 12

    assert result.loc[1, "age_min"] == 10
    assert result.loc[1, "age_max"] == 16


def test_clean_age_plus():
    """
    Test + values. 6+ -> "6" "99"
    """
    df = pd.DataFrame({"ages": ["6+", "12+"]})

    result = clean_ages(df)

    assert result.loc[0, "age_min"] == 6
    assert result.loc[0, "age_max"] == 99

    assert result.loc[1, "age_min"] == 12
    assert result.loc[1, "age_max"] == 99


def test_clean_age_fractional():
    """
    Test fractions become decimals
    """
    df = pd.DataFrame({"ages": ["1½-3"]})

    result = clean_ages(df)

    assert result.loc[0, "age_min"] == 1.5
    assert result.loc[0, "age_max"] == 3


# def test_clean_age_invalid():
#     df = pd.DataFrame({"ages": ["unknown", None, "invalid"]})

#     result = clean_ages(df)

#     assert result["age_min"].isna().all()
#     assert result["age_max"].isna().all()


# ==============
# test_list_price
# ==============
def test_list_price_converts_to_float():
    """
    clean_list_price should convert values to float.
    """
    # Arrange
    df = pd.DataFrame({"list_price": ["29.99", "19.50", "40"]})

    # Act
    cleaned = clean_list_price(df)

    # Assert
    assert cleaned["list_price"].dtype == "float64"
    assert cleaned["list_price"].tolist() == [29.99, 19.50, 40.00]


def test_list_price_rounds_values():
    """
    clean_list_price should round values to 2 decimals.
    """
    df = pd.DataFrame({"list_price": [12.9999, 5.6789]})

    cleaned = clean_list_price(df)

    assert cleaned["list_price"].tolist() == [13.00, 5.68]


# ==============
# test_num_reviews
# ==============
def test_num_reviews_converts_to_int():
    """
    clean_num_reviews should convert values to int.
    """
    df = pd.DataFrame({"num_reviews": ["2", "15", "40.0"]})

    cleaned = clean_num_reviews(df)

    assert cleaned["num_reviews"].dtype == "int64"
    assert cleaned["num_reviews"].tolist() == [2, 15, 40]


def test_num_reviews_replaces_nan_with_zero():
    """
    clean_num_reviews should replace NaN values with 0.
    """
    df = pd.DataFrame({"num_reviews": [10, None, float("nan")]})

    cleaned = clean_num_reviews(df)

    assert cleaned["num_reviews"].tolist() == [10, 0, 0]


# ==============
# test_piece_count
# ==============
def test_piece_count_converts_to_int():
    """
    clean_piece_count should convert values to int.
    """
    df = pd.DataFrame({"piece_count": ["2", "15", "40.0"]})

    cleaned = clean_piece_count(df)

    assert cleaned["piece_count"].dtype == "int64"
    assert cleaned["piece_count"].tolist() == [2, 15, 40]


# ==============
# test_prod_id
# ==============
def test_prod_id_converts_to_int():
    """
    clean_prod_id should convert values to int.
    """
    df = pd.DataFrame({"prod_id": ["2", "15", "40.0"]})

    cleaned = clean_prod_id(df)

    assert cleaned["prod_id"].dtype == "int64"
    assert cleaned["prod_id"].tolist() == [2, 15, 40]
