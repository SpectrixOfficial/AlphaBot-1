import time
from time import ctime
import discord
from discord.ext import commands
import asyncio



class servercog:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

  
    @commands.group(invoke_without_command=True)
    async def faq(self, ctx):
        if ctx.author.guild.id == 471336570394378240:
            await ctx.send("Welcome To The Server Exclusives Help Commands\nAll You Need is here\n1: How To report a bug\n2: how to suggest new features\n3: where is the invite\nAll Those Are Just a few words to get to:\n1:`.faq reportbug`\n2:`.faq suggest`\n3:`.faq invite`")
        else:
            await ctx.send("Sorry This Is Only For Alpha Support Server, Please type `.server` for more info")




    @faq.command()
    async def invite(self, ctx):
        if ctx.author.guild.id == 471336570394378240:
            await ctx.send("`Permanent Invite`\nhttps://discord.gg/bSHu5cb")
        else:
            await ctx.send("Sorry Only For Alpha Support Server, Type `.server` for the link")

    @faq.command()
    async def reportbug(self, ctx):
        if ctx.author.guild.id == 471336570394378240:
            await ctx.send("Report here <#471336993738194965>")
        else:
            await ctx.send("Sorry Only For Alpha Support Server , type `.server` to report bugs :}")

    @faq.command()
    async def suggest(self, ctx):
        if ctx.author.guild.id == 471336570394378240:
            await ctx.send("Suggest Here <#471337121056030721>")
        else:
            await ctx.send("Sorry Only For Alpha Support Server, to suggest ,type `.feedback <Suggestion>`  or do this command in the support server again")

 

    



    async def on_ready(self):
        print("Server Feature Exclusive Loaded")

def setup(bot):
    bot.add_cog(servercog(bot))
