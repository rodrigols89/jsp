# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to work with Database connections."""
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine_connection(
    dialect: str = "postgresql",
    username: str = "postgres",
    password: str = "postgres",
    database: str = "jsp-db",
    host: str = "localhost",
    port: int = 5432,
) -> Engine:
    """
    Create a SQLAlchemy Engine connection.

    Args:
        dialect (str, optional):
            The database dialect. Defaults to "postgresql".
        username (str, optional):
            The database username. Defaults to "postgres".
        password (str, optional):
            The database password. Defaults to "postgres".
        database (str, optional):
            Name of the database. Defaults to "jsp-db".
        host (str, optional):
            The database host. Defaults to "localhost".
        port (int, optional):
            The database port. Defaults to 5432.

    Returns:
        Engine: A SQLAlchemy Engine object.

    Example:
        >>> engine = get_engine_connection()
        >>> print(engine)
        Engine(postgresql://postgres:***@localhost:5432/jsp-db)
    """
    connection_url = (
        f"{dialect}://{username}:{password}@{host}:{port}/{database}"
    )
    engine = create_engine(connection_url, echo=False)
    return engine
