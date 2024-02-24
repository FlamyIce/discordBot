from discord.ext import commands
import dbConnect

class on_member_join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener('on_member_join')
    async def on_member_join(self, ctx):
        print(ctx.id)
        userid = ctx.id
        username = ctx.name+ '#' + ctx.discriminator
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

    # @commands.Cog.listener('on_member_remove')
    # async def on_member_remove(self, member):
    #     print(member.id)

async def setup(client):
    await client.add_cog(on_member_join(client))