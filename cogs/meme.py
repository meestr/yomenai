from libs import macro
from discord.ext import commands
import discord
import aiohttp

class MemeMaker(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name="make-meme")
    async def meme(self, ctx, id, *args):
        async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
            "template_id": id,
            "username": "meestr",
            "password": "yugignuf",
            "text0": args[0],
            "text1": args[1]
        },) as response:
            res = await response.json()
            url = res["data"]["url"]
            await ctx.send(
                embed=await macro.img(url=url)
            )
            await response.close()
def setup(bot:commands.Bot):
    bot.add_cog(MemeMaker(bot))