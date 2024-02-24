from discord.ext import commands
import discord
import datetime
import dbConnect
from easy_pil import Editor, Font, load_image_async
from discord import File, app_commands
class profile2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='profile', description='profile form')
    async def profile(self, interaction: discord.Interaction, member: discord.Member = None):
        color = discord.Colour.random()

        if not member:
            member = interaction.user

        userGuild = 'users'+str(interaction.guild_id)
        dbConnect.cur.execute(f"SELECT * FROM {userGuild} WHERE userid = '{member.id}'")
        dbConnect.db.commit()
        rows = dbConnect.cur.fetchall()
        for val in rows:
            vals = val

        curexp = str(vals[3])
        nexp = str(vals[4])
        money = str(vals[5])
        percentage = ((vals[3] / vals[4]) * 100)
        background = Editor('./assets/progBG.png').resize((600, 10))
        background.bar((0,0), max_width=600, height=30, percentage=percentage, fill=str(color))
        file = File(fp=background.image_bytes, filename='card.png')

        ms = str(member.status)
        if ms == 'idle':
            ms = 'Idle'
        elif ms == 'dnd':
            ms = 'Do not disturb'
        elif ms == 'online':
            ms = 'Online'
        else:
            ms = 'Offline'
        
        if member.guild_avatar:
            profile = member.guild_avatar.url
        else:
            profile = member.avatar.url

        embed=discord.Embed(
            color=color
            )
        embed.set_author(
            name=member.display_name+'#'+member.discriminator, 
            url="https://vk.com/oleg_fx", 
            icon_url=profile
            )
        embed.set_thumbnail(url=profile)
        embed.add_field(name="> LEVEL", value=f"```{vals[2]}```", inline=True) 
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name="> EXP", value=f"```{curexp}/{nexp}```", inline=True)

        embed.add_field(name='\u200b', value='\u200b', inline=False)

        embed.add_field(name='> MONEY', value=f'```{money}```', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='> STATUS', value=f'```{ms}```', inline=True)
        embed.set_image(url='attachment://card.png')
        # embed.set_footer(text='asd')
        embed.timestamp = datetime.datetime.now()

        await interaction.response.send_message(file=file, embed = embed, ephemeral=True)

async def setup(client):
    await client.add_cog(profile2(client))