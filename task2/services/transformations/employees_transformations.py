import pandas as pd

from task2.services.transformations.base_transformations import trim_string_values, convert_data_types


def transform_csv_data(df: pd.DataFrame, schema: dict[str, str]) -> pd.DataFrame:
    """
    First trim string columns, then convert data types based on the provided schema.
    """
    df = trim_string_values(df, schema)
    df = convert_data_types(df, schema)
    return df