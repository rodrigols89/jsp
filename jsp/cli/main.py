# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""The entry point to CLI application."""
from __future__ import annotations

import typer

from jsp.cli import etl

app = typer.Typer(
    add_completion=False,
    help="CLI application for the JSP project. E.g. ETL process.",
)

app.add_typer(etl.app, name="etl")

if __name__ == "__main__":
    app()
