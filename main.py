import discord, sys, os, datetime
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix = '!', description = "Bot for the UMD Entrepreneur Server")
yearRoles = ['2021', '2022', '2023', '2024']
majorRoles = ['CMSC', 'ENAE', 'ENEE', 'MATH', 'PHYS', 'BMGT', 'ENME', 'LTSC', 'BSCI', 'INST', 'PSYC', 'GVPT', 'BIOE']

def canPurge(m):
    return not (m.author.bot and "purged by" in m.content)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')


@bot.command(description = 'Shuts down the bot. Only usable by admin.')
async def shutdown(ctx):
    sys.exit()


@bot.command(desciption = 'For adding your graduation year.')
async def year(ctx, year: str):
    if year in yearRoles:
        member = ctx.message.author
        role = get(member.guild.roles, name = year)
        await member.add_roles(role)
        await ctx.send(ctx.message.author.mention + ": Added role " + year)
    else:
        await ctx.send("Role " + year + " does not exist.")


@bot.command(desciption = 'For adding your major.')
async def major(ctx, major: str):
    if major in majorRoles:
        member = ctx.message.author
        role = get(member.guild.roles, name = major)
        await member.add_roles(role)
        await ctx.send(ctx.message.author.mention + ": Added role " + major)
    else:
        await ctx.send("Role " + major + " does not exist.")


@bot.command(description = 'Wipes a channel of its messages.')
async def purge(ctx, l: int):
    member = ctx.message.author
    if get(ctx.guild.roles, name = 'Admin') in member.roles:
        if l == 0:
            deleted = await ctx.message.channel.purge(limit = 99999999, check = canPurge)
            await ctx.send("Channel purged by " + ctx.message.author.mention + " at " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        else:
            deleted = await ctx.message.channel.purge(limit = l, check = canPurge)
            await ctx.send(str(len(deleted)) + " messages purged by " + ctx.message.author.mention + " at " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    else:
        await ctx.send("Sorry, only administrators can use this command.")


bot.run('NzUzMjg1NzY2NDEwNDAzODUx.X1j-Cg.E46AzygkeFz09pWRPD_QQ3sxxyQ')
