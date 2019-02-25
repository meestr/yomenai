from discord.ext import commands
import discord
import aiohttp
from libs import macro
from asyncio import sleep
from datetime import datetime

class Games(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.command(name='apex')
    async def apex(self, ctx, username:str, platform:str):
        platform = platform.lower()
        try:
            async with aiohttp.ClientSession(headers={'TRN-Api-Key': '7576ed9c-80b2-416f-82f4-5c88d06ad76d'}) as cs:
                platform = {"xbl": '1', 'psn': "2", "pc": "5"}.get(platform)
                async with cs.get(f"https://public-api.tracker.gg/apex/v1/standard/profile/{platform}/{username}") as r:
                    re = await r.json()
                    plat = platform
                    platform = {'5':'PC/ORIGIN','1':'XBOX LIVE','2':'PLAYSTATION NETWORK'}.get(plat)
                    if platform == "PLAYSTATION NETWORK":
                        a = 4
                    else:
                        a = 2
                    if platform == "XBOX LIVE":
                        await ctx.send(
                            embed=await macro.img(
                                url=re['data']['children'][0]['metadata']['bgimage'],
                                desc="Note: The Apex Legends API does not completely support all information from Xbox Live\n\n" +
                                f"**Username**: {username}\n"
                                f"**Best Legend**: {re['data']['children'][0]['metadata']['legend_name']}\n"
                                f"**Level**: {re['data']['stats'][0]['displayValue']}\n"
                                f"**Kills**: {re['data']['stats'][1]['displayValue']}\n"
                            )
                        )
                    else:
                        await ctx.send(embed = await macro.img(
                            url=re['data']['children'][0]['metadata']['bgimage'],
                            desc=
                            f"**Username**: {username}\n"
                            f"**Best Legend**: {re['data']['children'][0]['metadata']['legend_name']}\n"
                            f"**Level**: {re['data']['stats'][0]['displayValue']}, (#{re['data']['stats'][0]['displayRank']})\n"
                            f"**Kills**: {re['data']['stats'][1]['displayValue']}, (#{re['data']['stats'][1]['displayRank']})\n"
                            f"**Damage**: {re['data']['stats'][a]['displayValue']}, (#{re['data']['stats'][a]['displayRank']})"))
                    print("apex called")
                    await cs.close()
        except:
            await ctx.send(embed=await macro.error(
                desc="I couldn't find that player. Try checking the spelling and platform. Remember that the name is case-sensitive."
            ))
    @commands.command(name="fortnite")
    async def fortnite(self, ctx, username:str):
        try:
            async with aiohttp.ClientSession(headers={"TRN-Api-Key": "815be3c0-3c39-4465-a031-2d35d6887c2a"}) as cs:
                async with cs.get(f"https://api.fortnitetracker.com/v1/profile/pc/{username}") as r:
                    re = await r.json()
                    await ctx.send(embed=await macro.msg(
                        desc=f"**Times in Top 3**: {re['lifeTimeStats'][1]['value']}\n"
                         f"**Score**: {re['lifeTimeStats'][6]['value']}\n"
                         f"**Matches Played**: {re['lifeTimeStats'][7]['value']}\n"
                         f"**Wins**: {re['lifeTimeStats'][8]['value']}\n"
                         f"**Win Percentage**: {re['lifeTimeStats'][9]['value']}\n"
                         f"**Kills**: {re['lifeTimeStats'][10]['value']}\n"
                         f"**K/D**: {re['lifeTimeStats'][11]['value']}\n"
                    ))
                    await cs.close()
        except:
            await ctx.send(
                embed=await macro.error(
                    desc="I couldn't find that player. Try checking the spelling, the case-sensitivity, as well as the fact that this command __only__ works with PC (At the moment) so there is no platform argument"
                )
            )
    @commands.command(name="fortnite-shop")
    async def shop(self, ctx):
        async with aiohttp.ClientSession(headers={"TRN-Api-Key": "815be3c0-3c39-4465-a031-2d35d6887c2a"}) as cs:
            async with cs.get(f"https://api.fortnitetracker.com/v1/store") as r:
                re = await r.json()
                await ctx.send(
                    embed=await macro.msg(desc=f"**Shop on {datetime.now().month}/{datetime.now().day}/{str(datetime.now().year)[2:]}**")
                )
                for i in range(0, 3):
                    await sleep(0.25)
                    await ctx.send(
                        embed=await macro.img(
                            url=re[i]['imageUrl'],
                            title=re[i]['name'] + " | " + str(re[i]['vBucks']) + " vBucks"
                        )
                    )
                await cs.close()
    #TODO: FORTNITE CHALLENGES
def setup(bot:commands.Bot):
    bot.add_cog(Games(bot=bot))

