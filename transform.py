# src/transform.py
import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Example: clean column names, drop duplicates, etc."""
    df = df.copy()
    # Lower-case column names and replace spaces with underscores
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates()
    print(f"[transform] Cleaned DataFrame shape: {df.shape}")
    return df
