import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from decouple import config

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ['k+', 'K+'], case_insensitive=True, help_command=None, intents=intents)
status = cycle(['Hacking To The Gate', 'Its not Tina'])

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online,  activity=discord.Game('Hacking To The Gate'))
    print("bot is ready")

# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please pass the required arguments.')
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('Invalid command twat')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Public Welcome
# @client.event
# async def on_member_join(member):
#     guild = client.get_guild()
#     channel = client.get_channel()

#     e = discord.Embed(title='', color=0xFF0055)
#     e.add_field(name='WELL CUM', value=f'Welcome to the server {member.mention}')
#     e.set_image(url='https://media.tenor.com/images/ce68656c54f859c5786d62ff93bc8ebf/tenor.gif')
#     await channel.send(embed=e)

client.run('ODA0Mjk0ODIxOTI1MDkzNDA3.YBKP7A.n0zFVpBZh2LeStNEfQU9a0_faYs')
