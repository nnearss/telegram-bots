### 🤖 telegram-боты · telegram bots

семь ботов от простого к сложному: эхо, справочник из википедии, кнопки, гороскоп, автопостинг в канал, чат-бот с нечётким поиском и асинхронный бот на aiogram 3. каждый бот это отдельный скрипт, токен хранится в `.env`, а не в коде
*seven bots from simple to advanced: echo, wikipedia lookup, buttons, horoscope, channel autoposting, a fuzzy-matching faq bot and an async aiogram 3 bot. each bot is its own script, and the token lives in `.env`, not in the code*

`python` `pytelegrambotapi` `aiogram 3` `asyncio` `rapidfuzz` `wikipedia api`

---

**боты** · *bots*

| # | бот · bot | что умеет · what it does | чему учит · skills |
|---|---|---|---|
| 01 | [эхо](bots/01_echo.py) · *echo* | повторяет сообщения, команды /start и /help | обработчики команд и текста |
| 02 | [всезнайка](bots/02_wiki.py) · *wiki* | присылает краткое описание слова из википедии | внешний api, очистка текста регулярками |
| 03 | [кнопки](bots/03_buttons.py) · *buttons* | случайная новость или афоризм по кнопке | reply-клавиатура, данные из файлов |
| 04 | [гороскоп](bots/04_horoscope.py) · *horoscope* | собирает предсказание из случайных частей по знаку | проверка ввода, генерация текста |
| 05 | [постинг в канал](bots/05_channel_poster.py) · *channel poster* | публикует посты из файла по таймеру | бот-администратор канала |
| 06 | [faq-чат](bots/06_faq_chat.py) · *faq chat* | находит самый похожий вопрос в базе и отвечает | нечёткий поиск rapidfuzz, порог похожести |
| 07 | [бот на aiogram](bots/07_aiogram_links.py) · *aiogram* | меню-кнопки и inline-кнопки со ссылками | async/await, фильтры, inline-клавиатура |

тексты для ботов 03, 05 и 06 лежат в [`data/`](data/), их можно менять без правки кода
*texts for bots 03, 05 and 06 live in [`data/`](data/) and can be edited without touching code*

---

**как запустить** · *how to run*

1. создайте бота у [@BotFather](https://t.me/BotFather) командой `/newbot` и скопируйте токен
2. установите зависимости и вставьте токен:

```bash
pip install -r requirements.txt
cp .env.example .env       # вставьте BOT_TOKEN
python bots/01_echo.py     # или любой другой бот
```

бот работает, пока запущен скрипт. для бота 05 добавьте его администратором в канал и укажите `CHANNEL` в `.env`
*the bot runs while the script is running. for bot 05, make it a channel admin and set `CHANNEL` in `.env`*

---

**что поменяла по сравнению с лабой** · *changes from the original lab*

- лаба была одним ноутбуком для colab, теперь это отдельные скрипты с общим конфигом
- токен больше не вставляется в код, а читается из `.env`, который не попадает в git
- `fuzzywuzzy` заменила на `rapidfuzz`: тот же интерфейс, но библиотека поддерживается и работает быстрее
- в боте на aiogram команда `/ссылки` не работала, потому что команды в telegram пишутся только латиницей. теперь это `/links`

*the colab notebook became standalone scripts with shared config; the token moved from code to `.env`; `fuzzywuzzy` became the maintained `rapidfuzz`; the cyrillic `/ссылки` command (telegram only allows latin commands) became `/links`*

---

лабораторная работа по разработке telegram-ботов, мтуси
*a university lab on telegram bot development, mtuci*
