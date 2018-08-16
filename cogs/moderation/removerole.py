import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
   

class RemoveRoleCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def removerole(self, ctx, user: discord.Member, *, role : discord.Role):
        if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id == 373256462211874836:
            try:
                await user.remove_roles(role , reason=f"Role Removed By {ctx.author}, User ID: {ctx.author.id}")
                await ctx.send(f"**I Have Removed Role:`{role}` from {user}**")           
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Removed Role {role} from  {user}|  {datetime.datetime.now().ctime()}")              
            except discord.Forbidden:
                await ctx.send(":x: **Make Sure I Have `manage_roles` Permission**", delete_after=1.0)
        else:
            await ctx.send("You seem not to have the role `manage_roles`, ask your guild owner for the role")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Attempted To Remove Role {role} From {user}| {datetime.datetime.now().ctime()}")


    async def on_ready(self):
        print("RemoveRoleCog Is Loaded")


def setup(bot):
    bot.add_cog(RemoveRoleCog(bot))
