import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['一般_channel']))
        await channel.send(f'{member}Join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['一般_channel']))
        await channel.send(f'{member}Leave!') 

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = [jdata["keyword"]]
        if msg.content.endwish =='keyword' and msg.author != self.bot.user:
            await msg.channel.send('hi')
def setup(bot):
    bot.add_cog(Event(bot))