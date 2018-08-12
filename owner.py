import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp
from collections import Counter
import random
import math
import os




class OwnerCog:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()
    



    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')


    async def __local_check(self, ctx):
        return await self.bot.is_owner(ctx.author)


    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
     


    @commands.is_owner()
    @commands.command(hidden=True, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
            try:
                await ctx.message.add_reaction(emoji='❌')
            except:
                pass

        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction(emoji='☑')
            except:
                pass
    	    
            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
                    
            else:    
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')




    @commands.is_owner()
    @commands.command(aliases=["rl"])
    async def reload(self, ctx, *, cog):
        try:
            try: 
                self.bot.unload_extension(f"cogs.{cog}")
                self.bot.load_extension(f"cogs.{cog}")
                await ctx.send(f"***:stopwatch: Reloaded cogs.{cog}***")
            except Exception as e:
                await ctx.send(f"```{e}```")
                
        except ModuleNotFoundError:
            try:
                self.bot.unload_extension(f"cogs.{cog}")
                self.bot.load_extension(f"cogs.{cog}")
            except Exception as e:
                await ctx.send(f"Couldn't load Cog, cogs.{cog} ERROR MESSAGE:\n```{e}```")


    @commands.is_owner()        
    @commands.command(aliases=["l"])
    async def load(self, ctx, *, cog):
        try:
            try: 
                self.bot.load_extension(f"cogs.{cog}")
                await ctx.send(f":stopwatch: Loaded cogs.{cog}.")
                await ctx.message.add_reaction(emoji="☑")
            except Exception as e:
                await ctx.send(f"```{e}```")
                await ctx.message.add_reaction(emoji="❌")
               
        except ModuleNotFoundError:
            try:
                self.bot.load_extension(f"cogs.{cog}")
            except Exception as e:
                await ctx.send(f"Couldn't load Cog, cogs.{cog} ERROR MESSAGE: ```{e}```")
                await ctx.message.add_reaction(emoji="❌")

    @commands.is_owner()
    @commands.command(aliases=["ul"])
    async def unload(self, ctx, *, cog):
        try:
            try:
                self.bot.unload_extension(f"cogs.{cog}")
                await ctx.send(f":stopwatch: Unloaded cogs.{cog}.")
                await ctx.message.add_reaction(emoji="☑")

            except Exception as e:
                await ctx.send(f"```{e}```")
                await ctx.message.add_reaction(emoji="❌")

        except ModuleNotFoundError:
            try:
                self.bot.unload_extension(f"cogs.{cog}")
            except Exception as e:
                await ctx.send(f":thumbsdown: Couldn't unload Cog, cog.{cog} ERROR MESSAGE: ```{e}```")
                await ctx.message.add_reaction(emoji="❌")


    async def on_ready(self):
        print("Owner Cog Is Loaded For Updates!")

    @commands.is_owner()
    @commands.command()
    async def die(self, ctx):
        await self.bot.logout()




def setup(bot):
    bot.add_cog(OwnerCog(bot))