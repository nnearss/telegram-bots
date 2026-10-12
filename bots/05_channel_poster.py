"""Бот для канала: публикует посты из data/jokes.txt по таймеру.

Бота нужно добавить в канал администратором с правом публикации,
а имя канала указать в .env: CHANNEL=@имя_канала
"""

import os
import time

import telebot

from config import TOKEN, read_lines

CHANNEL = os.getenv("CHANNEL")
INTERVAL_SEC = int(os.getenv("POST_INTERVAL_SEC", "30"))

if __name__ == "__main__":
    if not CHANNEL:
        raise SystemExit("Укажите канал в .env: CHANNEL=@имя_канала")
    bot = telebot.TeleBot(TOKEN)
    posts = read_lines("jokes.txt")
    print(f"📢 {len(posts)} постов → {CHANNEL}, интервал {INTERVAL_SEC} с")
    for i, post in enumerate(posts, 1):
        bot.send_message(CHANNEL, f"😄 {post}")
        print(f"✅ отправлен пост {i}/{len(posts)}")
        if i < len(posts):
            time.sleep(INTERVAL_SEC)
    bot.send_message(CHANNEL, "😔 Анекдоты закончились...")
