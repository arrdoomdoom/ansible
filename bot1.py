import telebot
import math
bot = telebot.TeleBot('5535006541:AAHRNNwTt1z__BkwL5D6f3c9fv11yxUF1To')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Возводит число в квадрат, введите число')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        bot.send_message(message.chat.id, float(message.text)^2)
    except:
        bot.send_message(message.chat.id, 'Введите число')

bot.polling(none_stop=True, interval=0)