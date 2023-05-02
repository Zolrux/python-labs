import telebot
from telebot import types
from info import init_buttons
from config import API_TOKEN

# Initialize bot
bot = telebot.TeleBot(API_TOKEN)

# User dict data
user_dict = {}

keyboard = types.InlineKeyboardMarkup(row_width=1)
keyboard.add(*init_buttons())


@bot.message_handler(commands=['start'])
def send_keyboard(message):
    bot.send_message(message.chat.id, text="Choose button to exchange currency to UAH", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def button_pressed_callback(query):
    from info import message_require
    button_id = int(query.data)
    user_dict['button_id'] = button_id
    user_dict['chat_id'] = query.message.chat.id
    user_dict['attempts'] = 0
    msg = bot.send_message(chat_id=user_dict['chat_id'], text=message_require(button_id))
    bot.register_next_step_handler(msg, show_result)


def show_result(message):
    try:
        from info import exchange_calculate, get_country_info
        value = message.text
        if ',' in value:
            value = float(value.replace(',', '.'))
        else:
            value = float(value)
        calc = '{:.2f}'.format(exchange_calculate(user_dict['button_id'], value))
        country_flag, country_name = get_country_info(user_dict['button_id']).split(',')
        msg = f"{country_flag} {value} {country_name} = \U0001F1FA\U0001F1E6 {calc} UAH"
        bot.send_message(user_dict['chat_id'], text=msg)
    except Exception:
        user_dict['attempts'] += 1
        if user_dict['attempts'] <= 3:
            bot.reply_to(message, '\u203C Please enter only decimal number or natural number \u203C')
            bot.register_next_step_handler(message, show_result)
        else:
            bot.send_message(user_dict['chat_id'], '\u26A0 Input limit exceeded! \u26A0')
            return False


@bot.message_handler(commands=['active'])
def send_list(message):
    from info import available_currencies
    bot.send_message(message.chat.id, text=available_currencies())


if __name__ == '__main__':
    bot.infinity_polling()