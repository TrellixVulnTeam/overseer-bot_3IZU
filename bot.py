import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import asyncio
import requests
import random
import json

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,
    activity=discord.Game("with my creator's feelings."))
    print('Logged into Discord API.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(":x: That command doesn't exist!")

@client.command(aliases = ['hi'])
async def hello(ctx):
    await ctx.send(f'Hello <@{ctx.message.author.id}>!')

@client.command(aliases = ['ask', '8ball'])
async def _8ball(ctx, *, question):
    responses = [
            "It is certain,",
            "It is decidedly so,",
            "Without a doubt,",
            "Yes - definitely,",
            "You may rely on it,",
            "As I see it, yes,",
            "Most likely,",
            "Outlook good,",
            "Yes,",
            "Signs point to yes,",
            "Reply hazy, try again,",
            "Ask again later,",
            "Better not tell you now,",
            "Cannot predict now,",
            "Concentrate and ask again,",
            "Don't count on it,",
            "My reply is no,",
            "My sources say no,",
            "Outlook not so good,",
            "Very doubtful,"]
    await ctx.send(f"{random.choice(responses)} <@{ctx.message.author.id}>")

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Ask me a question first!")

# Administrator commands

# clear command and error handle
@client.command(aliases = ['purge'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'cleared {amount} messages')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" :x: You do not have the required permissions to use that.")

# kick command and error handle
@client.command(aliases = ['boot'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, Reason = None):
    await ctx.guild.kick(member) #client.kick and ctx.kick are no longer supported;
    await ctx.send(f':boot: {member} has been kicked from the server!')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" :x: You do not have the required permissions to use that.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: You forgot to mention the user you'd like to kick.")

# ban command and error handle
@client.command(aliases = ['banish', 'begone'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, Reason = None):
    await ctx.guild.ban(member) #client.ban and ctx.ban are no longer supported
    await ctx.send(f':hammer_pick: {member} has been banned from the server!')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" :x: You do not have the required permissions to use that.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: You forgot to mention the user you'd like to ban.")
api_key = '34a9fdca0eaadb711592e297787268f1'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
client.run('Nzg0MjA2Nzg5NjU4NDExMDg4.X8l7fA.SzOBipWnj8k8L8nAVEv4NjmebGc')
