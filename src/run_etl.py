from src.extract.extract import extract_data
from src.utils.raw_validation import validate_raw_lego_data
from src.transform.transform import transform_data
from src.utils.clean_validation import validate_clean_lego_data
from src.load.load_clean import save_clean_data
from src.load.load import create_tables


def run():
    # Extract data
    df_raw = extract_data()
    validate_raw_lego_data(df_raw)
    # clean data
    df_clean = transform_data(df_raw)
    validate_clean_lego_data(df_clean)
    # save cleaned data
    save_clean_data(df_clean, "lego_clean.csv")

    # load RDS
    create_tables(df_clean)


if __name__ == "__main__":
    run()
