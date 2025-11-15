# src/load.py
import pandas as pd
from pathlib import Path


def load(df: pd.DataFrame, output_path: str = "data/processed_properties.csv") -> None:
    """Write the DataFrame to a CSV file."""
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"[load] Saved {len(df)} rows to: {out_path.resolve()}")
