import discord
from discord import message
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime, timezone, timedelta

time = timezone(timedelta(hours=+8))                                                                    #設定時間變數
class Help(Cog_Extension):
    
    commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="懶人包",                                                             #標題(社課 社團活動)
        url="https://www.facebook.com/ntucyc/",                                                         #網址
        description="hello",                                                                            #描述內容(路路線地點時間)
        color=0x00ffff,                                                                                 #顏色(網路上找之後複製即可)
        timestamp=datetime.now(time).isoformat(timespec="seconds"))                                                          #時間(不用調整)
        embed.set_author(name="Chen",                                                                   #發文者名字
        url="https://www.facebook.com/shunbao.chen.1",                                                  #發文者個人資訊連結    
        icon_url="https://imgur.com/DX5G9ru")                                                           #發文者個人圖片 or 社徽
        embed.set_thumbnail(url="")                                                                     #ICON可放社團宣傳圖之類的...
        embed.add_field(name="行事曆", value="https://www.facebook.com/ntucyc/", inline=False)          #行事曆圖片連結(要放imgur的連結)
        embed.add_field(name="社團粉專", value="https://www.facebook.com/ntucyc/", inline=False)        #社團粉專連結
        embed.add_field(name="社團", value="https://www.facebook.com/groups/NTUCYCLUB", inline=False)   #社團連結    
        embed.add_field(name="Strava", value="https://www.facebook.com/ntucyc/", inline=False)          #路線連結
        await ctx.send(embed=embed)                                                                     #inline true or false影響排版

        

def setup(bot):
    bot.add_cog(Help(bot))

