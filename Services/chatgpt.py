from typing import List

from openai import AsyncOpenAI
import os
import asyncio
# aclient = AsyncOpenAI()
from openai import OpenAI

from Models.Chord import Chord

API_KEY = open("API_KEY", "r").read().strip()
os.environ['OPENAI_API_KEY'] = API_KEY


async def get_response2():
    aclient = AsyncOpenAI(api_key=API_KEY)
    completion = await aclient.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": "What's up with it"}])

    print(completion.choices[0].message.content)


async def get_response(message: str, mock: bool = False) -> str:
    if mock:
        response: str = "offline - mock response"
        return response
    aclient = AsyncOpenAI(api_key=API_KEY)
    completion = await aclient.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": message}])
    response: str = completion.choices[0].message.content

    print()
    return response


def test_response():
    asyncio.run(get_response2())


def find_key(chord_list: List[Chord]):
    chord_list_string = ""
    for chord in chord_list:
        chord_name = chord.chord_name
        chord_list_string += f'{chord_name}, '

    message: str = f'What key is this list of chords? {chord_list_string}'
    print(asyncio.run(get_response(message, mock=False)))

