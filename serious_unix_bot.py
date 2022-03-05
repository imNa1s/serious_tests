import telebot
from telebot import types
from seriousbot.call_tsts_bot import CallUnixTest

token = '5271986414:AAGyv59KpbcnBHu-SBHUWrh3tv1atUPqTjg'


def serioustestbot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text="Логин тесты", callback_data="Логин тесты")
        item2 = types.InlineKeyboardButton(text="Тесты тикетов", callback_data="Тесты тикетов")
        item3 = types.InlineKeyboardButton(text="Тесты категории", callback_data="Тесты тикетов")
        item4 = types.InlineKeyboardButton(text="Тесты страны", callback_data="Тесты тикетов")
        item5 = types.InlineKeyboardButton(text="Тесты источников", callback_data="Тесты тикетов")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, '\nВыбери категорию', reply_markup=markup)

    @bot.callback_query_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Логин тесты':
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton(text="Логин в админку", callback_data="Логин в админку")
            item2 = types.InlineKeyboardButton(text="Неудачный логин в админку", callback_data="нлва")
            item3 = types.InlineKeyboardButton("Логин партнёра test через админку")
            item4 = types.InlineKeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)
        # Тесты логина
        elif message.text.strip() == 'Логин в админку':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallUnixTest.bot_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'нлва':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallUnixTest.bot_fail_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Логин партнёра test через админку':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallUnixTest.bot_partner_login()
            bot.send_message(message.chat.id, date)
        # Тесты тикетов
        elif message.text.strip() == 'Тесты тикетов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест тикета от админа")
            item2 = types.KeyboardButton("Тест тикета от пользователя")
            item3 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест тикета от админа':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_admin_tiket()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест тикета от пользователя':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_partner_tiket()
            bot.send_message(message.chat.id, date)
        # Тесты категории
        elif message.text.strip() == 'Тесты категории':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест создания категории")
            item2 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест создания категории':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_category()
            bot.send_message(message.chat.id, date)
        # Тесты страны
        elif message.text.strip() == 'Тесты страны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест создания страны")
            item2 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест создания страны':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_country()
            bot.send_message(message.chat.id, date)
        # Тесты источника
        elif message.text.strip() == 'Тесты источников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест создания источника")
            item2 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест создания источника':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_create_source()
            bot.send_message(message.chat.id, date)


        else:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEDRZiIh8ObfbsI_sBsTO6OSQ7B7gwfwACg08CAAFji0YMFnvL46C3JM8jBA")

    bot.polling()


if __name__ == '__main__':
    serioustestbot(token)
