import discord
from discord.ext import commands

class ban_kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        await ctx.send(f'{member} was kicked with reason: {reason}!', delete_after=60)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send(f'{member} was banned with reason: {reason}!', delete_after=60)

async def setup(client):
    await client.add_cog(ban_kick(client))