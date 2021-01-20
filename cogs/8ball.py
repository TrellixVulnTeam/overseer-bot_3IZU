import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random

class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['8ball', 'ask'])
    async def _8ball(self, ctx, *, question):
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
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x: Ask me a question first!")

def setup(client):
    client.add_cog(_8ball(client))
