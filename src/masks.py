def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""

    mask_card = str(card_number)
    first_six = mask_card[:6]
    last_four = mask_card[-4:]
    return f"{first_six[0:4]} {first_six[4:6]}** **** {last_four}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""

    mask_account = str(account_number)
    return f"**{mask_account[-4:]}"
