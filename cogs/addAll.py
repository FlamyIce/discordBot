from discord.ext import commands
import dbConnect

class addAll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addAll(self, ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            userid = user.id
            username = user.name+ '#' + user.discriminator
            usersTable = 'users'+str(user.guild.id)
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
                insc = 'INSERT INTO channels (userID,channelID) VALUES (%s,%s)'
                channelID = 0
                vals__ = (userid, channelID)
                dbConnect.cur.execute(insc, vals__)
                dbConnect.db.commit()
            except:
                pass


async def setup(client):
    await client.add_cog(addAll(client))