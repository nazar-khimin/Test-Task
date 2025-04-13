from typing import List

from task2.models import Departments

def generate_10_department_records() -> List[Departments]:
    """
    Creates Department ORM instances using a fixed list of 10 department names.
    """
    department_names = [
        "HR",
        "Engineering",
        "Marketing",
        "Sales",
        "Finance",
        "Operations",
        "Legal",
        "Customer Support",
        "Product Management",
        "IT"
    ]

    departments = [
        Departments(id=i + 1, name=name)
        for i, name in enumerate(department_names)
    ]
    return departments