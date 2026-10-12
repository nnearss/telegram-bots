"""Бот с двумя кнопками: случайная новость или афоризм из файлов data/."""

import random

import telebot
from telebot import types

from config import TOKEN, read_lines

bot = telebot.TeleBot(TOKEN)
FACTS = read_lines("facts.txt")
QUOTES = read_lines("quotes.txt")
NEWS, QUOTE = "📰 Новость", "💡 Афоризм"


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(NEWS))
    markup.add(types.KeyboardButton(QUOTE))
    bot.send_message(message.chat.id, "👇 Выберите, что хотите узнать:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle(message):
    text = message.text.strip()
    if text == NEWS:
        bot.send_message(message.chat.id, "📰 " + random.choice(FACTS))
    elif text == QUOTE:
        bot.send_message(message.chat.id, "💡 " + random.choice(QUOTES))
    else:
        bot.send_message(message.chat.id, "❓ Нажмите одну из кнопок или введите /start")


if __name__ == "__main__":
    print("🚀 Бот с кнопками запущен")
    bot.infinity_polling()
