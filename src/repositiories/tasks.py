from typing import List, Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.tasks import Task
from src.repositiories.base import BaseDAO
from src.schemas.tasks import TaskInDB


class TasksDAO(BaseDAO):
    """DAO для управления задачами."""

    async def create(self, data: dict, session: AsyncSession) -> TaskInDB:
        """Создать новую задачу."""
        task = Task(**data)
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    async def get(
        self, obj_id: UUID, session: AsyncSession,
    ) -> Optional[TaskInDB]:
        """Получить задачу по ID."""
        result = await session.execute(select(Task).where(Task.id == obj_id))
        task = result.scalar_one_or_none()
        return task

    async def get_list(self, session: AsyncSession) -> List[TaskInDB]:
        """Получить список всех задач."""
        result = await session.execute(select(Task))
        return result.scalars().all()

    async def update(
        self, obj: Task, obj_data: dict, session: AsyncSession,
    ) -> Optional[TaskInDB]:
        """Обновить задачу по ID."""
        for key, value in obj_data.items():
            setattr(obj, key, value)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, obj: Task, session: AsyncSession) -> None:
        """Удалить задачу по ID."""
        await session.delete(obj)
        await session.commit()
