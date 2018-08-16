import discord, asyncio, time, datetime
from time import ctime
from discord.ext import commands

class KickCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["k"])
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, kickReason=None):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == 373256462211874836:
            if user == ctx.author:
                await ctx.send("**You Can't Kick Yourself....**")
                await ctx.message.delete()
            elif user == self.bot.user:
                await ctx.send("I Can't Kick Myself Y'know")
            else:
                try:
                    await user.kick(reason=f"{user} Kicked By {ctx.author}, User ID: {ctx.author.id}, Reason:{kickReason}")
                    await ctx.send(f"**Kicked {user} By {ctx.author.mention} With Reason Of:** {kickReason}")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User kicked {user} with reason of {kickReason}  | {datetime.datetime.now().ctime()}")

        
                except discord.Forbidden:
                    await ctx.send(":x: **Make Sure I Have `kick_members` Permission**")
                    print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A Kick Command But Permissions was restricted| {datetime.datetime.now().ctime()}")
  
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} You Do Not Have Correct Permissions, `kick_members` is required")

    async def on_ready(self):
        print("KickCog Is Loaded")

def setup(bot):
    bot.add_cog(KickCog(bot))
