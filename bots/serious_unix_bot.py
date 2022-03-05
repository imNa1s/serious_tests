import telebot
from telebot import types
from bots.call_tsts_bot import CallableTsts

token = '5271986414:AAGyv59KpbcnBHu-SBHUWrh3tv1atUPqTjg'


def serioustestbot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Логин тест")
        item2 = types.KeyboardButton("Тест тикета от админа")
        item3 = types.KeyboardButton("Тест тикета от пользователя")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, '\nВыбери требуемый тест"', reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Логин тест':
            date = CallableTsts.bot_login()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест тикета от админа':
            date = CallableTsts.bot_admin_tiket()
            bot.send_message(message.chat.id, date)

        elif message.text.strip() == 'Тест тикета от пользователя':
            date = CallableTsts.bot_partner_tiket()
            bot.send_message(message.chat.id, date)

        else:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEDRZiIh8ObfbsI_sBsTO6OSQ7B7gwfwACg08CAAFji0YMFnvL46C3JM8jBA")

    bot.polling()


if __name__ == '__main__':
    serioustestbot(token)
