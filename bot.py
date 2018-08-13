import discord, asyncio, time, datetime
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp
import json 
from discord.ext.commands.cooldowns import BucketType
import os


                         
bot = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True, clean_content=True, owner_id=373256462211874836)
bot.remove_command("help")


startup_extensions = ['cogs.moderation',
                      'cogs.owner',
                      'cogs.home',
                      'cogs.eventhandler',
                      'cogs.server']

 
if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)
            

@bot.event
async def on_ready():
    print("Connected To Use")
    print(f'{bot.user.name} Is Online!')
    print(f'I Am In {len(bot.guilds)} Guilds')
    print(f'Current Version For Discord Bot : {discord.__version__}')
    print(f'Time And Date {datetime.datetime.now().ctime()}')

f = open("token.txt")
bot.run(f.read())
