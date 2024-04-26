from aiogram import types
from database.agents_database import get_agent_for_user
from model.gigachat_model import get_answer


def text_message_handler(dp, bot):
    @dp.message_handler()
    async def echo(message: types.Message):
        current_agent_name = get_agent_for_user(message.from_user.id)
        if current_agent_name is None:
            await bot.send_message(chat_id=message.chat.id, text="агент не выбран")
        else:
            answer = get_answer(message.text, message.from_user.id, current_agent_name)[
                "result"
            ]
            await bot.send_message(chat_id=message.chat.id, text=answer)
