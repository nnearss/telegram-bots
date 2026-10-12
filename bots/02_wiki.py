"""Бот-всезнайка: присылает краткое описание слова из русской Википедии."""

import re

import telebot
import wikipedia

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("ru")


def get_summary(query: str) -> str:
    """Первые предложения статьи без разделов и скобок."""
    try:
        text = wikipedia.page(query).content[:1000]
    except Exception:
        return "❌ В энциклопедии нет информации об этом. Попробуйте другое слово."
    sentences = []
    for sentence in text.split(".")[:-1]:
        if "==" in sentence:
            break
        if len(sentence.strip()) > 3:
            sentences.append(sentence + ".")
    result = "".join(sentences)
    result = re.sub(r"\([^()]*\)", "", result)   # убираем скобки (дважды — для вложенных)
    result = re.sub(r"\([^()]*\)", "", result)
    result = re.sub(r"\{[^{}]*\}", "", result)
    return result.strip() or "❌ Не получилось сформулировать ответ."


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "📚 Привет! Напишите любое слово, и я расскажу, что это такое.")


@bot.message_handler(content_types=["text"])
def answer(message):
    bot.send_message(message.chat.id, "🔍 Ищу в Википедии...")
    bot.send_message(message.chat.id, get_summary(message.text))


if __name__ == "__main__":
    print("🚀 Бот-всезнайка запущен")
    bot.infinity_polling()
