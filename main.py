# src/main.py
from extract import extract
from transform import transform
from load import load


def run_pipeline():
    # No argument → auto-detects the correct file
    raw_df = extract()

    cleaned_df = transform(raw_df)

    load(cleaned_df)


if __name__ == "__main__":
    run_pipeline()
