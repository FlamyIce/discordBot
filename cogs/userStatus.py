import discord
from discord.ext import commands

class userStatus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userStatus(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.message.delete()
        print(member.status)
        ms = str(member.status)
        if ms == 'idle':
            ms = 'Отошел'
        elif ms == 'dnd':
            ms = 'Не беспокоить'
        elif ms == 'online':
            ms = 'Онлайн'
        else:
            ms = 'Оффлайн'
        await ctx.send(str(member.name)+" "+str(ms), delete_after=60)

async def setup(client):
    await client.add_cog(userStatus(client))