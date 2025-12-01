import pandas as pd

from src.load.write_tables import write_table


def test_write_table_selects_columns():
    df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})

    result = write_table(
        df=df,
        columns=["a", "c"],
        output_name="test.csv",
        deduplication_key="a",
        add_surrogate_id=None,
    )

    assert list(result.columns) == ["a", "c"]


def test_write_table_duplicates():

    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})

    result = write_table(
        df=df,
        columns=["a", "b"],
        output_name="test.csv",
        deduplication_key="a",
        add_surrogate_id=None,
    )

    assert len(result) == 2


def test_write_table_add_surrogate():
    df = pd.DataFrame({"a": ["a", "b", "c"]})

    result = write_table(
        df=df,
        columns=["a"],
        output_name="test.csv",
        deduplication_key="a",
        add_surrogate_id="id",
    )

    assert list(result["id"]) == [1, 2, 3]
