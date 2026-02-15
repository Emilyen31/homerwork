from typing import Any
from datetime import datetime


def filter_by_state(list_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, у которых ключ state соответствует указанному значению."""

    # Создаём пустой список

    filter_dicts = []
    for filter_dict in list_dicts:

        # Проверяем в заданых словарях наличие значения 'EXECUTED' по ключу  'state'

        if filter_dict.get("state") == state:

            # Добавляем в список словари, в которых есть значение 'EXECUTED'

            filter_dicts.append(filter_dict)

    return filter_dicts


def sort_by_date(list_dicts: list[dict[str, Any]], sort_descending: bool = True) -> list[dict[str, Any]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    и возвращает новый список, отсортированный по дате."""

    # Преобразуем строки дат в объекты datetime для сортировки

    for date in list_dicts:
        date["date"] = datetime.strptime(date["date"], "%Y-%m-%dT%H:%M:%S.%f")

    # Сортируем список словарей по ключу 'date'

        sorted_data: list[dict[str, Any]] = sorted(list_dicts, key=lambda x: x["date"], reverse=sort_descending)

    # Преобразуем обратно в строковый формат
    for data in list_dicts:
        data["date"] = data["date"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    return sorted_data
