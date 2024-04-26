from aiogram.types import Message
from aiogram import Bot
from database.agents_database import delete_agent, check_agent_exists


def delete_command_handler(dp, bot: Bot):
    @dp.message_handler(commands=["delete"])
    async def get_data_handler(message: Message):
        text = message.text
        agent_name = text[text.find(' ')+1:]
        user_id = message.from_user.id
        if check_agent_exists(user_id, agent_name):
            delete_agent(message.from_user.id,agent_name)
            await bot.send_message(text=DELETE_SUCSECC_MESSAGE(agent_name), chat_id=message.chat.id, parse_mode="HTML")
        else:
            await bot.send_message(text=DELE_ERROR_MESSAGE(agent_name), chat_id=message.chat.id, parse_mode="HTML")


DELETE_SUCSECC_MESSAGE = lambda agent_name: f"Агент <b>{agent_name}</b> успешно удален!"
DELE_ERROR_MESSAGE = lambda agent_name: f"Агент с именем <b>{agent_name}</b> не найден"