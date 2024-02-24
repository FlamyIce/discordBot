from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class price(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def price(self, ctx, arg):
        await ctx.message.delete()
        urlCryp = 'https://www.binance.com/ru/futures/'+arg
        reqsCryp = requests.get(urlCryp)
        soupCryp = BeautifulSoup(reqsCryp.text, 'html.parser')
        for title in soupCryp.find_all('title'):
            crypto = title.get_text()
            cr = crypto.find('|')
            await ctx.send(crypto[0:cr], delete_after=60)

async def setup(client):
    await client.add_cog(price(client))