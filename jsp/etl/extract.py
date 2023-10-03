# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with ETL 'extract'."""

from __future__ import annotations

import pandas as pd


def extract_data_from_csv(csv_file_path: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The data extracted from the .CSV file.
    """
    data_frame = pd.read_csv(csv_file_path)
    return data_frame
