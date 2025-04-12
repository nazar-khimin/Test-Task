import polars as pl
from polars import DataFrame


def normalize_breed_names(data: pl.LazyFrame) -> DataFrame:
    """
    Cleans and normalizes breed names using SQL-like operations.
    """
    query = """
        SELECT *, LOWER(TRIM(Breed)) AS normalized_breed
        FROM self
    """
    return data.sql(query).collect()


def extract_unique_breeds(data: pl.DataFrame) -> DataFrame:

    lazy_data = data.lazy()
    query = """
        SELECT DISTINCT normalized_breed
        FROM self
    """
    return lazy_data.sql(query).collect()

def licenses_by_breed(data: pl.LazyFrame) -> pl.DataFrame:
    """
    Counts licenses by LicenseType for each breed using SQL-like operations.
    """
    query = """
        SELECT LicenseType, LOWER(TRIM(Breed)) AS normalized_breed, COUNT(*) AS license_count
        FROM self
        GROUP BY LicenseType, normalized_breed
    """
    result = data.sql(query).collect()
    return result