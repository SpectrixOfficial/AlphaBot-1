import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands

class SoftBanCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["sb"])
    @commands.guild_only()
    async def softban(self, ctx, user : discord.Member, *, softbanReason=None):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == 373256462211874836:
            if user == ctx.author:
                await ctx.send("*you can't softban yourself*", delete_after=3.0)
            else:
                try:
                    await user.ban(reason=f"Softbanned {user} By {ctx.author}, User ID: {ctx.author.id}, Reason:{softbanReason}", delete_message_days=7)
                    await user.unban(reason="Read Latest Ban Log")
                    await ctx.send(f"*Softbanned {user} With Reason Of:*`{softbanReason}`")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User softbanned {user} with reason of {softbanReason} | {datetime.datetime.now().ctime()}")
                except discord.Forbidden:
                    await ctx.send(":x: **Make Sure I Have `ban_members` Permission**")
        else:
            await ctx.send(f"*Hey {ctx.author.mention} You Do Not Have Correct Permissions, `ban_members` is required*", delete_after=1.0)
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A softBan Command | {datetime.datetime.now().ctime()}")

    async def on_ready(self):
        print("SoftBanCog Is Loaded")

def setup(bot):
    bot.add_cog(SoftBanCog(bot))
