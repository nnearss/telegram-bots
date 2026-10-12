"""Чат-бот по базе вопросов и ответов: находит самый похожий вопрос нечётким поиском."""

import telebot
from rapidfuzz import fuzz

from config import DATA, TOKEN

bot = telebot.TeleBot(TOKEN)
THRESHOLD = 50   # минимальная похожесть вопроса, из 100


def load_faq(path=DATA / "faq.txt") -> list[tuple[str, str]]:
    """Файл из пар строк: «u: вопрос», затем ответ."""
    lines = [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [(q[3:].lower(), a) for q, a in zip(lines, lines[1:]) if q.startswith("u: ")]


FAQ = load_faq()


def answer(text: str) -> str:
    text = text.lower().strip()
    score, reply = max((fuzz.token_sort_ratio(q, text), a) for q, a in FAQ)
    return reply if score > THRESHOLD else "🤷 Я не совсем понял вопрос. Попробуйте переформулировать!"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "👋 Давай поболтаем! Например, напиши «Привет».")


@bot.message_handler(content_types=["text"])
def handle(message):
    bot.send_message(message.chat.id, answer(message.text))


if __name__ == "__main__":
    print(f"🚀 Чат-бот запущен, в базе {len(FAQ)} вопросов")
    bot.infinity_polling()
