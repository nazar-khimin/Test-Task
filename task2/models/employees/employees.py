from datetime import date

from sqlalchemy import String, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from task2.models.base import Base
from task2.models.timestamp_mixin import TimestampMixin
from task2.repr_generator import generate_repr


@generate_repr()
class Employees(Base, TimestampMixin):
    __tablename__ = "employees"

    name: Mapped[str] = mapped_column(String(30))
    date_of_birth: Mapped[date] = mapped_column(Date)
    salary: Mapped[int] = mapped_column(Integer)
    department_id: Mapped[int] = mapped_column(String, ForeignKey('departments.id'))