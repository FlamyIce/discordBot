from discord.ext import commands
import dbConnect
from bs4 import BeautifulSoup
import requests

class addCryp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def addCryp(self, ctx, arg):
        await ctx.message.delete()
        arg = arg.upper()
        btcp = 'https://www.binance.com/ru/futures/BTCUSDT'
        btcreqsCryp = requests.get(btcp)
        btcsoupCryp = BeautifulSoup(btcreqsCryp.text, 'html.parser')
        for titlebtc in btcsoupCryp.find_all('title'):
            btccrypT = titlebtc.get_text()
            price = btccrypT.split('|')

        btcPrice = float(price[0])

        btcp = 'https://www.binance.com/ru/futures/'+arg
        reqsCryp = requests.get(btcp)
        soupCryp = BeautifulSoup(reqsCryp.text, 'html.parser')
        for title in soupCryp.find_all('title'):
            crypT = title.get_text()
            price = crypT.split('|')

        price = float(price[0])

        dbConnect.cur.execute("SELECT * FROM cryptocurrency")
        rows = dbConnect.cur.fetchall()
        dbConnect.db.commit()

        crypList = []

        for i in rows:
            crypList.append(i[1])

        if price == btcPrice or arg in crypList:
            await ctx.send('Currency does not exists!', delete_after=60)
        else:
            dbConnect.cur.execute(f"INSERT INTO cryptocurrency(crname) VALUES ('{arg}')")
            dbConnect.db.commit()
            await ctx.send('Currency added!', delete_after=60)

async def setup(client):
    await client.add_cog(addCryp(client))