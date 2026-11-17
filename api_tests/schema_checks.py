from jsonschema import Draft202012Validator


def get_error_locations(users_to_check, expected_list_schema):
    # Создаём объект, который проверяет данные по переданной схеме.
    schema_validator = Draft202012Validator(expected_list_schema)

    # Проверяем переданные данные и собираем найденные ошибки.
    found_errors = list(
        schema_validator.iter_errors(users_to_check)
    )

    # Сюда будем добавлять адреса ошибок.
    error_locations = []

    for validation_error in found_errors:
        # Получаем адрес одной ошибки.
        error_location = list(validation_error.path)

        # Добавляем этот адрес в общий список.
        error_locations.append(error_location)

    # Отдаём готовый список тому, кто вызвал функцию.
    return error_locations