import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready. ')


@client.command(aliases=['test', 'rate'])
async def ping(ctx, *, member: discord.Member):
    Responses = ['sucks', 
                'Is aswesome', 
                'Is Fat',
                'Is strong',
                'Is smart',
                'Sucks to the Core!',
                'Is Amazing',
                'Is Brilliant',
                'Is a Loser',
                'Is a Low life',
                'Is Really..Really Dumb!',
                'Is Nothing',
                'Is The Champ']
    #Responses = ['1', '2']
    #lst = [team]
    #await ctx.send(f'Crewmate : {team}\nYou are in team: {random.choice(Responses)}')
    #await ctx.send(f'list : {lst}')
    await ctx.send(f'{member.name} {random.choice(Responses)}')

@client.command(aliases=['nasu'])
async def funny_Gif(ctx):
    await ctx.send('https://imgur.com/TtJnIrq')



client.run('Nzc4ODQwODkxMjIxNzM3NTI0.X7X2Gg.FBTLhJ9QYgA4aF00sRdS2UXl-Xk')
