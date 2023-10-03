# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to apply ETL commands."""
from __future__ import annotations

import typer

from jsp.etl.load import (
    load_test_df_to_postgresql,
    load_train_df_to_postgresql,
)

app = typer.Typer(help="Command to apply ETL processes.")


@app.command("load-train")
def load_train() -> None:
    """
    Loads train DataFrames into PostgreSQL.
    """
    load_train_df_to_postgresql()


@app.command("load-test")
def load_test() -> None:
    """
    Loads test data into PostgreSQL.
    """
    load_test_df_to_postgresql()


@app.command("load-all")
def load_all() -> None:
    """
    Loads all train and test data into PostgreSQL.
    """
    load_train()
    load_test()
