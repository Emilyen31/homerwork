from masks import get_mask_card_number, get_mask_account


def mask_account_card(number_account_card: str) -> str:
    """Функция, которая принимает на вход номер карты или счёта и возвращает их маску."""

    user_input = number_account_card.rsplit(" ", 1)

    if len(user_input[1]) == 16:
        return f"{user_input[0]} {get_mask_card_number(user_input[1])}"
    elif len(user_input[1]) == 20:
        return f"{user_input[0]} {get_mask_account(user_input[1])}"
    else:
        return "Некорректный ввод"


def get_date(iso_date_str):
    """Функция преобразует дату в формат 'ДД.ММ.ГГГГ'"""

    # Делим строку с датой '2024-03-11T02:26:18.671407' на две подстроки по символу 'T'

    date_y_m_d = str(iso_date_str.split("T", 1)[0])

    # Делим строку с датой '2024-03-11' на три подстроки по символу '-'

    date_d_m_y = date_y_m_d.split("-", 3)

    # Выводим получившиеся подстроки, начиная с последней, с разделителем "."
    return f"{date_d_m_y[2]}.{date_d_m_y[1]}.{date_d_m_y[0]}"


if __name__ == "__main__":
    test1 = "Visa Platinum 8990922113665229"
    test2 = "Счет 64686473678894779589"
    test12 = "2024-03-11T02:26:18.671407"
    print(mask_account_card(test1))
    print(mask_account_card(test2))
    print(get_date(test12))
