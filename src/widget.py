from masks import get_mask_card_number, get_mask_account


def mask_account_card(number_account_card: str) -> str:
    """Функция, которая принимает на вход номер карты или счёта и возвращает их маску."""

    # Разделяем введённую строку на две подстроки с разделителем по пробелу

    user_input = number_account_card.rsplit(" ", 1)

    # Проверяем количество символов подстроки, начиноая с конца 16 или 20, что означает карта или счёт соответственно

    if len(user_input[1]) == 16:
        return f"{user_input[0]} {get_mask_card_number(user_input[1])}"
    elif len(user_input[1]) == 20:
        return f"{user_input[0]} {get_mask_account(user_input[1])}"
    else:
        return "Некорректный ввод"
