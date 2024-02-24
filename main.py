import discord
from discord.ext import commands
import os
import asyncio
from bs4 import BeautifulSoup
import requests
import asyncio
import dbConnect

client = commands.Bot(intents=discord.Intents.all(), command_prefix='$', activity=discord.Game(name='$help'), application_id='1022929963235692545')
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Bot {client.user} was logged in!')
    ch_id = 1025910068207689838
    msg_id = 1025910508886433874
    while True:
        #Delete empty channels ----------------------------------
        dbConnect.cur.execute("SELECT * FROM channels")
        rows = dbConnect.cur.fetchall()
        dbConnect.db.commit()
        for val in rows:
            a = val[1]
            try:
                getChannel = client.get_channel(a)
                memb = getChannel.members
                if len(memb) == 0:
                    await getChannel.delete()
                    dbConnect.cur.execute(f'UPDATE channels SET channelID = 0 WHERE channelID ="{a}"')
                    dbConnect.db.commit()
            except:
                pass
        #Parse Binance futures-------------------------------------------------------
        embed2=discord.Embed(
            title="Crypto", 
            url="https://vk.com/oleg_fx", 
            color=discord.Colour.random()
        )
        dbConnect.cur.execute(f"SELECT * FROM cryptocurrency")
        dbConnect.db.commit()
        rows = dbConnect.cur.fetchall()

        priceList = []
        pr = 0
        for val in rows:
            val = 'https://www.binance.com/ru/futures/'+val[1]
            a = val.split('/')
            a = a[5]
            reqsCryp = requests.get(val)
            soupCryp = BeautifulSoup(reqsCryp.text, 'html.parser')
            for title in soupCryp.find_all('title'):
                crypT = title.get_text()
                price = crypT.split('|')
                if a in price[1]:
                    price = float(price[0])
                    test = crypT.split('|')
                    priceList.append([float(test[0]),a])
                    priceList.sort(reverse=True)
                else:
                    pass
        for t in priceList:
            if pr >= len(rows):
                pr = 0
            embed2.add_field(name="> **"+str(priceList[pr][1])+"**", value='**```'+str(priceList[pr][0])+'```**', inline=True)
            pr+=1

        channel = client.get_channel(ch_id)
        msg = await channel.fetch_message(msg_id)
        try:
            await msg.edit(embed = embed2)
        except:
            pass
        await asyncio.sleep(4)

@client.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, command does not exists.**', color=0x0c0c0c), delete_after=60)


@client.event
async def main():
    async with client:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f"cogs.{filename[:-3]}")
        takeToken = open('TOKEN', 'r')
        token = ''
        for a in takeToken:
            token = a
        await client.start(token)

asyncio.run(main())