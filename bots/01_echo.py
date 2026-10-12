"""Эхо-бот: повторяет сообщения пользователя."""

import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "🤖 К работе готов! Напишите мне что-нибудь.")


@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.send_message(message.chat.id, "📌 Команды:\n/start — запуск бота\n/help — справка")


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, "🔁 Вы написали: " + message.text)


if __name__ == "__main__":
    print("🚀 Эхо-бот запущен")
    bot.infinity_polling()
