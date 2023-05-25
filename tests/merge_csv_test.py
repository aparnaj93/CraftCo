import pytest

from merge_csv import read_file, merge_dataframes


def test_read_file():
    df = read_file("tests/resources/test1.csv")
    expected_columns = ["ID", "SCORE"]
    assert df.columns.tolist() == expected_columns


def test_merge_dataframes():
    df1 = read_file("tests/resources/test1.csv")
    df2 = read_file("tests/resources/test2.csv")
    merged_df = merge_dataframes(df1, df2, "ID")
    expected_merged_columns = ["ID", "SCORE", "NAME"]
    assert merged_df.columns.tolist() == expected_merged_columns


def test_merge_column_does_not_exist():
    with pytest.raises(Exception):
        df1 = read_file("tests/resources/test1.csv")
        df2 = read_file("tests/resources/test2.csv")
        merge_dataframes(df1, df2, "non-existing-column")
