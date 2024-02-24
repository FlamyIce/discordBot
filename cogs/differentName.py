import discord
from discord.ext import commands
import asyncio

class differentName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def differentName(self, ctx, member: discord.Member, arg1, arg2,arg3):
        await ctx.message.delete()
        nicks = [arg1, arg2, arg3]
        i = 0
        while True:
            await asyncio.sleep(2)
            await member.edit(nick = nicks[i])
            i+=1
            if i==len(nicks):
                i = 0

async def setup(client):
    await client.add_cog(differentName(client))
