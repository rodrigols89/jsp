# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
"""Tests to "connections.p"y module."""
from __future__ import annotations

import pytest
import sqlalchemy
from sqlalchemy.engine import Engine

from jsp.database.connections import get_engine_connection


def test_get_engine_connection_default_arguments() -> None:
    """
    Test for checking the default arguments
    of get_engine_connection() function.
    """
    engine = get_engine_connection()
    assert engine.url.drivername == "postgresql"
    assert engine.url.username == "postgres"
    assert engine.url.password == "postgres"
    assert engine.url.host == "localhost"
    assert engine.url.port == 5432
    assert engine.url.database == "jsp-db"


def test_get_engine_connection_not_default_arguments(
    not_default_database_arguments: dict[str],
) -> None:
    """
    Test getting engine connection with non-default arguments.
    """
    engine = get_engine_connection(**not_default_database_arguments)
    assert isinstance(engine, Engine)
    expected_str = "Engine(postgresql://myusername:***@localhost:5432/mydb)"
    assert str(engine) == expected_str


def test_get_engine_connection_invalid_port_argument() -> None:
    """
    Test invalid port argument as literal.
    """
    with pytest.raises(ValueError):
        get_engine_connection(port="ABC")


def test_get_engine_connection_missing_drivers() -> None:
    """
    Test missing drivers modules using sqlalchemy.exc.NoSuchModuleError.
    """
    drivers = [
        # PostgreSQL Drivers.
        "psycopg2",
        "pg8000",
        # MySQL Drivers.
        "mysqldb",
        "mysqlconnector",
        # Oracle Drivers.
        "cx_oracle",
        # SQL Server Drivers.
        "pyodbc",
        "pymssql",
    ]
    for driver in drivers:
        with pytest.raises(sqlalchemy.exc.NoSuchModuleError):
            get_engine_connection(dialect="pyodbc")


def test_get_engine_connection_missing_dialect_argument() -> None:
    """
    Test missing dialect argument.
    """
    with pytest.raises(sqlalchemy.exc.ArgumentError):
        get_engine_connection(dialect="")


def test_get_engine_connection_invalid_dialects_as_number() -> None:
    """
    Test invalid dialects as number.
    """
    with pytest.raises(sqlalchemy.exc.NoSuchModuleError):
        get_engine_connection(dialect=102030)
