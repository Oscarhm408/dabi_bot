# This example requires the 'message_content' privileged intents

import os
import random 
import discord
import json
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
    
@bot.command()
async def praise(ctx):
    await ctx.send(random.choice(json.loads(os.environ["praise_list"])))
    
@bot.command()
async def dabi(ctx):
    await ctx.send(random.choice(json.loads(os.environ["dabi_quotes"])))

                   
bot.run(os.environ["DISCORD_TOKEN"])
