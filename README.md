# QA Automation · Python / pytest / Playwright

Учебное QA-портфолио Евгения Бугуева: API, браузерные сценарии, авторизация и SQL.
В проекте **149 собираемых тест-кейсов с учётом параметризации**: 70 API, 41 UI, 31 unit и 7 SQLite.
Подробные сценарии и границы покрытия — в [карте покрытия](docs/COVERAGE.md).

## Что демонстрирует проект

- **API:** GET, POST, PATCH, DELETE; HTTP-статусы, Content-Type, поля и типы JSON, вложенные данные, фильтры, связи пользователей, постов и комментариев.
- **Авторизация:** Bearer token, неверный пароль, отсутствующий и невалидный токен; вход через API с передачей cookies в браузер, storage state, logout и повторный доступ.
- **UI:** локаторы по роли и label, повторяемые проверки через `expect`, параметризация ввода, редактирование и сохранение формы. Page Object `FoodPage` отделён от тестов.
- **Изоляция и ошибки:** вкладки в одном контексте, независимые контексты, очистка cookies; `route.fulfill` для ответов 200/404/500; `monkeypatch` для HTTPError и Timeout API-клиента.
- **SQL и инфраструктура тестов:** SQLite in-memory, JOIN/LEFT JOIN, GROUP BY, точечные UPDATE/DELETE, ограничения уникальности и rollback; фикстуры `session/function`, `yield`, `tmp_path`.
- **CI и диагностика:** GitHub Actions, проверка стиля Ruff, JUnit XML, screenshots и Playwright traces.

## Структура

| Путь | Назначение |
| --- | --- |
| `tests/api/` | Внешние демо-API: посты, пользователи, Bearer-авторизация |
| `tests/unit/` | Валидаторы, подмена ответов API-клиента, временный файл и teardown |
| `tests/db/` | SQLite с отдельной базой на каждый тест |
| `ui_tests/` | Браузерные сценарии и UI-фикстуры; номера файлов сохраняют порядок упражнений |
| `pages/food_page.py` | Page Object формы |
| `api_client.py`, `helpers/validators.py` | Минимальный API-клиент и общие проверки данных |
| `examples/` | Дополнительный пример; не входит в обычный сбор тестов |
| `.github/workflows/` | Локальные проверки, внешние API, UI и ручная запись traces |
| `docs/` | Карта покрытия, разбор изменений и текст для резюме/откликов |

## Установка на Windows · PowerShell

Нужны Git и Python 3.12+; CI проверяет локальный набор на Python 3.12 и 3.14.
Репозиторий приватный: для клонирования нужен выданный доступ к GitHub.

```powershell
git clone https://github.com/evgeny-buguev/python-api-tests.git
cd python-api-tests
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

Активация окружения не требуется. Если нужны только unit и SQL, установку Chromium можно пропустить.

## Команды запуска · Windows

Все команды выполняются из корня проекта.

```powershell
# Быстрая проверка без браузера и внешних сайтов: 38 тест-кейсов
.\.venv\Scripts\python.exe -m pytest tests/unit tests/db -q

# Все проверки без зависимости от внешних сайтов: 44, включая 6 UI; нужен Chromium
.\.venv\Scripts\python.exe -m pytest -m "not external" -q

# API: 70 тест-кейсов, нужен интернет
.\.venv\Scripts\python.exe -m pytest tests/api -v

# UI: 41 тест-кейс, нужен Chromium; 35 зависят от внешних сайтов
.\.venv\Scripts\python.exe -m pytest ui_tests -v --browser chromium

# Smoke: 5 тест-кейсов, нужен интернет и Chromium
.\.venv\Scripts\python.exe -m pytest -m smoke -v

# Полный прогон
.\.venv\Scripts\python.exe -m pytest -v

# Только сбор: список кейсов без выполнения
.\.venv\Scripts\python.exe -m pytest --collect-only -q
```

Для визуальной отладки добавьте `--headed --slowmo 300`.
Для одного кейса укажите его node ID, например:

```powershell
.\.venv\Scripts\python.exe -m pytest "ui_tests/test_04_values.py::test_save_food_values[chromium-Soup]" -v
```

## Linux / macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python -m pytest tests/unit tests/db -q
.venv/bin/python -m pytest -m "not external" -q
.venv/bin/python -m pytest -v
```

На Linux при нехватке системных библиотек используйте
`.venv/bin/python -m playwright install --with-deps chromium`.
Остальные параметры совпадают с Windows; меняется только путь к Python.

## Отчёты и отладка

JUnit XML по умолчанию: `test-results/junit.xml`. Отдельный путь задаётся через `--junitxml`.
Для сохранения причин падения:

```powershell
.\.venv\Scripts\python.exe -m pytest ui_tests -v --tracing retain-on-failure --screenshot only-on-failure --output test-results/browser
```

Чтобы записать trace даже у прошедшего теста, используйте `--tracing on`.
Для открытия скачанного или локального trace укажите фактический путь к ZIP:

```powershell
.\.venv\Scripts\python.exe -m playwright show-trace "test-results\browser\<папка-теста>\trace.zip"
```

Артефакты, окружения и файлы состояния авторизации исключены из Git.
В тестах используются публичные учебные учётные записи демо-сервисов; cookies хранятся в памяти.

## GitHub Actions

На push в `master`, pull request в `master` и при ручном запуске:

| Workflow | Проверки и результат |
| --- | --- |
| `API and local tests` | Ruff + 38 локальных тестов на Python 3.12/3.14; отдельный job на 70 внешних API-кейсов |
| `UI tests` | Chromium: отдельные jobs на 6 локальных и 35 внешних кейсов; trace/screenshot при падении |
| `UI traces` | Только ручной запуск: запись всех UI-тестов через `--tracing on` |

Отчёты находятся во вкладке [Actions](https://github.com/evgeny-buguev/python-api-tests/actions) → запуск → Artifacts.
Срок хранения — 7 дней. Внешние проверки не маскируются через `skip` или `continue-on-error`.

## Проверка стиля

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
```

Правила Ruff включают B018: выражение вроде `expect(field).to_be_disabled` без вызова метода будет ошибкой.

## Границы и развитие

Это учебный проект на демо-сервисах. JSONPlaceholder имитирует запись: POST/PATCH/DELETE
проверяют ответ, но не подтверждают сохранение изменений в базе сервиса.
Проверки JSON написаны через assertions; полноценная JSON Schema ещё не подключена.
Базовый прогон браузера — Chromium; Firefox/WebKit, мобильная адаптация, нагрузка и безопасность требуют отдельных наборов.
149 кейсов не означают процент покрытия продукта или 149 уникальных пользовательских сценариев.

При сетевой ошибке проверьте адрес сервиса и отчёт, затем запустите тот же упавший кейс отдельно.
Набор `tests/unit tests/db` помогает отдельно проверить локальную часть проекта.

[Карта покрытия](docs/COVERAGE.md) · [Аудит и проверка изменений](docs/REVIEW.md) · [Резюме и отклики](docs/PORTFOLIO.md)

Документация: [pytest markers](https://docs.pytest.org/en/stable/how-to/mark.html),
[Playwright fixtures и CLI](https://playwright.dev/python/docs/test-runners),
[JSONPlaceholder](https://jsonplaceholder.typicode.com/guide/).
