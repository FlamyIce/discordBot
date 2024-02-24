import discord
import asyncio
from discord.ext import commands
import dbConnect

class joinToCreate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener('on_ready')
    async def joinToCreate(self):
        while True:
            try:
                dbConnect.cur.execute("SELECT * FROM jtc")
                rows = dbConnect.cur.fetchall()

                for val in rows:
                    guild = self.client.get_guild(int(val[0]))
                    category = self.client.get_channel(int(val[1]))
                    channel = self.client.get_channel(int(val[2]))
                    members = channel.members
                    for member in members:
                        dbConnect.cur.execute(f"SELECT * FROM channels WHERE userID = {member.id}")
                        rows = dbConnect.cur.fetchall()
                        a = 0

                        for val in rows:
                            a = val[1]

                        membObj = guild.get_member(member.id)
                        if a == 0:
                            await guild.create_voice_channel(f'{member}', category = category)
                            getChannelName = discord.utils.get(guild.channels, name=str(member))
                            await getChannelName.set_permissions(membObj, manage_channels=True)
                            chObj = guild.get_channel(getChannelName.id)
                            await membObj.move_to(chObj)
                            dbConnect.cur.execute(f'UPDATE channels SET channelID = {getChannelName.id} WHERE userID ="{member.id}"')
                            dbConnect.db.commit()
                        else:
                            dbConnect.cur.execute(f"SELECT * FROM channels WHERE userID = {member.id}")
                            rows = dbConnect.cur.fetchall()
                            for val in rows:
                                a = val[1]
                            ch = guild.get_channel(a)
                            await membObj.move_to(ch)
            except:
                pass
            await asyncio.sleep(0.1)

async def setup(client):
    await client.add_cog(joinToCreate(client))