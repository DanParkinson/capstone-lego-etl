import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("The Extraction Process")

st.subheader("Epic 1 — Data Acquisition, Extraction & Validation")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <div class="card">
        <h3>US1 — Fetch LEGO dataset via Kaggle API</h3>

        <p>
        As a developer, I want to fetch the LEGO dataset automatically from Kaggle 
        if the raw file does not exist, so that the ETL pipeline is reproducible.
        </p>

        <p><strong>Acceptance Criteria</strong></p>
        <ul>
            <li>Raw CSV downloads if missing</li>
            <li>If file already exists, ETL skips download and logs it</li>
            <li>Data loads into a pandas DataFrame</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
        <h3>US2 — Load Raw CSV into DataFrame</h3>

        <p>
        As a developer, I want to load the raw CSV into a DataFrame,
        so that I can inspect and validate the raw dataset.
        </p>

        <p><strong>Acceptance Criteria</strong></p>
        <ul>
            <li>DataFrame loads without errors</li>
            <li>Column names match expected structure</li>
            <li>Data types logged for reference</li>
            <li>Missing values summary logged</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Extraction Orchestrator — `extract.py`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Eliminate manual downloads</li>
        <li>Skip the download step if the CSV already exists locally</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Check whether <code>lego_sets_raw.csv</code> already exists</li>
        <li>If missing → download via Kaggle API</li>
        <li>Rename the downloaded file to a predictable filename</li>
        <li>Load the CSV into a DataFrame using <code>extract_lego_data()</code></li>
    </ul>

    <p>
    This simple orchestration keeps logic clean while relying on 
    well-structured helper modules to perform the work.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def extract_data():
    \"""
    Orchestrates extraction:
    - Checks if raw CSV exists.
    - Downloads from Kaggle if missing
    - Loads dataframe from CSV
    \"""

    logger.info("Starting Extraction Pipeline...")

    if RAW_FILE.exists():
        logger.info("Raw Lego CSV found Locally - skipping download.")
        csv_path = RAW_FILE
    else:
        logger.info("Raw LEGO CSV Not Found - Downloading from Kaggle.")
        download_path = download_kaggle_csv()
        download_path.rename(RAW_FILE)
        csv_path = RAW_FILE

    df = extract_lego_data(csv_path)

    logger.info("Extraction Pipeline Completed Successfully.")
    return df
    """,
        language="python",
    )

with col3:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 1</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
@patch("src.extract.extract.RAW_FILE")
@patch("src.extract.extract.extract_lego_data")
def test_extract_data_returns_dataframe(mock_extract_lego_data, mock_raw):
    \"""
    Test: extract_data returns csv as df
    \"""

    # Arrange
    mock_raw.exists.return_value = True
    mock_df = pd.DataFrame({"col1": [1], "col2": [2]})
    mock_extract_lego_data.return_value = mock_df

    # Act
    result = extract_data()

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.equals(mock_df)
    """,
        language="python",
    )

st.markdown("---")

st.markdown("## Kaggle Downloader — `kaggle_downloader.py`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Automate interaction with the Kaggle API</li>
        <li>Add error handling so failures are obvious and logged</li>
        <li>Return the path of the downloaded CSV for downstream functions</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Create the <code>data/raw</code> directory if missing</li>
        <li>Authenticate with the Kaggle API</li>
        <li>Download and unzip the dataset</li>
        <li>Locate the CSV file inside the raw folder</li>
        <li>Raise meaningful errors if anything goes wrong</li>
    </ul>

    <p>
    This module isolates all Kaggle-specific logic, keeping
    <code>extract.py</code> clean and readable.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def download_kaggle_csv() -> Path:
    \"""
    Downloads and unzips the LEGO dataset from kaggle into RAW_DIR
    returns the path to the csv file.
    \"""

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
        """,
        language="python",
    )

with col3:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 4</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
@patch("src.extract.kaggle_downloader.Path.glob")
@patch("src.extract.kaggle_downloader.KaggleApi")
def test_kaggle_downloader_authentication(mock_api_cls, mock_glob):
    \"""
    Test: kaggle_downloader initiates API and authenticates
    \"""

    # Arrange
    mock_glob.return_value = [Path("data/raw/fake.csv")]
    mock_api = MagicMock()
    mock_api_cls.return_value = mock_api

    # Act
    download_kaggle_csv()

    # Assert
    mock_api.authenticate.assert_called_once()
        """,
        language="python",
    )

st.markdown("---")

st.markdown("## Extract LEGO Data — `extract_lego.py`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Separate CSV reading into its own function for clarity and testing</li>
        <li>Log extraction success with dataset shape and performance</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Read the CSV from a given path</li>
        <li>Catch and surface lower-level I/O failures</li>
        <li>Record the extraction duration for performance monitoring</li>
        <li>Return a fully loaded pandas DataFrame</li>
    </ul>

    <p>
    Keeping extraction separate from orchestration makes the ETL modular 
    and easier to test.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def extract_lego_data(file_path: Path) -> pd.DataFrame:

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"Failed to read CSV from {file_path}.")
        raise RuntimeError(f"Failed to read CSV file: {file_path}: {e}")

    return df
        """,
        language="python",
    )

with col3:
    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 1</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
@patch("src.extract.extract_lego.pd.read_csv")
def test_extract_lego_data_returns_dataframe(mock_read_csv):
    \"""
    Test: extract_lego_data() loads CSV and returns a DataFrame
    \"""
    # Arrange
    mock_df = pd.DataFrame({"col1": [1], "col2": [2]})
    mock_read_csv.return_value = mock_df
    file_path = Path("data/raw/fake.csv")

    # Act
    df = extract_lego_data(file_path)

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert df.equals(mock_df)
        """,
        language="python",
    )

st.markdown("---")

st.markdown("## Raw Validation — `validate_raw_lego_data.py`")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="top")

with col1:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Thought Process</h3>

    <ul>
        <li>Ensure the raw dataset matches the structure expected by the ETL</li>
        <li>Fail fast if the Kaggle dataset ever changes</li>
        <li>Provide clear, early error messages for structural problems</li>
        <li>Warn about extra columns so unexpected data never goes unnoticed</li>
    </ul>

    <p>
    This stage protects the pipeline from breaking downstream
    by validating the shape of the input immediately.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Key Responsibilities</h3>

    <ul>
        <li>Check all expected columns are present</li>
        <li>Raise <code>ValueError</code> for missing columns</li>
        <li>Warn if extra columns appear in the dataset</li>
        <li>Log successful validation</li>
    </ul>

    <p>
    This guarantees that the pipeline always starts with predictable,
    well-structured data.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.code(
        """
def validate_raw_lego_data(df: pd.DataFrame) -> None:
    \"""
    Validates the raw LEGO dataset after extraction.

    Checks:
        - All expected columns are present
        - No expected columns are missing
    Warns:
        - Extra unexpected columns
    \"""

    # Check structure
    df_cols = set(df.columns)
    expected = set(EXPECTED_COLUMNS)

    missing_columns = expected - df_cols
    extra_columns = df_cols - expected

    if missing_columns:
        logger.error(f"Missing expected columns: {missing_columns}")
        raise ValueError(f"Missing expected columns: {missing_columns}")

    if extra_columns:
        logger.warning(f"Unexpected extra columns: {extra_columns}")

    logger.info("Raw data structure validated successfully.")
        """,
        language="python",
    )


with col3:

    st.markdown(
        """
    <div class="flexi-card">
    <h3>Tests completed: 2</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.code(
        """
def test_validate_raw_lego_data_structure_fails():
    \"""
    Test validation raises ValueError for incorrect column names.
    \"""

    df = pd.DataFrame(columns=["wrong", "columns"])

    with pytest.raises(ValueError):
        validate_raw_lego_data(df)
        """,
        language="python",
    )
