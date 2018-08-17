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


startup_extensions = ['cogs.framework.eventhandler',
                     'cogs.framework.owner',
                     'cogs.framework.home',
                     'cogs.moderation.ban', 
                     'cogs.moderation.clear',
                     'cogs.moderation.createrole',
                     'cogs.moderation.deleterole',
                     'cogs.moderation.giverole',
                     'cogs.moderation.kick',
                     'cogs.moderation.permission',
                     'cogs.moderation.removerole',
                     'cogs.moderation.softban',
                     'cogs.serverexclusive.server',]

 
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

f = open("C:/Users/Lithimus/Documents/VS Code/Alpha Bot Script(Py)/token.txt")
bot.run(f.read())
