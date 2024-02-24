import discord
from discord.ext import commands
import asyncio

class runningRow(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def runningRow(self, ctx,member: discord.Member, arg1):
        await ctx.message.delete()
        i = 0
        while True:
            await asyncio.sleep(1)
            await member.edit(nick = arg1[i:i+len(arg1)])
            i+=1
            if i==len(arg1):
                i = 0

async def setup(client):
    await client.add_cog(runningRow(client))