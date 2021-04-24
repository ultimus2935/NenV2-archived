import discord
from discord.ext import commands

import os
import json
from datetime import datetime as dt  
from random import choice

from decouple import config

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

data = json.load(open('data.json', 'r'))
client = commands.Bot(command_prefix=data['prefix'], case_insensitive=True, intents=intents)
client.remove_command('help')

# Load all Extensions
def loadCogs():
    for filename in os.listdir("extensions"):
        if filename.endswith(".py"):
            try: 
                extname = f"extensions.{filename[:-3]}"                            
                client.load_extension(extname)
                print(f" * '{extname}'  has been loaded")
            except Exception as e: print(e)
                
# Ready Message
@client.event
async def on_ready():
    print(f'\n * Logged in as {client.user.name}#{client.user.discriminator} \n * Time: {dt.now()}\n * Total Servers: {len(client.guilds)} \n')
    await client.change_presence(activity=discord.Game(name='sacred_numbers.exe'))
    loadCogs()
    print("\n   Nen is online and fully functional!")
        

# Defualt Message
@client.command()
async def nen(ctx):
    emojis = ['🐖', '🐕‍🦺', '🦙', '🐅', '🐍', '🐑', '🐧', '🐒']
    await ctx.send('Nen Nen Nhentai, hello senpai! ' + choice(emojis))

keep_alive()
client.run(config('token'))
