from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from task2.models.base import Base
from task2.models.timestamp_mixin import TimestampMixin
from task2.repr_generator import generate_repr


@generate_repr()
class Departments(Base, TimestampMixin):
    __tablename__ = "departments"
    name: Mapped[str] = mapped_column(String(30))
    employee_id: Mapped[int] = mapped_column(String, ForeignKey('employees.id'))