import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Вакансии")],
        [KeyboardButton(text="👤 Я соискатель"), KeyboardButton(text="🤝 Я рекрутер")],
        [KeyboardButton(text="📞 Связаться с менеджером")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в NEXUS Работа.\n\n"
        "Здесь ты можешь найти работу или работать с вакансиями.",
        reply_markup=menu
    )

@dp.message()
async def buttons(message: Message):
    if message.text == "🔎 Вакансии":
        await message.answer("📋 Пока вакансий нет. Скоро здесь появятся актуальные предложения.")

    elif message.text == "👤 Я соискатель":
        await message.answer("👤 Раздел соискателя.\n\nЗдесь будет анкета и отклики на вакансии.")

    elif message.text == "🤝 Я рекрутер":
        await message.answer("🤝 Раздел рекрутера.\n\nЗдесь можно будет передавать кандидатов и отслеживать выплаты.")

    elif message.text == "📞 Связаться с менеджером":
        await message.answer("📞 Связь с менеджером будет настроена следующим шагом.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
