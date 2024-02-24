from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        await ctx.message.delete()
        if ctx.author.voice:
            ch = ctx.message.author.voice.channel
            await ch.connect()

async def setup(client):
    await client.add_cog(join(client))