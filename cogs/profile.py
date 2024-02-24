import discord
from discord.ext import commands
from easy_pil import Editor, Font, load_image_async
from discord import File
import dbConnect
from discord import app_commands

class profile(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @app_commands.command(name='profile2', description='profile2 form')
    async def profile2(self, interaction: discord.Interaction, member: discord.Member = None):
        if not member:
            member = interaction.user
        aName = member.name+'#'+member.discriminator
        userGuild = 'users'+str(interaction.guild_id)

        ms = str(member.status)
        if ms == 'idle':
            ms = 'Idle'
        elif ms == 'dnd':
            ms = 'Do not disturb'
        elif ms == 'online':
            ms = 'Online'
        else:
            ms = 'Offline'

        background = Editor('./assets/card_1.jpg').resize((900, 300))

        poppins = Font(path='./assets/blood.ttf').poppins(size=35)
        poppins2 = Font(path='./assets/blood.ttf').poppins(size=30)

        if member.guild_avatar:
            profileIMG = await load_image_async(str(member.guild_avatar.url))
        else:
            profileIMG = await load_image_async(str(member.avatar.url))

        profileIMG = Editor(profileIMG).resize((150,150)).circle_image()

        background.paste(profileIMG.image, (30,30))
        background.rectangle((30,220), width=600, height=30, fill='#C0B6CC', radius=20)
        background.text((200, 30), aName, font = poppins, color="white")
        background.rectangle((200,70), width=300, height=1, fill='#8D3EEA')

        file = File(fp=background.image_bytes, filename='card.png')
        await interaction.response.send_message(file=file, ephemeral=True)

async def setup(client):
    await client.add_cog(profile(client))