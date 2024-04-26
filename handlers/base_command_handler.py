from aiogram.types import Message
from aiogram import Bot



def base_command_handler(dp, bot: Bot):
    @dp.message_handler(commands=["start", 'help'])
    async def get_data_handler(message: Message):
        await bot.send_message(text=START_MESSAGE, chat_id=message.chat.id)


START_MESSAGE = \
f"""
Привет 👋 , это чат-бот на основе GigaChat 🗿. Он умеет находить статьи 📄 по интересующей вас области научных исследований 👩‍🔬 и отвечать на вопросы по найденным статьям. 

🧠 Чтобы создать нового агента воспользуйтесь командой /create_agent. Далее нужно ввести его имя, добавить описание для удобной работы, а затем выбрать научную сферу. 
🧠 Чтобы переключаться между агентами используйте команду /agents. Каждый агент будет обладать информацией о фиксированном количестве статей из заданной Вами области.
🧠 Область необходимо писать на английском языке. Если по запросу не находятся статьи, попробуйте перефразировать предложение.
"""