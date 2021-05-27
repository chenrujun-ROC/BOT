import discord
from discord.ext import commands
import json
import os

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['一般_channel']))
    await channel.send(f'{member}Join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['一般_channel']))
    await channel.send(f'{member}Leave!') 

@commands.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} dene.')

@commands.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} dene.')

@commands.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'RE-Loaded {extension} dene.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])