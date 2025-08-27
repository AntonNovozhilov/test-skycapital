from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from src.models.tasks import TaskStatus


class TaskBase(BaseModel):
    """Базовая схема для задачи."""

    title: str = Field(..., max_length=255, description="Название задачи")
    description: Optional[str] = Field(None, description="Описание задачи")
    status: TaskStatus = Field(
        default=TaskStatus.CREATED, description="Статус задачи",
    )


class TaskCreate(TaskBase):
    """Схема для создания задачи."""


class TaskUpdate(BaseModel):
    """Схема для обновления задачи."""

    title: Optional[str] = Field(
        None, max_length=255, description="Название задачи",
    )
    description: Optional[str] = Field(None, description="Описание задачи")
    status: Optional[TaskStatus] = Field(None, description="Статус задачи")


class TaskInDB(TaskBase):
    """Схема, отражающая объект в БД."""

    id: UUID

    class Config:
        from_attributes = True


class TaskList(BaseModel):
    """Схема для списка задач."""

    tasks: List[TaskInDB]
