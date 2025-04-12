import logging
from datetime import date

import pandas as pd
from faker import Faker
from faker.generator import random
from polars.dependencies import pandas


def create_data(locale: str) -> Faker:
    """
        Creates a Faker instance for generating localized fake data.
    """
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)


def generate_record(fake: Faker) -> list:
    """
        Generates a single fake employee record.
    """
    id = fake.uuid4()
    name = fake.name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=55)
    salary = random.randint(30000, 150000)
    department_id = random.randint(1, 10)

    return [id, name, date_of_birth, salary, department_id]


def write_to_csv(file_path: str, num_records: int) -> None:
    """
        Generates multiple fake user records and writes them to a CSV file.
    """
    fake = create_data("en_US")
    headers = ["id", "name", "date_of_birth", "salary", "department_id"]

    data = [generate_record(fake) for _ in range(num_records)]
    df = pd.DataFrame(data, columns=headers)

    df.to_csv(file_path, index=False)
    logging.info(f"Wrote {num_records} records to {file_path}")


if __name__ == '__main__':
    logging.info(f"Started data generation for {date.today()}.")

    write_to_csv("employees.csv", num_records=100)