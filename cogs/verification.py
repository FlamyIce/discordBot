from discord.ext import commands
import discord
from discord.ui import Select, View

class verification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def verification(self, ctx):
        embed = discord.Embed(title="Pass the user verification!", description="It gives u access to other channels.")
        select = Select(
            placeholder="Open menu",
            options=[
                    discord.SelectOption(label="Verify your account", value="1", description="Click to get '✅' role")
                    # discord.SelectOption(label="Second", value="2", description="Second"),
                    # discord.SelectOption(label="Third", value="3", description="Third")
                ]
            )
        async def callback(interaction):
            if select.values[0] == "1":
                guild = interaction.guild
                getRole = guild.get_role(1035935785582600263)
                getMember = guild.get_member(interaction.user.id)
                await getMember.add_roles(getRole)
                await interaction.response.send_message(" ")

        select.callback = callback
        view = View()
        view.add_item(select)
        await ctx.send(embed=embed, view=view)

async def setup(client):
    await client.add_cog(verification(client))