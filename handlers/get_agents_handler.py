from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from database.agents_database import get_agent_names, set_agent_for_user, get_agent_info


def create_buttons_by_agent_name(agents_names: list[str]):
    button = []
    for name in agents_names:
        button.append(types.InlineKeyboardButton(text=name, callback_data=name))
    return button


def get_agent_handler(dp, bot):
    @dp.message_handler(commands=["agents"])
    async def get_data_handler(message: Message):
        agents = get_agent_names(message.from_user.id)
        buttons = create_buttons_by_agent_name(agents)

        keyboard = types.InlineKeyboardMarkup()
        for button in buttons:
            keyboard.add(button)
        await message.answer("Choose an option:", reply_markup=keyboard)

    @dp.callback_query_handler(lambda query: True)
    async def handle_callback_query(query: types.CallbackQuery):
        user_id = query.from_user.id
        agent_name = query.data
        set_agent_for_user(user_id, agent_name)
        agent_info = get_agent_info(user_id, agent_name)
        answer = create_select_agent_answer(
            agent_info["name"],
            agent_info["scientific_article"],
            agent_info["description"],
        )
        await bot.send_message(user_id, answer, parse_mode="HTML")


def create_select_agent_answer(name, prompt, description):
    return f"""
    <b>Выбран агент: </b> {name} 
    <b>Инициализирующий промпт: </b> {prompt}
    <b>Описание:</b> {description}
    """
