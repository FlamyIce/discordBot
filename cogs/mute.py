import discord
from discord.ext import commands

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: discord.Member):
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        guild = ctx.guild
        if role not in guild.roles:
            permissions = discord. Permissions()
            permissions.update(speak=False, send_messages=False)
            roleM = await guild.create_role(name='Muted', permissions=permissions)
            await member.add_roles(roleM)
            await ctx.send(f'{member} has been muted!')
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.set_permissions(role, send_messages=False)
                elif isinstance(channel, discord.VoiceChannel):
                    await channel.set_permissions(role, speak=False)
        else:
            await member.add_roles(role)
            await ctx.send(f'{member} has been muted!')
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.set_permissions(role, send_messages=False)
                elif isinstance(channel, discord.VoiceChannel):
                    await channel.set_permissions(role, speak=False)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: discord.Member):
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        try:
            await member.remove_roles(role)
            await ctx.send(f'{member} has been unmuted!', delete_after=60)
        except:
            pass

async def setup(client):
    await client.add_cog(mute(client))