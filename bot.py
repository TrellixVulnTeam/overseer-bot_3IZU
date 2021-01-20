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



# OpenWeatherMap
#api_key = '#'
#base_url = 'http://api.openweathermap.org/data/2.5/weather?'

#Discord Login
client.run('TOKEN')
