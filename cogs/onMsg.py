from discord.ext import commands
import dbConnect

class onMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener("on_message")
    async def onMsg(self, ctx):
        userid = ctx.author.id
        username = ctx.author.name+ '#' + ctx.author.discriminator
        usersTable = 'users'+str(ctx.guild.id)
        try:
            insu = f'INSERT INTO {usersTable} (userid,username,level,currentXP,needXP,money) VALUES (%s,%s,%s,%s,%s,%s)'
            level = 1
            currentXP = 0
            needXP = 200
            money = 0
            vals_ = (userid,username,level,currentXP,needXP,money)
            dbConnect.cur.execute(insu, vals_)
            dbConnect.db.commit()
        except:
            pass
        try:
            insc = 'INSERT INTO channels (userID,channel,channelID) VALUES (%s,%s)'
            channelID = 0
            vals__ = (userid, channelID)
            dbConnect.cur.execute(insc, vals__)
            dbConnect.db.commit()
        except:
            pass
        
        dbConnect.cur.execute(f"SELECT * FROM {usersTable} WHERE userid = {ctx.author.id}")
        rows = dbConnect.cur.fetchall()
        for val in rows:
            vals = val
        print(vals)
        exp = int(vals[3]) + 20
        dbConnect.cur.execute(f'UPDATE {usersTable} SET currentXP = "{exp}" WHERE userid ="{userid}"')
        dbConnect.db.commit()
        if vals[3] >= vals[4]:
            dbConnect.cur.execute(f'UPDATE {usersTable} SET level = {vals[2]+1},needXP = {vals[4]+100}, currentXP = {0}, money = {vals[5]+5} WHERE userid ="{userid}"')
            dbConnect.db.commit()
        if vals[1] != username:
            dbConnect.cur.execute(f'UPDATE {usersTable} SET username = "{username}" WHERE userid = "{userid}"')

async def setup(client):
    await client.add_cog(onMsg(client))