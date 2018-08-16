import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
   
class CreateRoleCog:
    def __init__(self, bot):
        self.bot = bot
   
   
   
    @commands.command()
    @commands.guild_only()
    async def createrole(self, ctx,* , rolename):
        if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id == 373256462211874836:
            try:
                guild = ctx.guild
                await guild.create_role(name=rolename , reason=f"Role {rolename}  Created By {ctx.author}, User ID: {ctx.author.id}")
                await ctx.message.delete()
                await ctx.send(f"**Created Role `{rolename}` by `{ctx.author}`**")                         
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Created Role {rolename} | {datetime.datetime.now().ctime()}")
            except discord.Forbidden:
                await ctx.send(":x: **Make Sure I Have `manage_roles` Permission**")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Alpha Blocked From Using createrole  | {datetime.datetime.now().ctime()}")

        else:
            await ctx.send("You seem not to have the role `manage_roles`, ask your guild owner for the role")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted To Create Role | {datetime.datetime.now().ctime()}")

    async def on_ready(self):
        print("CreateRoleCog Is Loaded")


def setup(bot):
    bot.add_cog(CreateRoleCog(bot))
