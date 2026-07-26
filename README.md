# FastAPI — тестовый бэкенд

Простой бэкенд на FastAPI, возвращающий текущее время и дату сервера.

## Запуск

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Эндпоинты

| Метод   | Путь         | Описание              |
|---------|-------------|-----------------------|
| GET     | `/`         | Приветственное сообщение |
| GET     | `/time`     | Текущее время сервера  |
| GET     | `/date`     | Текущая дата сервера   |

## API документация

После запуска доступна интерактивная документация:
- Swagger UI — `http://127.0.0.1:8000/docs`
- ReDoc — `http://127.0.0.1:8000/redoc`

## Docker

```bash
docker build -t my-fastapi .
docker run -p 8000:8000 my-fastapi
```
