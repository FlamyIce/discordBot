from discord.ext import commands
import discord
from discord import app_commands

class ModalTest(discord.ui.Modal, title='Registration form'):
    login = discord.ui.TextInput(
        label='Login',
        placeholder='Your login here...',
        )
    email = discord.ui.TextInput(
        label='Email',
        style=discord.TextStyle.long,
        placeholder='Your email here...',
        max_length=300,
        )
    password = discord.ui.TextInput(
        label='Password',
        placeholder='Password',
        min_length=6
    )
    passwordRepeat = discord.ui.TextInput(
        label='Repeat password',
        placeholder='Repeat password',
        min_length=6
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        if self.password.value != self.passwordRepeat.value:
            await interaction.response.send_message('Passwords are not match.', ephemeral=True)
        elif '@' not in self.email.value:
            await interaction.response.send_message('Incorrect email.', ephemeral=True)
        else:
            await interaction.response.send_message('Success.',ephemeral=True)
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test cog loaded')

class Test(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()

        await ctx.send(f'Synced {len(fmt)} commands.')

    @app_commands.command(name='test', description='test form')
    async def test(self,interaction: discord.Interaction):
        await interaction.response.send_modal(ModalTest())
    
async def setup(client):
    await client.add_cog(Test(client))