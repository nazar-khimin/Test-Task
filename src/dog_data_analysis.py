import polars as pl
from polars import DataFrame


def normalize_breed_names(data: pl.LazyFrame) -> DataFrame:
    """
    Cleans and normalizes breed names using SQL-like operations.
    """
    query = """
            SELECT *, LOWER(REPLACE(Breed, ' ', '')) AS NormalizedBreed
            FROM self
        """
    return data.sql(query).collect()


def extract_unique_breeds(data: pl.DataFrame) -> DataFrame:

    lazy_data = data.lazy()
    query = """
        SELECT DISTINCT NormalizedBreed
        FROM self
    """
    return lazy_data.sql(query).collect()

def licenses_by_breed(data: pl.LazyFrame) -> pl.DataFrame:
    """
    Counts licenses by LicenseType for each breed using SQL-like operations.
    """
    query = """        
        SELECT d."Breed", d."LicenseType", COUNT(*) AS "LicenseCount"
        FROM self AS d
        GROUP BY d."Breed", d."LicenseType"
        ORDER BY "LicenseCount" DESC;
    """
    result = data.sql(query).collect()
    return result