import enum

from sqlalchemy import Column, String, Text

from src.core.base import Base


class TaskStatus(enum.StrEnum):
    """Статусы задач."""

    CREATED = "Создано"
    IN_PROGRESS = "В работе"
    DONE = "Заверешено"


class Task(Base):
    """Модель задачи."""

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, nullable=False, default=TaskStatus.CREATED)
