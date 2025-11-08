# Incident API Service

API-сервис для учёта и управления инцидентами.

## 🚀 Установка и запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/dmitriysemenov83/incident_api_test_task.git
cd incident_api_test_task
```

### 2. Установите зависимости
```bash
pip install -r requirements.txt
```
### 3. Создайте файл .env и настройте переменные окружения
переименуйте .env_example заполните его своими данными
```ini
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=incident_db
DB_USER=your_db_user
DB_PASSWORD=yor_password
DB_HOST=localhost
DB_PORT=5432
```
### 4. Настройте PostgreSQL базу данных
Создайте базу данных incident_db (или с другим именем, указанным в .env).

### 5. Выполните миграции
```bash
python manage.py migrate
```
### 6. Запустите сервер разработки
```bash
python manage.py runserver
```
Сервер будет доступен по адресу:
👉 http://127.0.0.1:8000

## 📘 Эндпоинты

### 1. Создать инцидент
URL: POST /api/v1/incidents/
Тело запроса:
```json
{
    "description": "Самокат не в сети",
    "source": "operator"
}
```
Доступные источники: operator, monitoring, partner

## 2. Получить список инцидентов

URL: GET /api/v1/incidents/
Фильтрация по статусу:
```swift
GET /api/v1/incidents/?status=open
```
Доступные статусы:
open, in_progress, resolved, closed

## 3. Обновить статус инцидента

URL: PATCH /api/v1/incidents/{id}/status/
Тело запроса:
```json
{
    "status": "in_progress"
}
```
Ошибки:
404 — инцидент не найден
