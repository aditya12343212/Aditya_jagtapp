# src/extract.py
import json
import os        # ← ADD THIS LINE
from pathlib import Path
from typing import Optional

import pandas as pd


def extract(json_file_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load the raw property JSON file and return a normalised DataFrame.
    """
    # ---------- 1. Resolve the path ----------
    if json_file_path:
        file_path = Path(json_file_path)
    elif env_path := Path(os.getenv("JSON_FILE", "")):  # ← now os is defined
        file_path = env_path
    else:
        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "data" / "fake_property_data_new.json"

    file_path = file_path.resolve()

    # ---------- 2. Safety ----------
    if not file_path.exists():
        raise FileNotFoundError(
            f"JSON file not found:\n  {file_path}\n"
            "  • Is 'fake_property_data_new.json' in the 'data/' folder?\n"
            "  • Run from project root: C:\\...\\data_engineer_assessment"
        )

    print(f"[extract] Loading: {file_path}")

    # ---------- 3. Load ----------
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    print(f"[extract] Shape: {df.shape}")
    return df