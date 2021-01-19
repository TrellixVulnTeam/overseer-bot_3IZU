import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases = ['purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 2):
        await ctx.channel.purge(limit = amount)
        await ctx.send(f'cleared {amount} messages')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(" :x: You do not have the required permissions to use that.")

    @commands.command(aliases = ['boot'])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, Reason = None):
        await ctx.guild.kick(member) #client.kick and ctx.kick are no longer supported;
        await ctx.send(f':boot: {member} has been kicked from the server!')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(" :x: You do not have the required permissions to use that.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x: You forgot to mention the user you'd like to kick.")

    @commands.command(aliases = ['banish'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, Reason = None):
        await ctx.guild.kick(member) #client.kick and ctx.kick are no longer supported;
        await ctx.send(f':hammer_pick: {member} has been kicked from the server!')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(" :x: You do not have the required permissions to use that.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x: You forgot to mention the user you'd like to ban.")
            
    @commands.command(aliases = ['silence'])
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, member: discord.Member, *, Reason = None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name='Muted')
        if not mutedRole:
            mutedRole = await guild.create_role(name='Muted')
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=True)
        await member.add_roles(mutedRole)
        await member.send(f':mute: You have been muted in **{guild}**')
        await ctx.send(f':mute: {member} has been muted!')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(" :x: You do not have the required permissions to use that.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x: You forgot to mention the user you'd like to mute.")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def unmute(self, ctx, member: discord.Member, *, reason = None):
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name='Muted')
            await member.remove_roles(mutedRole)
            await ctx.send(f"{member} is now unmuted")

def setup(client):
    client.add_cog(Moderation(client))
