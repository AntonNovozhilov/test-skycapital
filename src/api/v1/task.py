from http import HTTPStatus
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.base import get_async_session
from src.repositiories.tasks import TasksDAO
from src.schemas.tasks import TaskCreate, TaskInDB, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])
dao = TasksDAO()


@router.post("/", response_model=TaskInDB)
async def create_task(
    data: TaskCreate, session: AsyncSession = Depends(get_async_session),
):
    """Создать новую задачу"""
    task = await dao.create(data.model_dump(), session)
    return task


@router.get("/{task_id}", response_model=TaskInDB)
async def get_task(
    task_id: UUID, session: AsyncSession = Depends(get_async_session),
):
    """Получить задачу по ID"""
    task = await dao.get(task_id, session)
    if not task:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Задача не найдена",
        )
    return task


@router.get("/", response_model=List[TaskInDB])
async def get_tasks(session: AsyncSession = Depends(get_async_session)):
    """Получить список всех задач"""
    tasks = await dao.get_list(session)
    return tasks


@router.put("/{task_id}", response_model=TaskInDB)
async def update_task(
    task_id: UUID,
    data: TaskUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Обновить задачу по ID"""
    task = await dao.get(task_id, session)
    if not task:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Задача не найдена",
        )
    updated_task = await dao.update(task, data.model_dump(), session)
    return updated_task


@router.delete("/{task_id}", status_code=204)
async def delete_task(
    task_id: UUID, session: AsyncSession = Depends(get_async_session),
):
    """Удалить задачу по ID"""
    task = await dao.get(task_id, session)
    if not task:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Задача не найдена",
        )
    await dao.delete(task, session)
