import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {message.from_user.username}, я могу транслитерировать твоё сообщение просто отправь его!"
    )


transliteration_mapping = {
    ord("а"): "a",
    ord("б"): "b",
    ord("в"): "v",
    ord("г"): "g",
    ord("д"): "d",
    ord("е"): "e",
    ord("ё"): "e",
    ord("ж"): "zh",
    ord("з"): "z",
    ord("и"): "i",
    ord("й"): "i",
    ord("к"): "k",
    ord("л"): "l",
    ord("м"): "m",
    ord("н"): "n",
    ord("о"): "o",
    ord("п"): "p",
    ord("р"): "r",
    ord("с"): "s",
    ord("т"): "t",
    ord("у"): "u",
    ord("ф"): "f",
    ord("х"): "kh",
    ord("ц"): "ts",
    ord("ч"): "ch",
    ord("ш"): "sh",
    ord("щ"): "shch",
    ord("ъ"): "ie",
    ord("ы"): "y",
    ord("ь"): "",
    ord("э"): "e",
    ord("ю"): "iu",
    ord("я"): "ia",
    ord("А"): "A",
    ord("Б"): "B",
    ord("В"): "V",
    ord("Г"): "G",
    ord("Д"): "D",
    ord("Е"): "E",
    ord("Ё"): "E",
    ord("Ж"): "Zh",
    ord("З"): "Z",
    ord("И"): "I",
    ord("Й"): "I",
    ord("К"): "K",
    ord("Л"): "L",
    ord("М"): "M",
    ord("Н"): "N",
    ord("О"): "O",
    ord("П"): "P",
    ord("Р"): "R",
    ord("С"): "S",
    ord("Т"): "T",
    ord("У"): "U",
    ord("Ф"): "F",
    ord("Х"): "Kh",
    ord("Ц"): "Ts",
    ord("Ч"): "Ch",
    ord("Ш"): "Sh",
    ord("Щ"): "Shch",
    ord("Ъ"): "Ie",
    ord("Ы"): "Y",
    ord("Ь"): "",
    ord("Э"): "E",
    ord("Ю"): "Iu",
    ord("Я"): "Ia",
}


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer(message.text.translate(transliteration_mapping))
    except TypeError:
        await message.answer("Я умею только транслитерировать текс из сообщения.")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="bot.log")
    asyncio.run(main())
