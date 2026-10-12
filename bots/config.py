"""Общие настройки: токен и пути. Токен берётся из файла .env в корне репозитория."""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
load_dotenv(ROOT / ".env")

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("Нет BOT_TOKEN. Скопируйте .env.example в .env и вставьте токен от @BotFather.")


def read_lines(name: str) -> list[str]:
    """Читает непустые строки из файла в папке data/."""
    text = (DATA / name).read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]
