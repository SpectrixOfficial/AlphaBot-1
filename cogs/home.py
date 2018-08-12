import discord, asyncio, time, datetime, json
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp
import json
from discord.ext.commands.cooldowns import BucketType



class HomeCog:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()
    
    @commands.command()
    async def prefix(self, ctx):
        await ctx.send("My Current Prefix Is `.` and is Mandatory")
 

    @commands.command(aliases=["halp"])
    async def help(self, ctx):
        helpEmbed = discord.Embed(colour=discord.Colour(value=0x2a446d))
        helpEmbed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
        helpEmbed.add_field(name="For A List Of Public Commands Go Here:", value="https://alphadevelopmentteam.github.io/alphabotsite/alphahelp/commands", inline=True)
        helpEmbed.set_footer(text="Join The Support Server For More Help by .support or .server 👍")
        await ctx.send(embed=helpEmbed)
        print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Sent Help | {datetime.datetime.now().ctime()}")




    @commands.cooldown(1, 10, BucketType.channel)
    @commands.command()
    async def ping(self, ctx):
        ping1 = time.perf_counter()
        ping = await ctx.send(f'Pinging 0/5')
        ping2 = time.perf_counter()
        time1 = ping2 - ping1 
        result1 = round(time1 * 1000)
        ping1 = time.perf_counter()  
        await ping.edit(content="Pinging 1/5") 
        ping2 = time.perf_counter()
        time2 = ping2 - ping1
        result2 = round(time2 * 1000)
        ping1 = time.perf_counter()
        await ping.edit(content="Pinging 2/5")
        ping2 = time.perf_counter()
        time3 = ping2 - ping1
        result3 = round(time3 * 1000)
        ping1 = time.perf_counter()
        await ping.edit(content="Pinging 3/5")
        ping2 = time.perf_counter()
        time4 = ping2 - ping1
        result4 = round(time4 * 1000)
        ping1 = time.perf_counter()
        await ping.edit(content="Pinging 4/5")
        ping2 = time.perf_counter()
        time5 = ping2 - ping1
        result5 = round(time5 * 1000)
        finalresult = round((result1+result2+result3+result4+result5)/5)
        await ping.edit(content="Pinging 5/5, Calculating Average", delete_after=.1)
        

        pingEmbed = discord.Embed(title="Ping", description=f" Hey {ctx.author.name} I Calculated The Average Response Time", color=discord.Color(value=0x2a446d))
        pingEmbed.set_author(name=f"Calculated Result")
        pingEmbed.add_field(name="Pong 1", value=f"{result1}ms", inline=False)
        pingEmbed.add_field(name="Pong 2", value=f"{result2}ms", inline=None)
        pingEmbed.add_field(name="Pong 3", value=f"{result3}ms", inline=False)
        pingEmbed.add_field(name="Pong 4", value=f"{result4}ms", inline=False)
        pingEmbed.add_field(name="Pong 5", value=f"{result5}ms", inline=False)
        pingEmbed.add_field(name="Pong Average", value=f"{finalresult}ms", inline=True)
        pingEmbed.add_field(name="Bot Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        await ctx.send(embed=pingEmbed)
        print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} |  Author Name: {ctx.author} | Author ID: {ctx.author.id} | Pinged With An Average Of {finalresult}ms | {datetime.datetime.now().ctime()}")

       
       
        


    @commands.command()
    async def poll(self, ctx,* , pollmessage):
        pollEmbed = discord.Embed(color=discord.Color(value=0x2a446d))
        pollEmbed.set_author(name="Every Vote Counts, So Vote Now")
        pollEmbed.add_field(name=f"{pollmessage}", value="Submitted Poll" , inline=True)  
        pollEmbed.set_footer(text=f"{ctx.message.author} Made Poll | {datetime.datetime.now().date()}")
        msg = await ctx.send(embed=pollEmbed)
        await msg.add_reaction(emoji="👍")
        await msg.add_reaction(emoji="👎")

        print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} | Author ID: {ctx.author.id} | Made A Poll: {pollmessage} | {datetime.datetime.now().ctime()}")
                



    @commands.command(aliases=["server"])
    async def support(self, ctx):
        await ctx.send(f"***{ctx.message.author.mention} Heres My Support Server\nhttps://discord.gg/bSHu5cb***")
        print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} |  Author Name: {ctx.author} | Author ID: {ctx.author.id} | Sent My  Server Invite | {datetime.datetime.now().ctime()}")

    


    @commands.command()
    async def invite(self, ctx):
        try:
            await ctx.send("***I have DM you with my invite***")
            await ctx.author.send(f"https://bit.ly/alpha-bot-invite")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} |  Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Sent My Invite | {datetime.datetime.now().ctime()}")
        except Exception:
            await ctx.send("***I have DM you with my invite***")
            await ctx.author.send(f"https://bit.ly/alpha-bot-invite")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Sent My Invite | {datetime.datetime.now().ctime()}")


    @commands.cooldown(3, 30, BucketType.guild)
    @commands.command()
    async def feedback(self, ctx,* , message):
        try:
            channel = self.bot.get_channel(473181437365977089)  
            fb = discord.Embed(title="Feedback :ballot_box_with_check: ", color=discord.Color(value=0x2a446d))   
            fb.add_field(name=f"Feedback Username: {ctx.author} |", value=f" User ID: {ctx.author.id}", inline=False)
            fb.add_field(name=f"Server Name: {ctx.author.guild}", value=f"Server ID: {ctx.author.guild.id}", inline=False)
            fb.add_field(name=f"Feedback Text", value=message, inline=False)
            await channel.send(embed=fb)
            await ctx.send("***Feedback Sent, Thank You***")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} |  Channel Name: {ctx.channel} | Channel ID: {ctx.channel.id} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | Sent Feedback: {message} | {datetime.datetime.now().ctime()}")
       
        except:
            await ctx.send(f"**Hey, I am In Cooldown For The Server Try Again in A Couple Of Seconds\nPlease Note This Is For Less Traffic**")

    async def on_ready(self):
        print("Home Cog Is Loaded")


def setup(bot):
    bot.add_cog(HomeCog(bot))
