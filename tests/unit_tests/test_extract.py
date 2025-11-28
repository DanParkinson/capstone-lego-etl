import pandas as pd
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock


from src.extract.extract_lego import extract_lego_data
from src.extract.kaggle_downloader import download_kaggle_csv, DATASET, RAW_DIR
from src.extract.extract import extract_data, RAW_FILE
from src.utils.raw_validation import validate_raw_lego_data, EXPECTED_COLUMNS


# ===============
# Extract_Lego.py
# ===============
@patch("src.extract.extract_lego.pd.read_csv")
def test_extract_lego_data_returns_dataframe(mock_read_csv):
    """
    Test: extract_lego_data() loads CSV and returns a DataFrame
    """
    # Arrange
    mock_df = pd.DataFrame({"col1": [1], "col2": [2]})
    mock_read_csv.return_value = mock_df
    file_path = Path("data/raw/fake.csv")

    # Act
    df = extract_lego_data(file_path)

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert df.equals(mock_df)


# ===============
# Kaggle_Downloader.py
# ===============
@patch("src.extract.kaggle_downloader.Path.glob")
@patch("src.extract.kaggle_downloader.KaggleApi")
def test_kaggle_downloader_authentication(mock_api_cls, mock_glob):
    """
    Test: kaggle_downloader inititates API and authenticates
    """
    # Arrange
    mock_glob.return_value = [Path("data/raw/fake.csv")]
    mock_api = MagicMock()
    mock_api_cls.return_value = mock_api

    # Act
    download_kaggle_csv()

    # assert
    mock_api.authenticate.assert_called_once()


@patch("src.extract.kaggle_downloader.Path.glob")
@patch("src.extract.kaggle_downloader.KaggleApi")
def test_kaggle_downloader_download_called(mock_api_cls, mock_glob):
    """
    Test: kaggle_downloader correctly requests download
    """
    # Arrange
    mock_glob.return_value = [Path("data/raw/fake.csv")]
    mock_api = MagicMock()
    mock_api_cls.return_value = mock_api

    # Act
    download_kaggle_csv()

    # Assert
    mock_api.dataset_download_files.assert_called_once_with(
        DATASET, path=str(RAW_DIR), unzip=True
    )


@patch("src.extract.kaggle_downloader.Path.glob")
@patch("src.extract.kaggle_downloader.KaggleApi")
def test_kaggle_downloader_returned_csv_path(mock_api_cls, mock_glob):
    """
    Test: Check that the the correct CSV path is returned
    """
    mock_glob.return_value = [Path("data/raw/fake.csv")]
    mock_api = MagicMock()
    mock_api_cls.return_value = mock_api()

    csv_path = download_kaggle_csv()

    assert csv_path == Path("data/raw/fake.csv")


@patch("src.extract.kaggle_downloader.Path.glob")
@patch("src.extract.kaggle_downloader.KaggleApi")
def test_kaggle_downloader_return_error_for_no_csv(mock_api_cls, mock_glob):
    """
    Test: Check for errors if no CSV is present
    """
    # Arrange
    mock_glob.return_value = []
    mock_api = MagicMock()
    mock_api_cls.return_value = mock_api

    # Act and Assert
    with pytest.raises(FileNotFoundError):
        download_kaggle_csv()


# ===============
# Extract.py
# Needs
# Data skips download when file exists
# Data downloads when file missing
# ===============
@patch("src.extract.extract.RAW_FILE")
@patch("src.extract.extract.extract_lego_data")
def test_extract_data_returns_dataframe(mock_extract_lego_data, mock_raw):
    """
    Test: extract_data returns csv as df
    """
    # Arrange
    mock_raw.exists.return_value = True
    mock_df = pd.DataFrame({"col1": [1], "col2": [2]})
    mock_extract_lego_data.return_value = mock_df

    # Act
    result = extract_data()

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.equals(mock_df)


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
