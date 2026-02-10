def filter_by_state(list_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая возвращает список словарей с заданым статусом"""

    # Создаём пустой список

    filter_dicts = []
    for filter_dict in list_dicts:

        # Проверяем в заданых словарях наличие значения 'EXECUTED' по ключу  'state'

        if filter_dict.get("state") == state:

            # Добавляем в список словари, в которых есть значение 'EXECUTED'

            filter_dicts.append(filter_dict)

    return filter_dicts


def sort_by_date(list_dicts: list[dict]) -> list:
    """Функция, которая  возвращает новый список словарей, отсортированный по дате"""

    sort_dicts = sorted(list_dicts, key=lambda x: x["date"], reverse=True)

    return sort_dicts
