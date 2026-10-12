"""Асинхронный бот на aiogram 3: reply- и inline-кнопки с полезными ссылками."""

import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton,
                           Message, ReplyKeyboardMarkup)

from config import TOKEN

LINKS_BTN, HELP_BTN = "🔗 Получить ссылки", "❓ Помощь"

reply_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=LINKS_BTN), KeyboardButton(text=HELP_BTN)]],
    resize_keyboard=True,
)
links_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📖 Документация Python", url="https://docs.python.org/ru/3/")],
    [InlineKeyboardButton(text="🤖 Telegram Bot API", url="https://core.telegram.org/bots/api")],
    [InlineKeyboardButton(text="📚 Документация aiogram", url="https://docs.aiogram.dev/")],
])

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Я бот на aiogram. Жми кнопки ниже или /links.", reply_markup=reply_kb)


@dp.message(Command("help"))
@dp.message(F.text == HELP_BTN)
async def help_cmd(message: Message):
    await message.answer("📌 Команды:\n/start — запуск\n/help — справка\n/links — полезные ссылки")


# команды Telegram пишутся только латиницей, поэтому /links, а не /ссылки
@dp.message(Command("links"))
@dp.message(F.text == LINKS_BTN)
async def links(message: Message):
    await message.answer("🔗 Полезные ссылки:", reply_markup=links_kb)


@dp.message()
async def echo(message: Message):
    await message.answer(message.text or "🙂")


async def main():
    print("🚀 Aiogram-бот запущен")
    await dp.start_polling(Bot(token=TOKEN))


if __name__ == "__main__":
    asyncio.run(main())
