from abc import ABC, abstractmethod


class BaseDAO(ABC):
    """Абстрактный базовый Data Access Object."""

    @abstractmethod
    async def create(self, data: dict) -> dict:
        """Создать новый объект в базе данных."""

    @abstractmethod
    async def get(self, obj_id: int) -> dict:
        """Получить объект по его ID."""

    @abstractmethod
    async def get_list(self) -> list[dict]:
        """Получить список объектов с возможностью фильтрации."""

    @abstractmethod
    async def update(self, obj_id: int, obj_data: dict) -> dict:
        """Обновить объект по ID."""

    @abstractmethod
    async def delete(self, obj_id: int) -> None:
        """Удалить объект по ID."""
