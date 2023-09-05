# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Testing file."""
from __future__ import annotations

# from jsp.database.connections import get_engine_connection
from jsp.etl.extract import extract_data_from_csv
from jsp.etl.load import load_data_to_postgresql

if __name__ == "__main__":
    pass

    """Testing connection."""
    # engine = get_engine_connection()
    # print("Testing connection:")
    # print("Returned value:", engine)
    # print("Returned value type:", type(engine))

    """Testing extract_data_from_csv() function."""
    train_df = extract_data_from_csv("jsp/datalake/landing/Train_rev1.csv")
    test_df = extract_data_from_csv("jsp/datalake/landing/Test_rev1.csv")
    # print(train_df)
    # print(test_df)

    """Testing load_data_to_postgresql() function."""
    load_data_to_postgresql("train-table", train_df)
    load_data_to_postgresql("test-table", test_df)
