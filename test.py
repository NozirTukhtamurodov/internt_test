'''import openai
openai.api_key = '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'
messages = []
for i in range(20):
    messages.append({"role": "user", "content": input()})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print(response['choices'][0]['message']['content'])
'''
import aiohttp
import asyncio
import json

async def get_chat_completion(model, messages):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.5,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(payload), verify_ssl=False) as response:
            response_json = await response.json()
            return response_json['choices'][0]['message']['content']

model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello!"}]
response = asyncio.run(get_chat_completion(model, messages))
print(response)
