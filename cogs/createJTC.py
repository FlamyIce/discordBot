import asyncio
import discord
from discord.ext import commands
from discord.utils import get
import dbConnect

class createJTC(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def createJTC(self, ctx):
        await ctx.message.delete()
        guild = self.client.get_guild(ctx.guild.id)
        await ctx.guild.create_category('Channels')
        category = discord.utils.get(guild.categories, name = 'Channels')
        await guild.create_voice_channel('Create', category = category)
        channel = discord.utils.get(ctx.guild.channels, name='Create')
        try:
            dbConnect.cur.execute("""CREATE TABLE IF NOT EXISTS jtc (
                guildID BIGINT(255) PRIMARY KEY,
                categoryID BIGINT(255),
                channelID BIGINT(255)
            )""")
            query = "INSERT INTO jtc (guildID, categoryID,channelID) VALUES (%s,%s,%s)"
            guildID = ctx.guild.id
            categoryID = category.id
            channelID = channel.id
            vals = (guildID, categoryID, channelID)
            dbConnect.cur.execute(query, vals)
            dbConnect.db.commit()
        except:
            dbConnect.cur.execute(f'UPDATE jtc SET categoryID = {category.id}, channelID = {channel.id}  WHERE guildID = {ctx.guild.id}')
            dbConnect.db.commit()
async def setup(client):
    await client.add_cog(createJTC(client))