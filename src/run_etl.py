from src.extract.extract import extract_data
from src.utils.raw_validation import validate_raw_lego_data
from src.transform.transform import transform_data
from src.utils.clean_validation import validate_clean_lego_data


def run():
    df = extract_data()
    validate_raw_lego_data(df)
    df = transform_data(df)
    validate_clean_lego_data(df)

    df.to_csv("data/processed/lego_clean.csv", index=False)


if __name__ == "__main__":
    run()
