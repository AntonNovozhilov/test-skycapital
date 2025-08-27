## API для управления задачами
Приложение на FastAPI, которое позволяет управлять задачами.

### Эндпоинты
| Метод |  URL | Описание |
| ----- |----| --------|
| GET |  /api/v1/tasks/| Получить список всех задач |
| POST |  /api/v1/tasks/ | Создать задачу |
| GET |  /api/v1/tasks/{UUID}/ | Получить задачу по UUID |
| PUT |  /api/v1/tasks/{UUID}/ | Изменить задачу по UUID |
| DELETE |  /api/v1/tasks/{UUID} | Удалить задачу по UUID |

### Стек
- FastAPI
- SQLAlchemy
- Postgres
- Docker & Docker Compose
- Alembic
- Pydantic
- Poetry
- Pytest

### Установка и запуск
Клонируйте репозиторий:

```
git clone git@github.com:AntonNovozhilov/test-skycapital.git
cd test_kri
```

Создайте файл .env в корне проекта:

```
cd src
touch .env
```

Заполните .env следующими переменными:

```
TITLE=Название
POSTGRES_PORT=5432
POSTGRES_SERVER=db
POSTGRES_DB=test_db             # Название базы данных
POSTGRES_USER=postgres        # Логин от PostgreSQL
POSTGRES_PASSWORD=postgres    # Пароль от PostgreSQL
```

Запустите приложение через Docker:

```
docker compose up --build
```

После запуска документация будет доступна по адресу:
http://127.0.0.1:8000/docs