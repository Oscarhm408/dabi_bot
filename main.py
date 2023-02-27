# This example requires the 'message_content' privileged intents

import os
import discord
import requests
import random
import json


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
    "Sit on my face",
]

praise_quotes = [
        "Anything for you, Princess",
        "Behave yourself, Princess",
        "Be a good girl for me, Princess",
        "Give me all of you, Princess",
        "yes princess you are the sexiest",
        "keep talking to me like the pretty princess you are",
        "mm i can't wait to see your body princess",
        "good girl",
        "fuuuck you're such a hot princess",
        "Show your clean waxed pussy for me princess",
        "I know its princess pink",
        "I need that princess HEE HEE",
        "where should I cum princess?",
        "ah yes, princess's milk",
        "go reach for your rose princess",
        "I just can't control myself around you princess",
        "Mmm princess, you're doing such a good job",
        "Yeah, keep using that pretty mouth of yours just like that",
        "Why is your face so hot princess? Do you feel okay?",
        "I can't wait to rip those panties off you princess",
]

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message): 
    if message.author == client.user: 
        return 
    
    if message.content.lower() == "!jesus":
        gif = requests.get("https://i.kym-cdn.com/photos/images/newsfeed/002/528/120/c3c.gif")
        await message.channel.send(gif)
    
    if message.content.lower() == "!dabi":
        await message.channel.send(random.choice(dabi_quotes))
    
    if message.content.lower() == "!praise":
        await message.channel.send(random.choice(praise_list))
 
    elif "jk" in message.content.lower():
        await message.channel.send("Unless?")
        
    elif message.content.startswith("!bot"):
        await message.channel.send("bot")

    elif message.content.lower() == "!hello":
        await message.channel.send("Hello")
        

                  
client.run(os.environ["DISCORD_TOKEN"])
