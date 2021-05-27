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

@commands.command()
async def load(ctx, Extension):
    bot.load_extension(f'cmds.{Extension}')
    await ctx.send(f'Loaded {Extension} done.')

@commands.command()
async def unload(ctx, Extension):
    bot.unload_extension(f'cmds.{Extension}')
    await ctx.send(f'Un-Loaded {Extension} done.')

@commands.command()
async def reload(ctx, Extension):
    bot.reload_extension(f'cmds.{Extension}')
    await ctx.send(f'RE-Loaded {Extension} done.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])