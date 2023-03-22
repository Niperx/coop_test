import openai
openai.api_key = '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'
aaa = input()
messages = []
who_is = input("Кем будет являться чат GPT в данном диалоге: ")
print("Изменения")
while True:
    content = input("User: ")
    messages.append({"role": "assistant", "content": who_is})
    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})

# response = openai.Image.create(
#     prompt=aaa,
#     n=1,
#     size="256x256",
# )
#
# print(response["data"][0]["url"])



# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer("Привет!\n"
#                          "Отвечу на вопросы мира")
#
#
# @dp.message_handler(content_types=['text'])
# async def answer(message: types.Message):
#     question = message.text
#     ans = get_answer(question)
#     await message.answer(ans)
#
#
# if __name__ == '__main__':
#     aiogram.executor.start_polling(dp)
