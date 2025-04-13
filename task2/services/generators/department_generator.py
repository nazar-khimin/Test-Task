from typing import List

from faker import Faker

from task2.models import Departments

def generate_department_records(num_records: int) -> List[Departments]:
    """
    Generates a list of fake Department instances.
    """
    # Create a Faker instance
    fake = Faker("en_US")
    departments = []

    for i in range(1, num_records + 1):  # Ensure IDs are sequentially generated
        department_name = fake.company()  # Generate a fake company name
        department = Departments(
            id=i,
            name=department_name
        )
        departments.append(department)

    return departments