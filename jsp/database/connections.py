# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with Database connections."""
from __future__ import annotations

from sqlalchemy import Engine, create_engine


def get_engine_connection(
    dialect: str,
    username: str,
    password: str,
    database: str,
    host: str,
    port: int,
) -> Engine:
    """
    Create a SQLAlchemy Engine connection.

    Args:
        dialect (str): The database dialect (e.g., "postgresql").
        username (str): The database username.
        password (str): The database password.
        database (str): The name of the database
        host (str): The database host.
        port (int): The database port.

    Returns:
        Engine: A SQLAlchemy Engine object.
    """
    engine = create_engine(
        f"{dialect}://{username}:{password}@{host}:{port}/{database}",
        echo=False,
    )
    return engine
