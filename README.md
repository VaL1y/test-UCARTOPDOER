# Incident Service

## Запуск
uvicorn app.main:app --reload

База создаётся автоматически в файле `incidents.db`.

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
