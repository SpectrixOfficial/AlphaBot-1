import discord
import asyncio
import time
import datetime
from time import ctime
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import aiohttp


class ModerationCog:
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=["c"])
    @commands.guild_only()
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
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User cleared {number} messages | {datetime.datetime.now().ctime()}")

            except discord.Forbidden:
                await ctx.send(":x: **Make Sure i Have `manage_messages` Permission**")
                print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A CLear Command But checks discord.Forbidden Failed | {datetime.datetime.now().ctime()}")

              
        else:
            await ctx.send(f"Hi {ctx.message.author.mention} You are not permitted with the role `manage_message` feature")
            print(f"Server ID | {ctx.author.guild.id} | Server Name | {ctx.author.guild} | Author Name: {ctx.author} | Author ID: {ctx.author.id} | User Attempted A CLear Command | {datetime.datetime.now().ctime()}")
            



    @commands.command(aliases=["b"])
    @commands.guild_only()
    async def ban(self, ctx, user : discord.Member, *, banReason=None):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == 373256462211874836:
            if user == ctx.author:
                await ctx.send("**You Can't Ban Yourself**", delete_after=3.0)
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


    @commands.command(aliases=["k"])
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, kickReason=None):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == 373256462211874836:
            if user == ctx.author:
                await ctx.send("**You Can't Kick Yourself....**")
                await ctx.message.delete()
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




    @commands.command(aliases=["perms", "checkperms"])
    @commands.guild_only()
    async def permissions(self, ctx, *, member : discord.Member=None):

        if not member:
            member = ctx.author

        perms = "\n".join(perm for perm, value in member.guild_permissions if value)

        permEmbed = discord.Embed(title=f"Permissions For {member}:", description=ctx.guild.name, color=discord.Color(value=0x2a446d))
        permEmbed.set_author(icon_url=member.avatar_url, name=str(member))
        permEmbed.add_field(name="Listed Down Below", value=perms)
        await ctx.send(embed=permEmbed)


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
        print("==================\nModeration Cog Is Loaded\n==================")


def setup(bot):
    bot.add_cog(ModerationCog(bot))
