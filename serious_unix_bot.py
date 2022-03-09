import telebot
from telebot import types
from seriousbot.call_tsts_bot import CallUnixTest

token = '5234613832:AAHRtLcEMhmND0MZufYu07sbL0VD1Kvh7cQ'


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
        item6 = types.KeyboardButton("Тесты потоков")
        item7 = types.KeyboardButton("Тесты операторов")
        item8 = types.KeyboardButton("Тесты статистики")
        markup.add(item1, item2, item3)
        markup.add(item4, item5, item6)
        markup.add(item7, item8)
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
            date, answer = CallUnixTest.bot_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Неудачный логимн в админку':
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
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃 \nя займу около 30 секунд")
            date = CallUnixTest.bot_admin_tiket()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест тикета от пользователя':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу около 30 секунд")
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
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу около 10 секунд")
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
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу около 10 секунд")
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
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу около 15 секунд")
            date = CallUnixTest.bot_create_source()
            bot.send_message(message.chat.id, date)
        # Тесты потоков
        elif message.text.strip() == 'Тесты потоков':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест создания потока")
            item2 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест создания потока':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_create_stream()
            bot.send_message(message.chat.id, date)
        # Тесты операторов
        elif message.text.strip() == 'Тесты операторов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Тест создания оператора")
            item2 = types.KeyboardButton("/start")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест создания оператора':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу около 10 секунд")
            date = CallUnixTest.bot_create_operator()
            bot.send_message(message.chat.id, date)
        # Тесты статистики
        elif message.text.strip() == 'Тесты статистики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/start")
            item2 = types.KeyboardButton("Тест изменения даты")
            item3 = types.KeyboardButton("Тест статы переходов")
            item4 = types.KeyboardButton("Тест статы уников")
            item5 = types.KeyboardButton("Тест статы трафбека")
            item6 = types.KeyboardButton("Тест статы сабок")
            item7 = types.KeyboardButton("Тест статы конверсии")
            item8 = types.KeyboardButton("Тест статы ансабок")
            item9 = types.KeyboardButton("Тест статы ребилла")
            markup.add(item2, item3, item4)
            markup.add(item5, item6, item7)
            markup.add(item8, item9)
            markup.add(item1)
            bot.send_message(message.chat.id, '\nВыбери требуемый тест', reply_markup=markup)

        elif message.text.strip() == 'Тест изменения даты':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃")
            date = CallUnixTest.bot_stat_date()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы переходов':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃 \nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_transition()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы уников':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_unic()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы трафбека':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_traffback()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы сабок':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_subscribe()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы конверсии':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_conversion()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы ансабок':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_unsub()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест статы ребилла':
            bot.send_message(message.chat.id, "Нашёл, запускаю! 🏃\nя займу примерно 1 минуту времени.")
            date = CallUnixTest.bot_stat_rebill()
            bot.send_message(message.chat.id, date)

        else:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEDRZiIh8ObfbsI_sBsTO6OSQ7B7gwfwACg08CAAFji0YMFnvL46C3JM8jBA")

    bot.polling()


if __name__ == '__main__':
    serioustestbot(token)
