import discord
from discord import message
from discord.ext import commands
from core.classes import Cog_Extension

class Sayd(Cog_Extension):

    @commands.command()
    async def sayd(self, ctx, msg):
            await ctx.message.delete()
            msg=message
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(Sayd(bot))