import pandas as pd
import sqlite3

conn = sqlite3.connect(r"./data/data.sqlite")


def test_cleaned_co2e_data():
    cleaned_co2e_data = pd.read_sql_query(
        "SELECT * FROM co2e_price_development", conn)

    assert len(cleaned_co2e_data.columns.values) == 3  # one column for index

    assert cleaned_co2e_data.columns.values[1] == "date"
    assert cleaned_co2e_data.columns.values[2] == "price"

    assert cleaned_co2e_data.dtypes.values[1] == "object"
    assert cleaned_co2e_data.dtypes.values[2] == "float64"
    
    assert cleaned_co2e_data["price"].min() >= 0.0

    print("All tests passed for co2e_price_development")


def test_cleaned_eutl_data():
    cleaned_eutl_data = pd.read_sql_query(
        "SELECT * FROM eu_transaction_log", conn)

    assert len(cleaned_eutl_data.columns.values) == 11  # one column for index

    assert "VERIFIED_EMISSIONS" in cleaned_eutl_data.columns.values
    assert "ALLOCATION" in cleaned_eutl_data.columns.values
    
    assert cleaned_eutl_data["VERIFIED_EMISSIONS"].min() >= -1.0
    assert cleaned_eutl_data["YEAR"].min() == 2008 and cleaned_eutl_data["YEAR"].max() >= 2023

    print("All tests passed for eu_transaction_log")


def main():
    test_cleaned_co2e_data()
    test_cleaned_eutl_data()


if __name__ == "__main__":
    main()
