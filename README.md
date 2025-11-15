# Incident Service

## Запуск
uvicorn app.main:app --reload

База создаётся автоматически в файле `incidents.db`.

## Запуск с автотестами

```bash
docker compose up --build
```
Сервис api поднимается только если тесты (pytest) успешно прошли.
Приложение будет доступно на http://localhost:8000

## Эндпоинты

### 1. Создать инцидент
POST /incidents/
```json
{
  "description": "Самокат не отвечает",
  "source": "operator",
  "status": "new"
}
```
### 2. Получить список инцидентов (опционально фильтр)
GET /incidents/?status=resolved

### 3. Обновить статус по id
PATCH /incidents/1
```json
{ "status": "resolved" }
```


