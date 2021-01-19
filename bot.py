import asyncio
import json
import random
import os

import discord
import requests
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,
    activity=discord.Game("with my creator's feelings."))
    print('Logged into Discord API.')

#@client.event
#async def on_command_error(ctx, error):
#    if isinstance(error, CommandNotFound):
#        await ctx.send(":x: That command doesn't exist!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

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

# OpenWeatherMap
#api_key = '#'
#base_url = 'http://api.openweathermap.org/data/2.5/weather?'

#Discord Login
client.run('TOKEN')
