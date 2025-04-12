# ----------------------------
# Function to trim spaces from all string columns
# ----------------------------
import pandas as pd

from task2.utls.function_duration import timeit


@timeit
def trim_all_values(df: pd.DataFrame, schema: dict[str, str]) -> pd.DataFrame:
    """
    Trims leading and trailing spaces for every column in the schema, regardless of the target type.
    """
    for column in schema.keys():
        if column in df.columns:
            # Convert all values to strings and trim spaces
            df[column] = df[column].astype(str).str.strip()
    return df


@timeit
def convert_data_types(df: pd.DataFrame, schema: dict[str, str]) -> pd.DataFrame:
    """
    Converts the DataFrame columns to the desired types based on the schema:
    """
    for column, target_type in schema.items():
        if column not in df.columns:
            print(f"Column '{column}' is not in the DataFrame; skipping conversion.")
            continue

        if target_type == "date":
            df[column] = pd.to_datetime(df[column], errors="coerce")
        elif target_type == "int":
            df[column] = pd.to_numeric(df[column], errors="coerce").astype("Int64")
    return df
