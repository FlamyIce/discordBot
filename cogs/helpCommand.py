from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    prefix = '$'
    userCommands = ['**send** - **Example:** `'+prefix+'send @<unknown>#6969`. To transfer money, it have comission 2%', 
                    '**profile** - **Example:** `'+prefix+'profile | $profile @<unknown>#6969`. Shows your or user guild profile', 
                    '**price** - **Example:** `'+prefix+'price btcusdt | $price bnbusdt`. Shows cryptocurrency price', 
                    '**userStatus** - **Example:** `'+prefix+'userStatus @<unknown>#6969`. Shows user status',
                    '**buyRole** - **Example:** `'+prefix+'buyRole roleName 150 20 250`. To buy role, write `role name` + `red`, `green`, `blue` colors',
                    '**adminHelp** - **Example:** `'+prefix+'adminHelp` only for admins/moders'
                    ]
    adminCommands = ['**ready** - **Example:** `'+prefix+'ready`. To start bot on your server.', 
                     '**createJTC** - **Example:** `'+prefix+'createJTC`. To create join to create channel & category.', 
                     '**runningRow** - **Expample:** `'+prefix+'runningRow @<unknown>6969 something`. To do running nickname', 
                     '**mute** - **Example:** `'+prefix+'mute @<unknown>#6969`.', 
                     '**unmute** - **Example:** `'+prefix+'unmute @<unknown#6969>`.', 
                     '**ban** - **Example:** `'+prefix+'ban @<unknown#6969>`.', 
                     '**kick** - **Example:** `'+prefix+'kick @<unknown#6969>`.', 
                     '**differentName** - **Example:** `'+prefix+'differentName @<unknown#6969> first second third`. User nickname will be changed all time', 
                     '**addCryp** - **Example:** `'+prefix+'addCryp btcusdt`. To add cryptowallet in embed.', 
                     '**addAll** - **Example:** `'+prefix+'addAll`. To add all users in database.'
                     ]

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(
            color=discord.Colour.brand_green(),
            )
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='__**User commands**__', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)

        for i in help.userCommands:
            i = i.split('-')
            embed.add_field(name='> $'+i[0].strip() ,value=i[1].strip(), inline=False)
        embed.set_image(url='https://media1.tenor.com/images/e363c4e0d4cc716ad935f94ebf328ac8/tenor.gif?itemid=17241893')
        await ctx.send(embed = embed, delete_after=120)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def adminHelp(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(
            color=discord.Colour.brand_red(),
            )
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='__**User commands**__', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)

        for i in help.userCommands:
            i = i.split('-')
            embed.add_field(name='> $'+i[0].strip() ,value=i[1].strip(), inline=False)

        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='__**Admin commands**__', value='\u200b', inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)

        for i in help.adminCommands:
            i = i.split('-')
            embed.add_field(name='> $'+i[0].strip() ,value=i[1].strip(), inline=False)
        embed.set_image(url='https://media1.tenor.com/images/e363c4e0d4cc716ad935f94ebf328ac8/tenor.gif?itemid=17241893')
        await ctx.send(embed = embed,delete_after=120)
async def setup(client):
    await client.add_cog(help(client))