# This example requires the 'message_content' privileged intents

import os
import random
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

list = ["1", "2"]
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# @bot.command()
# async def hello(ctx):
#     await ctx.send(random.choice(list)


bot.run(os.environ["DISCORD_TOKEN"])
