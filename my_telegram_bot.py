import openai
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# .env faylini o'qish
load_dotenv()

# API kalitlar (maxfiy ma'lumotlarni .env faylidan olish)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Agar API kalitlari topilmasa, xatolik chiqarish
if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError("TELEGRAM_TOKEN yoki OPENAI_API_KEY noto‘g‘ri o‘rnatilgan!")

# OpenAI API sozlamalari
openai.api_key = OPENAI_API_KEY

# Botni ishga tushiramiz
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Logging
logging.basicConfig(level=logging.INFO)

# Foydalanuvchining xabariga javob berish
@dp.message_handler()
async def chatgpt_response(message: types.Message):
    try:
        # OpenAI API orqali javob olish
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        answer = response["choices"][0]["message"]["content"]
        await message.reply(answer)
    except openai.error.OpenAIError as e:
        # OpenAI bilan bog'liq xatoliklar
        await message.reply("OpenAI xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring.")
        logging.error(f"OpenAI xatolik: {e}")
    except Exception as e:
        # Boshqa umumiy xatoliklar
        await message.reply("Xatolik yuz berdi! ❌ Iltimos, keyinroq qayta urinib ko'ring.")
        logging.error(f"Xatolik: {e}")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
