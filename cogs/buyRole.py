import discord
from discord.ext import commands
from discord.utils import get
import dbConnect

class buyRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def buyRole(self, ctx, name, red,green,blue):
        await ctx.message.delete()
        guild = ctx.guild
        usersDB = 'users'+str(ctx.guild.id)
        dbConnect.cur.execute(f"SELECT * FROM {usersDB} WHERE userid = {ctx.author.id}")
        rows = dbConnect.cur.fetchall()
        dbConnect.db.commit()
        money = 0
        for val in rows: 
            money = val[5]
        if money < 100:
            await ctx.send('<@'+str(ctx.author.id)+'>' + " You don't have money!", delete_after=60)
        else:
            color = discord.Color.from_rgb(int(red), int(green), int(blue))
            role = await guild.create_role(name = name, color=int(color),hoist=True)
            getRole = guild.get_role(role.id)
            getMember = guild.get_member(ctx.author.id)
            await getMember.add_roles(getRole)
            money -= 100
            dbConnect.cur.execute(f"UPDATE {usersDB}  SET money = {money} WHERE userid = {ctx.author.id}")
            dbConnect.db.commit()
            await ctx.send('You got new role!', delete_after=60)

async def setup(client):
    await client.add_cog(buyRole(client))