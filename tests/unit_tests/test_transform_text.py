import pandas as pd
from src.transform.transform_text import (
    clean_prod_desc,
    clean_prod_long_desc,
    clean_review_difficulty,
    clean_set_name,
    clean_theme_name,
    clean_country,
)


# ===============
# clean_prod_desc
# ===============
def test_clean_prod_desc_fills_nulls():
    """
    clean_prod_desc should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"prod_desc": [None]})

    result = clean_prod_desc(df)

    assert result.loc[0, "prod_desc"] == "No description available"


def test_clean_prod_desc_ensures_string_type():
    """
    clean_prod_desc should convert values to string.
    """
    df = pd.DataFrame({"prod_desc": [123]})

    result = clean_prod_desc(df)

    assert isinstance(result.loc[0, "prod_desc"], str)
    assert result.loc[0, "prod_desc"] == "123"


# ===============
# clean_prod_long_desc
# ===============
def test_clean_prod_long_desc_fills_nulls():
    """
    clean_prod_long_desc should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"prod_long_desc": [None]})

    result = clean_prod_long_desc(df)

    assert result.loc[0, "prod_long_desc"] == "No long description available"


def test_clean_prod_long_desc_ensures_string_type():
    """
    clean_prod_long_desc should convert values to string.
    """
    df = pd.DataFrame({"prod_long_desc": [123]})

    result = clean_prod_long_desc(df)

    assert isinstance(result.loc[0, "prod_long_desc"], str)
    assert result.loc[0, "prod_long_desc"] == "123"


# ===============
# clean_review_difficulty
# ===============
def test_clean_review_difficulty_fills_nulls():
    """
    clean_review_difficulty should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"review_difficulty": [None]})

    result = clean_review_difficulty(df)

    assert result.loc[0, "review_difficulty"] == "unrated"


def test_clean_review_difficulty_ensures_string_type():
    """
    clean_review_difficulty should convert values to string.
    """
    df = pd.DataFrame({"review_difficulty": [123]})

    result = clean_review_difficulty(df)

    assert isinstance(result.loc[0, "review_difficulty"], str)
    assert result.loc[0, "review_difficulty"] == "123"


def test_clean_review_difficulty_converts_to_lowercase():
    """
    clean_review_difficulty should convert text to lowercase.
    """
    df = pd.DataFrame({"review_difficulty": ["Easy"]})

    result = clean_review_difficulty(df)

    assert result.loc[0, "review_difficulty"] == "easy"


# ===============
# clean_set_name
# ===============
def test_clean_set_name_fills_nulls():
    """
    clean_set_name should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"set_name": [None]})

    result = clean_set_name(df)

    assert result.loc[0, "set_name"] == "Unknown Set Name"


def test_clean_set_name_ensures_string_type():
    """
    clean_set_name should convert values to string.
    """
    df = pd.DataFrame({"set_name": [123]})

    result = clean_set_name(df)

    assert isinstance(result.loc[0, "set_name"], str)
    assert result.loc[0, "set_name"] == "123"


# ===============
# clean_theme_name
# ===============
def test_clean_theme_name_fills_nulls():
    """
    clean_theme_name should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"theme_name": [None]})

    result = clean_theme_name(df)

    assert result.loc[0, "theme_name"] == "Unknown Theme"


def test_clean_theme_name_ensures_string_type():
    """
    clean_theme_name should convert values to string.
    """
    df = pd.DataFrame({"theme_name": [999]})

    result = clean_theme_name(df)

    assert isinstance(result.loc[0, "theme_name"], str)
    assert result.loc[0, "theme_name"] == "999"


# ===============
# clean_country
# ===============
def test_clean_country_fills_nulls():
    """
    clean_country should replace NaN with the placeholder text.
    """
    df = pd.DataFrame({"country": [None]})

    result = clean_country(df)

    assert result.loc[0, "country"] == "Unknown"


def test_clean_country_ensures_string_type():
    """
    clean_country should convert values to string.
    """
    df = pd.DataFrame({"country": [123]})

    result = clean_country(df)

    assert isinstance(result.loc[0, "country"], str)
    assert result.loc[0, "country"] == "123"
