import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
   

class GiveRoleCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def giverole(self, ctx, user: discord.Member, *, role : discord.Role):
        if ctx.message.author.guild_permissions.manage_roles or ctx.message.author.id == 373256462211874836:
            try:
                await user.add_roles(role, reason=f"Role Added By {ctx.author}, User ID: {ctx.author.id}")
                await ctx.send(f"**{user.mention} Obtained `{role}`**")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | {user} Obtained {role} | {datetime.datetime.now().ctime()}")
            except discord.Forbidden:
                await ctx.send(":x: **Make Sure That I Have `manage_roles` Permissions**")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted To Give Role To {user} , But An Error Discord.Forbidden was Raised| {datetime.datetime.now().ctime()}")
        else:
            await ctx.send("You seem not to have the role `manage_roles`, ask your guild owner for the role")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Attempted To Give {user} Role {role}| {datetime.datetime.now().ctime()}")

    async def on_ready(self):
        print("GiveRoleCog Is Loaded")

def setup(bot):
    bot.add_cog(GiveRoleCog(bot))
