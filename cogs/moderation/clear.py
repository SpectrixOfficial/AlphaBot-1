import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
   

class ClearCog:
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(aliases=["c"])
    async def clear(self, ctx, number: int):
        if ctx.message.author.guild_permissions.manage_messages or ctx.message.author.id == 373256462211874836:
            try:
                if number > 1000:
                    number = 1000 
                
                if number == 1:
                    msg = "message"
                else:
                    msg = 'messages'

                amt = await ctx.channel.purge(limit=number + 1)
                await asyncio.sleep(1)
                await ctx.send(f"**Cleared `{len(amt) - 1}` {msg}**", delete_after=1.75)
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User cleared {len(amt)} messages | {datetime.datetime.now().ctime()}")

            except discord.Forbidden:
                await ctx.send(":x: **Make Sure i Have `manage_messages` Permission**")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A CLear Command But checks discord.Forbidden Failed | {datetime.datetime.now().ctime()}")

              
        else:
            await ctx.send(f"Hi {ctx.message.author.mention} You are not permitted with the role `manage_message` feature")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A CLear Command | {datetime.datetime.now().ctime()}")
   
    async def on_ready(self):
        print("ClearCog Is Loaded")

def setup(bot):
    bot.add_cog(ClearCog(bot))
