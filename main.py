import os
import discord
import requests
import random
import json
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dabi_quotes = [
    "I’ve seen you in pictures, but I gotta say you’re way grosser in person.",
    "First thing we have to do, is take away their sense of peace.",
    "Is it cuz your students are so precious? Hope you got what it takes to protect them… See ya later.",
    "You’re so weak… you couldn’t even stop a criminal organization from abducting your students.",
    "If you’re trash, at least burn and be kindling for my flames.",
    "This will just be a signal fire. We’ll fill those heroes full of holes… and put them in their place. All for a brighter future.",
    "Gathering a bunch of punks who are just strong will only increase the risk.",
    "It’s better to have a small group of experienced elites.",
    "Heroes are forgettable. They try to save the world… but villains are the ones who change it.",
    "Anyway, I will carry out the will of the hero killer.",
    "There's only one girl I've got my eye on, and her name is Rayne",
]

user_dict = {
    "ni": "Nina",
    "ev": "Evan",
    "ri": "Riri",
    "ma": "Mari",
    "Ra": "Rayne"
}

dabi_response = [
    "hey what's up",
    "yes im here",
    "sorry i was a lil nervous, hi",
    "what do you want",
    "hey wyding",
    "miss u",
    "hop on fortnite later?",
    "hi, watching anime rn",
    "sorry just woke up haha hi",
]
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.lower() == "!me":
        messages = [message async for message in message.channel.history(limit=5)]
        last_message = messages[1].content
        s = last_message.split(" ")
        print(last_message)
        print(s)
        for word in s:
            print(word.lower())
            print(type(word))
            if word.lower() in ["im", "i", "i'm", "idk", "idc"]:
                print(True)
                index = s.index(word)
                phrase = (" ".join(s[index:]))
                print(phrase)
                await message.channel.send(f"me when {phrase}")

    elif message.content.lower() == "!jesus":
        await message.channel.send(file=discord.File("jesus.gif"))

    elif message.content.lower() == "!dabi":
        await message.channel.send(random.choice(dabi_quotes))

    elif message.content.lower().startswith("!summon"):
        raw_user = message.content.split(" ")[1]
        if raw_user[:2] == "os":
            await message.channel.send("Oscar, get your sexy ass on fortnite")
        elif raw_user[:2] in user_dict:
            name = user_dict[raw_user[:2]]
        else:
            name = raw_user
        await message.channel.send(name + " , get your ass on fortnite")

    elif message.content.lower() == "!praise":
        await message.channel.send("Sorry, can't do that right now")

    elif "jk" in message.content.lower():
        await message.channel.send("Unless?")

    elif message.content.startswith("!bot"):
        await message.channel.send("yes im here")

    elif message.content.lower() == "!hello":
        await message.channel.send("Hello")

    elif message.content.lower().startswith("hi dabi"):
          async with message.channel.typing():
              type_time = random.uniform(0.5, 4)
              await asyncio.sleep(type_time)
              await message.channel.send(random.choice(dabi_response))


client.run(os.environ["DISCORD_TOKEN"])
