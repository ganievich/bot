from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Твой токен от BotFather
TOKEN = "7348973950:AAHoxJe03ITSSmiFQatp-nOx6-7t4-AjyIg"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавиатура с основными разделами
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton("🔹 Как зарегистрироваться"))
main_keyboard.add(KeyboardButton("🛒 Как покупать на Pinduoduo"))
main_keyboard.add(KeyboardButton("📦 Доставка в Аксукент"))
main_keyboard.add(KeyboardButton("❓ Задать вопрос"))

# Команда /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе разобраться с покупками на Pinduoduo. Выбери нужный раздел:",
        reply_markup=main_keyboard
    )

# Ответы на кнопки
@dp.message_handler(lambda message: message.text == "🔹 Как зарегистрироваться")
async def registration_info(message: types.Message):
    await message.answer(
        "1️⃣ Установи приложение Pinduoduo 📲\n"
        "2️⃣ Зарегистрируйся с китайским номером или через WeChat 📧\n"
        "3️⃣ Заполни профиль и настрой адрес доставки 📍"
    )

@dp.message_handler(lambda message: message.text == "🛒 Как покупать на Pinduoduo")
async def buying_info(message: types.Message):
    await message.answer(
        "1️⃣ Выбери товар и добавь в корзину 🛍️\n"
        "2️⃣ Проверь скидки и групповые покупки 📉\n"
        "3️⃣ Оплати через WeChat Pay или Alipay 💳"
    )

@dp.message_handler(lambda message: message.text == "📦 Доставка в Аксукент")
async def delivery_info(message: types.Message):
    await message.answer(
        "1️⃣ Используй посредников для доставки 🚛\n"
        "2️⃣ Популярные сервисы: Cainiao, CDEK 📦\n"
        "3️⃣ Время доставки: 15-30 дней ⏳"
    )

@dp.message_handler(lambda message: message.text == "❓ Задать вопрос")
async def ask_question(message: types.Message):
    await message.answer("Задай свой вопрос, и я постараюсь помочь! 😊")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
