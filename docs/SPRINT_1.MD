# User Story 1 – Data Acquisition, Extraction & Validation  
## Fetch LEGO Dataset via Kaggle API

### Overview
User Story 1 focused on implementing the **data acquisition stage** of the ETL pipeline. The goal was to fetch the LEGO dataset from Kaggle, store it in the local raw data directory, and load it into a pandas DataFrame for further processing. This story also required full unit test coverage for each component of the extraction process.

---

## Workflow Summary

### `run_etl.py`
- Acts as the main entry point for the ETL process.
- Triggers the extraction workflow by calling into `extract.py`.

---

### `extract.py`
Responsible for orchestrating the extraction flow:

- Checks whether the raw CSV file already exists locally.
- If the file exists:
  - Logs that the local file will be used.
  - Sends the file path to `extract_lego.py` for DataFrame creation.
- If the file does **not** exist:
  - Calls `kaggle_downloader.py` to fetch the dataset from Kaggle.
  - Renames the downloaded file to the expected RAW_FILE path.
  - Passes the resulting CSV path to `extract_lego.py`.

---

### `kaggle_downloader.py`
Handles communication with the Kaggle API:

- Authenticates via the Kaggle API.
- Downloads the target dataset defined in the `DATASET` constant.
- Extracts and stores files into `RAW_DIR`.
- Searches the extracted files for a `.csv` file.
- Returns the CSV file path back to `extract.py`.

---

### `extract_lego.py`
Responsible for DataFrame creation:

- Accepts a file path returned from `kaggle_downloader.py` or passed by `extract.py`.
- Loads the CSV into a pandas DataFrame.
- Logs performance metrics and dataset shape.
- Returns the DataFrame to the calling module.

---

## Testing Completed

Unit tests were written and executed for all major behaviours:

### **extract_lego.py**
- Confirms that `extract_lego_data()`:
  - Calls `pd.read_csv()` with the supplied file path.
  - Returns a pandas DataFrame.

### **kaggle_downloader.py**
- Authentication is initiated once.
- Kaggle API download method is called correctly.
- Downloader returns the correct CSV file path.
- Proper error is raised when no CSV file is found.

### **extract.py**
- Confirms that:
  - A DataFrame is returned after the extraction pipeline completes.
  - Existing local files bypass the download step.
  - Missing files trigger Kaggle download before extraction.

---

## Status
**User Story 1 is now complete.**  
Next onto User story 2 where we will check the dataframe matches big metrics of the original file such as column names, amount of rows etc.
