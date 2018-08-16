import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp
import json


class EventHandlerCog:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()
    
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(name=f".help | {len(self.bot.guilds)} Servers!", type=0))
        print("Bot Events Are Loaded")

    async def on_guild_join(self, guild):
        await self.bot.change_presence(activity=discord.Activity(name=f".help | {len(self.bot.guilds)} Servers!", type=0))


    async def on_guild_leave(self, guild):
        await self.bot.change_presence(activity=discord.Activity(name=f".help | {len(self.bot.guilds)} Servers!", type=0))

    



def setup(bot):
    bot.add_cog(EventHandlerCog(bot))
