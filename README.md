# Автотесты на Python и Playwright

Учебный проект с проверками интерфейса,
ответов сервера и авторизации.

## Что проверяется

- Редактирование и сохранение данных в форме.
- Работа с вкладками, cookies и контекстами.
- Статусы ответов и данные JSON.
- Подмена ответов сервера.
- Вход через API и использование cookies в браузере.

## Установка на Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

## Запуск UI-тестов

```powershell
.\.venv\Scripts\python.exe -m pytest ui_tests
```

## Автоматический запуск

GitHub Actions запускает UI-тесты после отправки
изменений в ветку master.

Результаты доступны во вкладке Actions.