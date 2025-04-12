from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from task2.models.base import Base
from task2.models.timestamp_mixin import TimestampMixin
from task2.repr_generator import generate_repr


@generate_repr()
class Employees(Base, TimestampMixin):
    __tablename__ = "employees"

    name: Mapped[str] = mapped_column(String(30))