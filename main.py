import discord
from discord.ext import commands
from classes import Cog_Extension 

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    
    @commands.command()
    async def hi(self, ctx):
        await ctx.send('ABCD')
    

def setup(bot):
    bot.add_cog(Main(bot))




   