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

    # Создаём новый список для хранения данных

    temp_list = []
    for date in list_dicts:

        # Копируем словарь, чтобы не изменять исходный

        new_date = date.copy()

        # Преобразуем строки дат в объекты datetime для сортировки

        new_date["date"] = datetime.strptime(new_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
        temp_list.append(new_date)

    # Сортируем временный список по ключу 'date'

    sorted_data = sorted(temp_list, key=lambda x: x["date"], reverse=sort_descending)

    # Преобразуем обратно в строковый формат и формируем итоговый список

    result_list = []
    for data in sorted_data:
        # Копируем словарь, чтобы не изменять временный

        new_data = data.copy()
        new_data["date"] = new_data["date"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        result_list.append(new_data)
    return result_list
