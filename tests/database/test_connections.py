# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
"""Tests to "connections.p"y module."""
from __future__ import annotations

from sqlalchemy.engine import Engine

from jsp.database.connections import get_engine_connection


def test_get_engine_connection_custom_arguments(
    default_database_arguments,
) -> None:
    """Test fake custom arguments."""
    engine = get_engine_connection(**default_database_arguments)
    assert isinstance(engine, Engine)
    expected_str = "Engine(postgresql://myusername:***@localhost:5432/mydb)"
    assert str(engine) == expected_str
