from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers import create_agent_handlers, get_agent_handler, text_message_handler, base_command_handler, delete_command_handler

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)

base_command_handler(dp, bot)
delete_command_handler(dp, bot)
create_agent_handlers(dp, bot)
get_agent_handler(dp, bot)
text_message_handler(dp,bot)


if __name__ == "__main__":
    executor.start_polling(dp)
