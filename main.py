import discord
from discord.ext import commands

class Cogs:
    safe=[
        "cogs.admin",
        "cogs.other",
        "cogs.help",
        "cogs.animals",
        "cogs.meme",
        "cogs.games",
        "cogs.dbl"
    ]

Yomenai = commands.Bot(command_prefix="=")

Yomenai.remove_command("help")

for cog in Cogs.safe:
    Yomenai.load_extension(cog)

@Yomenai.event
async def on_ready():
    await Yomenai.change_presence(activity=discord.Game(name=" =help "), status=discord.Status.idle)
    print(f"Ready\nUser: {Yomenai.user}\n")

Yomenai.run("")
