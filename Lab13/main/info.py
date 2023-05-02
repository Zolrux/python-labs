import json
import flag
from telebot.types import InlineKeyboardButton


def data():
    with open('exchange.json', 'r', encoding="utf-8") as json_file:
        return json.load(json_file)


def available_currencies():
    data_list = data()
    s = ""
    for dicts in data_list:
        for key in dicts:
            if key == 'country':
                s += f"{format_country_flag(dicts['country'])}"
            elif key == "txt":
                s += f"{dicts[key]}: "
            elif key == "cc":
                s += f"{dicts[key]}\n"
    return s


def init_buttons():
    data_list = data()
    buttons = []
    for index, dicts in enumerate(data_list):
        flag_ua = '\U0001F1FA\U0001F1E6'
        arrow = '\u2192'
        flag_country = format_country_flag(dicts["country"])
        currency = dicts["cc"]
        button = InlineKeyboardButton(text=f"{flag_country}{currency} {arrow} {flag_ua}UAH", callback_data=f"{index}")
        buttons.append(button)
    return buttons


def exchange_calculate(current_index: int, value: float):
    data_list = data()
    for index, dicts in enumerate(data_list):
        if index == current_index:
            return value * dicts["rate"]


def message_require(index):
    data_list = data()
    for i in range(len(data_list)):
        if i == index:
            flag_ua = '\U0001F1FA\U0001F1E6'
            currency = data_list[i]['cc']
            flag_country = format_country_flag(data_list[i]['country'])
            return f"Enter value {flag_country}{currency} to convert {flag_ua}UAH"


def get_country_info(index_country):
    data_list = data()
    for index in range(len(data_list)):
        if index == index_country:
            country_flag = format_country_flag(data_list[index]['country'])
            return f"{ country_flag},{data_list[index]['cc']}"


def format_country_flag(country):
    if country == "RU":
        return '\U0001F4A9'
    elif country == "BY":
        return "\U0001F954"
    else:
        return flag.flag(country)