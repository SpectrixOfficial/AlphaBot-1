import discord, asyncio, time, datetime
from time import ctime
from discord.ext import commands

class BanCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["b"])
    @commands.guild_only()
    async def ban(self, ctx, user : discord.Member, *, banReason=None):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == 373256462211874836:
            if user == ctx.author:
                await ctx.send("**You Can't Ban Yourself**", delete_after=3.0)
            elif user == self.bot.user:
                await ctx.send("I Can't Ban Myself Y'know")
            else:
                try:
                    await user.ban(reason=f"Banned {user} By {ctx.author}, User ID: {ctx.author.id}, Reason:{banReason}")
                    await ctx.send(f"**Banned {user} From {ctx.author.mention} With Reason of:**{banReason}")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User banned {user} with reason of {banReason} | {datetime.datetime.now().ctime()}")

                except discord.Forbidden:
                    await asyncio.sleep(1)
                    await ctx.send(f":x: **Make Sure I Have `ban_members` Permission**")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Ban CMD failed; Discord.Forbidden | {datetime.datetime.now().ctime()}")

            
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} You Do Not Have Correct Permissions, `ban_members` is required")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A Ban Command | {datetime.datetime.now().ctime()}")
   
    async def on_ready(self):
        print("BanCog Is Loaded")


def setup(bot):
    bot.add_cog(BanCog(bot))
