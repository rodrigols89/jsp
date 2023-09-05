from __future__ import annotations

import pytest


@pytest.fixture
def not_default_database_arguments():
    engine_dict = {
        "dialect": "postgresql",
        "username": "myusername",
        "password": "mypassword",
        "database": "mydb",
        "host": "localhost",
        "port": 5432,
    }
    yield engine_dict
