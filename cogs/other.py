from libs import macro
from discord.ext import commands
import discord
import random
import aiohttp
from asyncurban import UrbanDictionary
import asyncio
import googlesearch

def foo(a:str): return float(a)

class Other(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.command(name="say")
    async def say(self, ctx, *, args):
        await ctx.message.delete()
        await ctx.send(args)

    @commands.command(name="8ball")
    async def eightball(self, ctx):
        await ctx.send(
            embed=await macro.msg(
                desc=f":8ball: The 8 ball says...\n``{random.choice(['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'])}``"
            )
        )
    @commands.command(name="kill")
    async def kill(self, ctx, member:discord.Member):
        await ctx.send(
            embed=await macro.msg(
                desc=f"{ctx.message.author.mention} has killed {member.mention}! :scream:"
            )
        )
    @commands.command(name="roulette")
    async def roulette(self, ctx):
        if random.randint(1,4) == 1:
            await ctx.send(
                embed=await macro.msg(
                    desc=f"{ctx.message.author.mention} pulled the trigger and... died! :skull:"
                )
            )
        else:
            await ctx.send(
                embed=await macro.msg(
                    desc=f"{ctx.message.author.mention} pulled the trigger and... lived! :angel:"
                )
            )
    @commands.command(name="meme-template")
    async def meme_template(self, ctx):
        async with aiohttp.ClientSession() as cl:
            async with cl.get("https://api.imgflip.com/get_memes") as load:
                res = await load.json()
                await ctx.send(
                    embed=await macro.img(
                        url=random.choice(res['data']['memes']).get("url")
                    )
                )
                await cl.close()
    @commands.command(name="urban")
    async def urban(self, ctx, *, args):
        if ctx.channel.is_nsfw():
            try:
                ud = UrbanDictionary()
                word = await ud.get_word(args)
                await ctx.send(
                embed=await macro.msg(
                    f"**{word}**\n```{word.definition}```"
                )
                )
            except:
                await ctx.send(
                    embed=await macro.msg(
                    desc=f"Could not find any word under ``{args}``"
                )
            )
        else:
            await ctx.send(
            embed=await macro.error(
                desc="Command must be used in an NSFW channel"
            )
        )
    @commands.command(name="binary")
    async def binary(self, ctx, *, args):
        await ctx.send(
            embed=await macro.msg(
                desc="".join(str(bin(ord(letter))).replace("b", "") + " " for letter in args)
            )
        )
    @commands.command(name="randomurban")
    async def randurban(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send(
                embed=await macro.error(
                    desc="Command must be used in an NSFW channel"
                )
            )
        else:
            ud = UrbanDictionary()
            word = await ud.get_random()
            await ctx.send(
                embed=await macro.msg(
                    desc=f"**{word}**\n```{word.definition}```"
                )
            )
    @commands.command(name="google")
    async def google(self, ctx, *, args):
        if not ctx.channel.is_nsfw:
            return await ctx.send(
                embed=await macro.error(
                    desc="Command must be used in an NSFW channel"
                )
            )
        else:
            for url in googlesearch.search(args, stop=1):
                await ctx.send(url)
                break
    @commands.command(name="roll")
    async def dice(self, ctx, max_value:int=None):
        if not max_value: max_value = 6
        await ctx.send(
            embed=await macro.msg(
                desc=f":game_die: On a dice from 1 to {max_value}, you rolled a {random.randint(1,max_value)}"
            )
        )
    @commands.command(name="flip")
    async def flip(self, ctx):
        await ctx.send(
            embed=await macro.msg(
                desc=f"You flipped a coin, and it returned {random.choice(['tails', 'heads'])}!"
            )
        )
    @commands.command(name="color")
    async def color(self, ctx, *args):
        for item in args:
            if int(item) > 255 or int(item) < 0:
                return
        await ctx.send(
            embed=await macro.img(
                desc=f"**RGB**: {args[0]} {args[1]} {args[2]}\n**HEX**: {'#%02x%02x%02x' % (args[0],args[1],args[2])}",
                url=f"https://ice-creme.de/randcolor/?r={args[0]}&g={args[1]}&b={args[2]}"
            )
        )
    @commands.command(name="randomcolor")
    async def randomcolor(self, ctx):
        r = random.randint(1,255);g = random.randint(1,255);b = random.randint(1,255)
        await ctx.send(
            embed=await macro.img(
                desc=f"**RGB**: {r} {g} {b}\n**HEX**: {'#%02x%02x%02x' % (r,g,b)}",
                url=f"https://ice-creme.de/randcolor/?r={r}&g={g}&b={b}"
            )
        )
    @commands.command(name="character")
    async def character(self, ctx):
        await ctx.send(
            embed=await macro.msg(
                desc=f"**Age**: {random.randint(16,60)}\n"
                     f"**Alignment**: {random.choice(['Chaotic Good', 'Lawful Good', 'Neutral Good','Good Neutral', 'True Neutral', 'Chaotic Neutral', 'Chaotic Evil', 'Lawful Evil', 'Neutral Evil'])}\n"
                     f"**Color Scheme**: {random.choice(['blue', 'black', 'gray', 'red', 'navy'])} and {random.choice(['yellow', 'green', 'white', 'orange', 'brown'])}\n"
                     f"**Skin Tone**: {random.choice('Light Dark Mixed'.split())}\n"
                     f"**Body Size**: {random.choice(['average', 'small', 'large']).title()}\n"
                     f"**Race**: {random.choice(['human','human','human','human','human','human','human','human','human','human','dwarf','elf','angel/demon'])}\n"
                     f"**Hairstyle & Color**: {random.choice(['long', 'moderate', 'short'])} length and {random.choice(['white', 'brunette', 'blond', 'grey', 'jet-black','dyed'])}"
            )
        )
    @commands.command(name="poll")
    @commands.has_permissions(kick_members=True)
    async def poll(self, ctx, *args):
        emojis = ["\U0001f34e", "\U0001f352", "\U0001f34d", "\U0001f34a", "\U0001f349", "\U0001f347", "\U0001f34b"]
        used = []
        b = ""
        if len(args) > 7: return await ctx.send(
            embed=await macro.error(desc="Sorry, but you can only have 7 options")
        )
        for item in args:
            a = random.choice(emojis)
            used.append(a)
            emojis.pop(emojis.index(a))
        for i in range(0, len(args)):
            b += f"{used[i]}: {args[i]}\n"
        msg = await ctx.send(
            embed=await macro.msg(
                desc=b,
                title=f"{ctx.message.author}'s poll"
            )
        )
        for emoji in used:
            await msg.add_reaction(emoji)
            #TODO: ADD MORE EMOJIS
    @commands.command(name="vote")
    async def vote(self, ctx):
        await ctx.send(
            embed=await macro.msg(
                desc="Please vote for me here!\nhttps://discordbots.org/bot/503962394129596426/vote"
            )
        )
    @commands.command(name="invite")
    async def invite(self, ctx, member:discord.Member=None):
        if not member:
            member = ctx.message.author
        await member.send(
            embed=await macro.msg(
                desc="https://discordapp.com/oauth2/authorize?client_id=503962394129596426&permissions=8&scope=bot"
            )
        )
    @commands.command(name='fact')
    async def fact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://nekos.life/api/v2/fact") as r:
                re = await r.json()
                await ctx.send(
                    embed=await macro.msg(
                        desc=re.get("fact")
                    )
                )
                await cs.close()

def setup(bot:commands.Bot):
    bot.add_cog(Other(bot=bot))
