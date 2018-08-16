import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands


class DeleteRoleCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def deleterole(self, ctx, *, role : discord.Role):
            if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id == 373256462211874836:
                try:
                    await role.delete(reason=f"Role Deleted By {ctx.author}, User ID: {ctx.author.id}")
                    await ctx.send(f"**I deleted `{role}` {ctx.author.mention}**")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Deleted Role {role}| {datetime.datetime.now().ctime()}")              
                except discord.Forbidden:
                    await ctx.send("**:x: Make Sure I Have `manage_role` Permissions**")
            else:
                await ctx.send("*You seem not to have the role `manage_roles`, ask your guild owner for the role*")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Attempted To Delete Role {role}| {datetime.datetime.now().ctime()}")


    async def on_ready(self):
        print("DeleteRoleCog Is Loaded")


def setup(bot):
    bot.add_cog(DeleteRoleCog(bot))
