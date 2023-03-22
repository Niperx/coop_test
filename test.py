import openai
import aiogram
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
load_dotenv()
openai.api_key = os.getenv('OPEN_AI_TOKEN')
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


class ChatStage(StatesGroup):
    waiting_for_request = State()


def get_answer(input_text, messages):
    content = input_text
    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})
    return messages


@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    messages = []
    await state.update_data(info=messages)
    await message.answer("Разговорный бот, пиши что хочешь")


@dp.message_handler(content_types=['text'])
async def answer(message: types.Message, state: FSMContext):
    info = await state.get_data()
    ans = get_answer(message.text, info['info'])
    print(ans)
    await state.update_data(info=ans)
    await message.answer(ans[-1]['content'])


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
