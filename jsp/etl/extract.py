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

    Raises:
        FileNotFoundError:
            If the .CSV file or directory is not found.
        PermissionError:
            If there is a permission error accessing the .CSV file.
        pd.errors.EmptyDataError:
            If the .CSV file is empty.
        pd.errors.ParserError:
            If there is an error parsing the .CSV file.

    Returns:
        pd.DataFrame: The data extracted from the .CSV file.
    """
    try:
        data_frame = pd.read_csv(csv_file_path)
        return data_frame
    except FileNotFoundError as error:
        raise error
    except PermissionError as error:
        raise error
    except pd.errors.EmptyDataError as error:
        raise error
    except pd.errors.ParserError as error:
        raise error
