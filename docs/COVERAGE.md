# Карта покрытия

Сбор через `python -m pytest --collect-only -q`: **149 тест-кейсов с учётом параметризации**.
Числа ниже описывают состав набора, а не процент покрытия исходного кода или приложения.

| Набор | Кейсы | Внешний сервис | Что проверяется |
| --- | ---: | --- | --- |
| Unit | 31 | Нет | Валидаторы, граничные координаты, неверные типы/форматы, API-клиент с monkeypatch, tmp_path/yield |
| SQLite | 7 | Нет | INSERT/SELECT, UPDATE/DELETE выбранной строки, JOIN/LEFT JOIN/GROUP BY, orphan order, duplicate ID, rollback |
| API | 70 | Да | JSONPlaceholder и DummyJSON: статусы, JSON, связи данных, фильтры, Bearer-авторизация |
| UI | 41 | 35 — да; 6 — нет | Форма, авторизация, HTTP-ответы в браузере, route.fulfill, cookies, вкладки и контексты |
| **Всего** | **149** | **105 внешних / 44 локальных** | Взаимоисключающие категории unit/db/api/ui |

Без браузера выполняются 38 кейсов unit + db. Локальным UI нужен установленный Chromium.
Smoke — дополнительная метка: 5 кейсов уже включены в таблицу.

## Сценарии и код

| Область | Проверки | Где смотреть |
| --- | --- | --- |
| Посты и комментарии | POST 201 и возвращённые данные; GET известных/неизвестных ID; PATCH/DELETE; фильтр по userId; пустые выборки; принадлежность и уникальность комментариев | [test_posts.py](../tests/api/test_posts.py) |
| Пользователи | ID 1–10; отсутствующие ID 0/11/999; список; name/email/address/company; координаты и Content-Type | [test_users.py](../tests/api/test_users.py) |
| Bearer-авторизация | Действующий токен, отсутствие токена, невалидный токен, неверный пароль без выдачи accessToken | [test_auth.py](../tests/api/test_auth.py) |
| Границы данных | Широта -90/90, долгота -180/180 и выход за границы; нечисловые значения; email без @, пустое значение и неверный тип; пустой заголовок | [test_validators.py](../tests/unit/test_validators.py) |
| Ошибки API-клиента | Подменённый 200, HTTPError для 401/404/500, Timeout; URL и timeout успешного запроса | [test_api_client.py](../tests/unit/test_api_client.py) |
| Целостность SQL | Изменяется/удаляется только выбранный пользователь; заказ связан с владельцем; покупатель без заказов; заказ без пользователя; duplicate ID и rollback | [test_users.py](../tests/db/test_users.py), [test_constraints.py](../tests/db/test_constraints.py) |
| Форма | Начальное значение Pizza, Edit, сохранение Soup/Pasta/Salad, disabled после Save, повторное редактирование, добавление второй строки без изменения первой | [ui_tests](../ui_tests/), [FoodPage](../pages/food_page.py) |
| Сеть в браузере | HTTP status/text/JSON; подмена навигационного ответа на 200/404/500 | [test_11_response_status.py](../ui_tests/test_11_response_status.py) – [test_18_mock_not_found.py](../ui_tests/test_18_mock_not_found.py) |
| Сессии | API-login → cookies → secure; перенос storage state; отсутствие входа; очистка cookies; logout и повторный запрет доступа | [test_19_api_login.py](../ui_tests/test_19_api_login.py) – [test_24_logout.py](../ui_tests/test_24_logout.py) |
| Форма авторизации | POST /authenticate, точные form fields, redirect 302, итоговая страница и сообщение для верного/неверного пароля | [test_25_login_response.py](../ui_tests/test_25_login_response.py) – [test_28_login_full_flow.py](../ui_tests/test_28_login_full_flow.py) |
| Изоляция | Разные вкладки одного контекста разделяют cookies; независимые контексты имеют разные cookies; новая страница начинает с исходного значения | [test_tabs_share_cookies.py](../ui_tests/test_tabs_share_cookies.py), [test_two_contexts.py](../ui_tests/test_two_contexts.py), [test_isolation.py](../ui_tests/test_isolation.py) |

## Тестовые объекты

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — пользователи, посты, комментарии; изменения имитируются.
- [DummyJSON](https://dummyjson.com/docs/auth) — вход и Bearer token.
- [Practice Test Automation](https://practicetestautomation.com/practice-test-exceptions/) — форма с редактированием и добавлением строки.
- [ExpandTesting](https://practice.expandtesting.com/login) — login/secure/logout.
- Локальные UI-кейсы используют `page.set_content`, cookies или перехват запроса через `route.fulfill`.

## Ограничения и следующие шаги

- POM применяется к форме; авторизация пока показана отдельными сценариями.
- Подмена 404/500 проверяет навигационный HTTP/JSON-ответ, а не обработку ошибки полноценным frontend-приложением.
- Валидатор email проверяет тип, непустое значение и символ @; это не полная валидация адреса.
- SQL-тесты запускаются на SQLite in-memory; это не проверка PostgreSQL или реальной БД продукта.
- Для настоящего CRUD end-to-end нужен управляемый API со сохраняемой записью и удалением тестовых данных.
- Следующее расширение: формальная JSON Schema, локальный стенд авторизации, отдельные сценарии Firefox/WebKit и mobile viewport.
