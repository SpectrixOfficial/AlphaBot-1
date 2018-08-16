import discord
import asyncio
import time
import datetime
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp


class PermissionsCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["perms", "checkperms"])
    @commands.guild_only()
    async def permissions(self, ctx, *, member : discord.Member=None):

        if not member:
            member = ctx.author

        perms = "\n".join(perm for perm, value in member.guild_permissions if value)

        permEmbed = discord.Embed(title=f"Permissions For {member}:", description=ctx.guild.name, color=discord.Color(value=0x2a446d))
        permEmbed.set_author(icon_url=member.avatar_url, name=str(member))
        permEmbed.add_field(name="Listed Down Below", value=perms)
        await ctx.send(embed=permEmbed)


   

    async def on_ready(self):
        print("PermissionsCog Is Loaded")


def setup(bot):
    bot.add_cog(PermissionsCog(bot))
