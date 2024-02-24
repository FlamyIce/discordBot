from discord.ext import commands
import dbConnect

class ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def ready(self, ctx):
        await ctx.message.delete()
        guild = 'users'+str(ctx.guild.id)
        print(guild)
        dbConnect.cur.execute(f"""CREATE TABLE IF NOT EXISTS {guild} (
            userid BIGINT(255) PRIMARY KEY,
            username TEXT,
            level BIGINT(255),
            currentXP BIGINT(255),
            needXP BIGINT(255),
            money BIGINT(255)
        )""")

        dbConnect.cur.execute(f"""CREATE TABLE IF NOT EXISTS cryptocurrency (
            id BIGINT(255) PRIMARY KEY NOT NULL AUTO_INCREMENT,
            crname TEXT
        )""")

        dbConnect.cur.execute("""CREATE TABLE IF NOT EXISTS channels (
            userID BIGINT PRIMARY KEY,
            channelID BIGINT
        )""")

async def setup(client):
    await client.add_cog(ready(client))