#급식 기능
from discord.ext.commands import bot
from discord.ext import commands
import discord
import neispy
import time
import json

neiskey = "e1fa7c85eafc46098f79c372457fa0b7"
with open('./data/chats.json', "r", encoding='UTF-8') as json_file:
    responses = json.load(json_file)

neis = neispy.Client(neiskey)
dates = time.strftime(f'%Y%m%d', time.localtime(time.time()))

locallist = {
'서울': 'B10', 
'부산': 'C10', 
'대구': 'D10',
'인천': 'E10', 
'광주': 'F10', 
'대전': 'G10', 
'울산': 'H10',
'세종': 'I10', 
'경기': 'J10', 
'강원': 'K10', 
'충북': 'M10', 
'충남': 'N10', 
'전북': 'P10', 
'전남': 'Q10', 
'경북': 'R10', 
'경남': 'S10', 
'제주': 'T10'}

rquirereply = {}

class Schlmeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @commands.command(name="급식", aliases=responses["Commands"][0]["Meals"])
    async def listener(self, localname, schoolname):
        localcode = locallist[localname]
        scinfo = await neis.schoolInfo(ATPT_OFCDC_SC_CODE=localcode, SCHUL_NM=schoolname)
        AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
        SE = scinfo[0].SD_SCHUL_CODE  # 학교코드
        return AE
        return SE

    async def meal(self, ctx, AE, SE, localname, schoolname):
        try:            
            scmeal = await neis.mealServiceDietInfo(AE, SE, MLSV_YMD=dates)
            meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")
            await ctx.send(f"지명 : ``{localname}``\t교명 : ``{schoolname}``\n날짜 : ``{dates}``\n메뉴 :\n``{meal}``")
        except:
            await ctx.send(f"날짜 : ``{dates}``\n오늘은 급식 없어 급식충새끼야")
    

def setup(bot):
    bot.add_cog(Schlmeal(bot))
