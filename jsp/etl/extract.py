# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with ETL 'extract'."""

from __future__ import annotations

import pandas as pd


def extract_data_from_csv(csv_file: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The data extracted from the .CSV file.
    """
    df = pd.read_csv(csv_file)
    return df
