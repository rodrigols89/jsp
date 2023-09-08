# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Tests to "extract.p"y module."""

from __future__ import annotations

import os

import pandas as pd
import pytest

from jsp.etl.extract import extract_data_from_csv


def test_extract_data_from_csv() -> None:
    """
    Tests for extracting data from a .CSV file.
    """
    # Arrange = Create a fake .CSV file.
    data = {
        "Name": ["John", "Maria", "Peter", "Ana", "Marta"],
        "Age": [25, 30, 22, 28, 35],
        "City": [
            "Sao Paulo",
            "Rio de Janeiro",
            "Belo Horizonte",
            "Porto Alegre",
            "Salvador",
        ],
    }
    df = pd.DataFrame(data)
    file_path = "./tests/etl/fake_data.csv"
    df.to_csv(file_path, index=False)

    # Assert that the data is a DataFrame.
    assert isinstance(df, pd.DataFrame)

    # Act + Assert
    # Check if the extracted DataFrame is equal to fake DataFrame.
    assert extract_data_from_csv(file_path).equals(df)

    # Cleanup = Remove fake .CSV file.
    os.remove(file_path)


def test_extract_data_from_csv_FileNotFoundError() -> None:
    """
    Test for FileNotFoundError when extracting
    data from a non-existent CSV file.
    """
    with pytest.raises(FileNotFoundError):
        extract_data_from_csv("nonexistent.csv")


def test_extract_data_from_csv_PermissionError() -> None:
    """
    Test function to check if a PermissionError is raised when
    extracting data from a .CSV file with not permission.
    """
    # Arrange = Create a fake .CSV file.
    file_path = "./tests/etl/fake_data.csv"
    with open(file_path, "w"):
        pass  # Does nothing, just creates the file
    os.chmod(file_path, 0)  # Set the file permissions to 0 (no permissions)

    # Act + Assert.
    with pytest.raises(PermissionError):
        extract_data_from_csv(file_path)

    # Cleanup.
    os.remove(file_path)


def test_extract_data_from_csv_EmptyDataError() -> None:
    """
    Test for EmptyDataError when extracting.
    That's, raise when receives an empty DataFrame.
    """
    # Arrange = Create a empty fake DataFrame.
    file_path = "./tests/etl/fake_data.csv"
    with open(file_path, "w"):
        pass  # Does nothing, just creates the file

    # Act + Assert.
    with pytest.raises(pd.errors.EmptyDataError):
        extract_data_from_csv(file_path)

    # Cleanup.
    os.remove(file_path)


def test_extract_data_from_csv_ParserError() -> None:
    # Arrange = Create a fake .CSV file.
    data = """
        vers    2.1.0       computer
        info    days    6
        info,    x       a
        info    y       b
    """
    file_path = "./tests/etl/fake_data.csv"
    with open(file_path, "w") as file:
        file.write(data)

    # Act + Assert.
    with pytest.raises(pd.errors.ParserError):
        extract_data_from_csv(file_path)

    # Cleanup.
    os.remove(file_path)
