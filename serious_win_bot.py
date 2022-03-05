import telebot
from telebot import types
from seriousbot.call_tsts_bot import CallWinTests

token = '5271986414:AAGyv59KpbcnBHu-SBHUWrh3tv1atUPqTjg'


def serioustestbot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Логин тесты")
        item2 = types.KeyboardButton("Тесты тикетов")
        item3 = types.KeyboardButton("Тесты категории")
        item4 = types.KeyboardButton("Тесты страны")
        item5 = types.KeyboardButton("Тесты источников")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, '\nВыбери категорию', reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Логин тесты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Логин в админку")
            item2 = types.KeyboardButton("Неудачный логимн в админку")
            item3 = types.KeyboardButton("Логин партнёра test через админку")
            item4 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)
        # Тесты логина
        elif message.text.strip() == 'Логин в админку':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallWinTests.bot_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Неудачный логимн в админку':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallWinTests.bot_fail_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Логин партнёра test через админку':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date, answer = CallWinTests.bot_partner_login()
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
            date = CallWinTests.bot_admin_tiket()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест тикета от пользователя':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallWinTests.bot_partner_tiket()
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
            date = CallWinTests.bot_category()
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
            date = CallWinTests.bot_country()
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
            date = CallWinTests.bot_create_source()
            bot.send_message(message.chat.id, date)

        else:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEDRZiIh8ObfbsI_sBsTO6OSQ7B7gwfwACg08CAAFji0YMFnvL46C3JM8jBA")

    bot.polling()


if __name__ == '__main__':
    serioustestbot(token)
