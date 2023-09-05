# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with ETL 'Load'."""


from __future__ import annotations

import pandas as pd

from jsp.database.connections import get_engine_connection


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
