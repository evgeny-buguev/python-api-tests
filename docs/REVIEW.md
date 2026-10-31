# Аудит QA-портфолио

Проверен исходный commit [cbee66e7](https://github.com/evgeny-buguev/python-api-tests/commit/cbee66e7db86de1078767563123e006ae89b5e40)
«Add latest UI exercises» от 29 октября 2026 года. Исходный сбор: 149 кейсов с параметризацией.

## Что требовало улучшения

| Наблюдение | Исправление |
| --- | --- |
| README почти не раскрывал API и SQL, не давал команд полного/выборочного запуска | README с картой наборов, командами Windows/Linux и диагностикой |
| API, unit и SQL смешаны в корне проекта | Отдельные tests/api, tests/unit, tests/db; общие validators и Page Object вынесены |
| Две строки `expect(...).to_be_disabled` не вызывали метод | Добавлен вызов; Ruff B018 предотвращает повторение |
| `INTENGER` воспринимался SQLite как произвольный тип | Исправлен INTEGER; добавлены duplicate ID и rollback |
| Новые browser contexts создавались напрямую и закрывались вручную | Использован new_context pytest-playwright с teardown и настройками trace/screenshot |
| Полный сбор после разделения мог конфликтовать из-за одинаковых имён модулей | Включён importlib mode |
| CI срабатывал только на push master | Добавлен pull_request и ручной запуск; внешние наборы выполняются отдельно |
| Трейсы были только ручной опцией; артефакты сохранялись не во всех workflows | JUnit в каждом job, failure traces/screenshots в UI, ручная запись всех traces сохранена |
| Зависимости не фиксировали версии | Зафиксированы прямые зависимости, включая версию Playwright и Ruff |
| Учебный assert сравнивал две константы; 500 проверялся дважды одинаковым способом | Убраны 2 избыточных кейса; добавлены 2 SQL-кейса; итоговый сбор остаётся 149 |

## Проверка изменений

- Полный сбор: **149 кейсов**, ошибок коллекции нет.
- Unit + SQLite: **38 passed** локально на Python 3.12; в CI — на Python 3.12 и 3.14.
- Ruff: **check и format --check прошли** для 59 Python-файлов.
- YAML workflows и относительные ссылки в документации проверены.
- Внешние API: **70 passed** локально и в CI.
- Chromium: **6 локальных UI + 35 внешних UI passed** в CI.
- JUnit-отчёты и UI-артефакты опубликованы в GitHub Actions.

Проверки кода commit [a6af11a](https://github.com/evgeny-buguev/python-api-tests/commit/a6af11a03cac3be9babce59ed0a328a0a84afeb3):

| CI-запуск | Набор | Результат |
| --- | --- | --- |
| [API and local tests](https://github.com/evgeny-buguev/python-api-tests/actions/runs/41232617946) | Unit + SQLite, Python 3.12 | 38 passed; Ruff check/format passed |
| Тот же запуск | Unit + SQLite, Python 3.14 | 38 passed; Ruff check/format passed |
| Тот же запуск | Внешние API | 70 passed |
| [UI tests](https://github.com/evgeny-buguev/python-api-tests/actions/runs/41232617823) | Chromium без внешних сервисов | 6 passed, 35 deselected |
| Тот же запуск | Chromium с внешними сервисами | 35 passed, 6 deselected |

Таким образом, все 149 кейсов прошли в отдельных CI jobs; локальный набор дополнительно проверен на двух версиях Python.
Каждый UI job вывел одно предупреждение PytestRemovedIn10Warning о фикстуре base_url; ошибок выполнения нет.
Локальная установка Chromium и Headless Shell не завершилась из-за повреждённых скачанных архивов, поэтому браузерный результат подтверждён CI.

Количество кейсов не является процентом покрытия продукта. Последние исходные CI-запуски до изменений:
[API](https://github.com/evgeny-buguev/python-api-tests/actions/runs/40825782957) и
[UI](https://github.com/evgeny-buguev/python-api-tests/actions/runs/40825782959) — success.
Эти результаты относятся к исходному commit, а не к изменениям портфолио.
