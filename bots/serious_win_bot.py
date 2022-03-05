import telebot
from telebot import types
import subprocess

token = '5271986414:AAGyv59KpbcnBHu-SBHUWrh3tv1atUPqTjg'


def serioustestbot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Логин тест")
        item2 = types.KeyboardButton("Пока ничего :(")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, '\nПока могу сделать только - "Логин тест"', reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Логин тест':
            arg = [r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', "pytest -v -m admin",
                   'F:/serious/tests/Test_login.py']
            answer = subprocess.Popen(arg, stdout=subprocess.PIPE)
            date = answer.communicate()
            bot.send_message(message.chat.id, date)
        elif message.text.strip() == "Пока ничего :(":
            bot.send_sticker(message.chat.id,
                                    "CAACAgIAAxkBAAEEDRZiIh8ObfbsI_sBsTO6OSQ7B7gwfwACg08CAAFji0YMFnvL46C3JM8jBA")

    bot.polling()


if __name__ == '__main__':
    serioustestbot(token)
