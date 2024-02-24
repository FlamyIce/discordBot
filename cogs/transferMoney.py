import discord
import dbConnect
from discord.ext import commands

class transfer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx, member: discord.Member, money):
        await ctx.message.delete()
        dbConnect.cur.execute(f'SELECT * FROM users WHERE userID = {ctx.author.id}')
        row = dbConnect.cur.fetchall()
        userMoney = 0
        for inf in row:
            userMoney = float(inf[5])

        moneyPayed = float(money) * 0.02
        moneyPayed += float(money)

        if userMoney < moneyPayed:
            await ctx.send('<@'+str(ctx.author.id)+'>' + " you't have money!", delete_after=60)
        else:
            userMoney -= moneyPayed
            dbConnect.cur.execute(f'SELECT * FROM users WHERE userID = {member.id}')
            row = dbConnect.cur.fetchall()
            recipientUserMoney = 0
            
            for inf in row:
                recipientUserMoney = float(inf[5])
            recipientUserMoney += float(money)
            print(recipientUserMoney)
            
            dbConnect.cur.execute(f'UPDATE users SET money = {userMoney} WHERE userID = {ctx.author.id}')
            dbConnect.db.commit()
            
            dbConnect.cur.execute(f'UPDATE users SET money = {recipientUserMoney} WHERE userID = {member.id}')
            dbConnect.db.commit()

            await ctx.send('<@'+str(ctx.author.id)+'>'+' sent '+ str(money)+' to '+'<@'+str(member.id)+'>')
                

async def setup(client):
    await client.add_cog(transfer(client))