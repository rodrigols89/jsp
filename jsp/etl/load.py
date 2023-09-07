# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with ETL 'Load'."""


from __future__ import annotations

import pandas as pd

from jsp.database.connections import get_engine_connection
from jsp.etl.extract import extract_data_from_csv


def load_data_to_postgresql(table_name: str, dataframe: pd.DataFrame) -> None:
    """
    Load data from a pandas DataFrame into a PostgreSQL table.

    Args:
        table_name (str): The name of the PostgreSQL table.
        dataframe (pd.DataFrame): The pandas DataFrame containing the data.

    Returns:
        None
    """
    with get_engine_connection().connect() as connection:
        dataframe.to_sql(
            table_name, connection, if_exists="replace", index=False
        )


def load_train_df_to_postgresql() -> None:
    """
    Loads the TRAIN data from a .CSV file into a PostgreSQL database table.
    """
    print("Loading train data into PostgreSQL database...")
    train_df = extract_data_from_csv("jsp/datalake/landing/Train_rev1.csv")
    load_data_to_postgresql("train-table", train_df)
    print("Train data loaded successfully.")


def load_test_df_to_postgresql() -> None:
    """
    Loads the TEST data from a .CSV file into a PostgreSQL database table.
    """
    print("Loading test data into PostgreSQL database...")
    test_df = extract_data_from_csv("jsp/datalake/landing/Test_rev1.csv")
    load_data_to_postgresql("test-table", test_df)
    print("Test data loaded successfully.")
