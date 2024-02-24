import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class randomColorRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def rc(self, ctx, arg1):
        await ctx.message.delete()
        while True:
            await asyncio.sleep(1)
            guild = ctx.guild
            role = get(guild.roles, name=arg1)
            color = discord.Color.random()
            await role.edit(colour=color)

async def setup(client):
    await client.add_cog(randomColorRole(client))