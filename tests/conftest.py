from __future__ import annotations

import pytest


@pytest.fixture
def default_database_arguments():
    engine_dict = {
        "dialect": "postgresql",
        "username": "myusername",
        "password": "mypass",
        "database": "mydb",
        "host": "localhost",
        "port": 5432,
    }
    yield engine_dict
