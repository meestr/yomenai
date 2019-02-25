from discord.ext import commands
from libs import macro
import discord
import asyncio


async def get_time(a:str):
    b = {
        "s": 1,
        "m": 60,
        "h": 3200,
        "d": 86400
    }
    if a[-1] not in b: return None
    return b.get(a[-1]) * int(a[0:-1])

class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, args=None):
        try:
            await member.ban(reason=args)
            await ctx.send(
                embed=await macro.msg(
                    desc=f"**{member.name}** has been banned. :hammer:"
                )
            )
        except discord.Forbidden:
            await ctx.send(
                embed=await macro.error(
                    desc=f"I cannot ban {member.mention} :pensive:"
                )
            )
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, args=None):
        try:
            await member.kick(reason=args)
            await ctx.send(
                embed=await macro.msg(
                    desc=f"**{member.name}** has been kicked. :hammer:"
                )
            )
        except discord.Forbidden:
            await ctx.send(
                embed=await macro.error(
                    desc=f"I cannot kick {member.mention} :pensive:"
                )
            )
    @commands.command(name="mute")
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member:discord.Member, *, args=None):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if not role:
                return await ctx.send(
                    embed=await macro.error(
                        desc="There are no roles with the name of __Muted__"
                    )
                )
            await member.add_roles(role, reason=args)
            await ctx.send(
                embed=await macro.msg(
                    desc=f"{member.name} muted :hushed:"
                )
            )
        except discord.Forbidden:
            await ctx.send(
                embed=await macro.error(
                    desc="I do not have permission to do that."
                )
            )
    @commands.command(name="tempmute")
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member:discord.Member, length:str, *, args=None):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if not role:
                return await ctx.send(
                    embed=await macro.error(
                        desc="There are no roles with the name of __Muted__"
                    )
                )
            await member.add_roles(role, reason=args)
            await ctx.send(
                embed=await macro.msg(
                    desc=f"{member.mention} was muted for {length} :hushed:"
                )
            )
            await asyncio.sleep(await get_time(length))
            await member.remove_roles(role)
        except discord.Forbidden:
            await ctx.send(
                embed=await macro.error(
                    desc="I do not have permission to do that."
                )
            )
    @commands.command(nmae="info")
    async def info(self, ctx, member:discord.Member=None):
        if not member:
            embed = discord.Embed(color=discord.Color.purple())
            embed.set_image(url=ctx.author.avatar_url.replace("size=1024", "size=512"))
            embed.add_field(name="Name:", value=ctx.author.mention, inline=False)
            embed.add_field(name="Joined at:", value=ctx.author.joined_at, inline=False)
            embed.add_field(name="Account created:", value=ctx.author.created_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Color.purple())
            embed.set_image(url=member.avatar_url.replace("size=1024", "size=512"))
            embed.add_field(name="Name:", value=member.mention, inline=False)
            embed.add_field(name="Joined at:", value=member.joined_at, inline=False)
            embed.add_field(name="Account created:", value=member.created_at, inline=False)
            await ctx.send(embed=embed)
    @commands.command(name="ticket")
    @commands.has_permissions(manage_channels=True)
    async def ticket(self, ctx, length):
        for channel in ctx.guild.channels:
            if channel.name == f"{ctx.message.author.name}-ticket":
                return await ctx.send(
                    embed=await macro.msg(
                        desc="You have already created a ticket."
                    )
                )
        a = await get_time(length)
        channel = await ctx.guild.create_text_channel(name=f"{ctx.message.author.name}-ticket")
        await ctx.send(
            embed=await macro.msg(
                desc=f"A ticket with the name of **{channel.mention}** has been created for {length}. "
            )
        )
        await asyncio.sleep(await get_time(length))
        await channel.delete()
    @commands.command(name="warn")
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.Member, *, args):
        await ctx.send(
            embed=await macro.msg(
                desc=f"**{member.mention}** has been warned for **{args}**"
            )
        )
    @commands.command(name="purge")
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx,  limit:int=100,channel:discord.TextChannel=None, ):
        if not channel:
            channel = ctx.message.channel
        if limit > 100:
            return await ctx.send(
                embed=await macro.msg(
                    desc=f"Amount of messages too high! Please set it to lower than or equal to 100."
                )
            )
        await channel.purge(limit=limit)
        m = await ctx.send(
            embed=await macro.msg(
                desc=f"{limit} messages purged in {channel.mention}. :white_check_mark:"
            )
        )
        await asyncio.sleep(5)
        await m.delete()

def setup(bot:commands.Bot):
    bot.add_cog(Admin(bot=bot))
