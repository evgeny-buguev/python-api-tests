# Автотесты API, UI и базы данных

Портфолийный проект автоматизации на Python 3.12 и pytest. API-тесты проверяют ответы, ошибки и авторизацию. Playwright покрывает логин, cookies, обработку сетевых ответов, таблицы, загрузки файлов и вкладки. SQL-тесты выполняют CRUD и JOIN в SQLite.

| Где | Что находится |
| --- | --- |
| `test_api_post.py`, `test_api_users.py` | REST API, авторизация, проверки HTTP-ошибок и таймаута клиента |
| `api_client.py` | HTTP-клиент с `requests.Session`, базовым URL, таймаутом и Allure-шагами |
| `api_tests/` | Модели Pydantic и проверки контракта JSON Schema |
| `ui_tests/pages/`, `ui_tests/` | Page Objects, UI-сценарии и фикстуры браузера |
| `test_db.py` | Изолированные проверки SQLite |
| `.github/workflows/` | Запуск API, БД и UI в GitHub Actions |

## Запуск на Windows

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

`.env.example` содержит адреса и открытые тестовые учётные данные учебных сервисов. Для локальных настроек скопируй шаблон в `.env`. Переменные окружения имеют приоритет над обоими файлами. JSONPlaceholder имитирует запись, поэтому тесты POST, PATCH и DELETE проверяют контракт ответа.

```powershell
Copy-Item .env.example .env
python -m pytest test_api_post.py test_api_users.py test_db.py api_tests
python -m pytest ui_tests
```

В `test_28_login_full_flow.py` параметры задают ожидаемый редирект и текст для двух случаев входа. `LoginPage` отправляет форму и возвращает HTTP-ответ. Фикстура `authenticated_page` создаёт отдельный контекст для тестов cookies и logout и закрывает его после проверки.

Четыре файла сценариев авторизации можно запустить отдельно.

```powershell
python -m pytest ui_tests/test_21_login_from_fixture.py ui_tests/test_23_clear_cookies.py ui_tests/test_24_logout.py ui_tests/test_28_login_full_flow.py -v
```

## Отчёты и проверка кода

```powershell
ruff check .
ruff format --check .
python -m pytest ui_tests --alluredir=allure-results --clean-alluredir --tracing=retain-on-failure --screenshot=only-on-failure
allure generate allure-results --clean -o allure-report
allure open allure-report
```

Для последних двух команд нужен Allure CLI с Java. Для упавших браузерных тестов скриншоты и trace сохраняются в `test-results/` и прикладываются к Allure. Открыть trace можно командой `python -m playwright show-trace <путь-к-trace.zip>`.

GitHub Actions запускает API, SQLite и UI на pull request в `master` и после push в `master`. В разделе **Artifacts** соответствующего запуска доступны JUnit XML, HTML-отчёт, исходные результаты Allure и диагностические файлы Playwright.

## Docker

```powershell
docker build -t python-api-tests .
docker run --init --ipc=host --name qa-autotests python-api-tests
docker cp qa-autotests:/app/allure-results ./allure-results
docker cp qa-autotests:/app/report.xml ./report.xml
```

Для запуска со своей конфигурацией передай `--env-file .env` в `docker run`.
