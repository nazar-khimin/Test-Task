from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, declarative_mixin

@declarative_mixin
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())