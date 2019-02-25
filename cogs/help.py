from discord.ext import commands
from libs import macro


def get_help():
    return "**__Mod Commands__**\n" \
               "ban: Bans a member\n" \
               "kick: Kicks a member\n" \
                "purge: Purges a channel of messages(defaults to 100 messages, can mention channel)\n" \
                "warn: Warns a member(Doesn't really do anything but mention them, modlogs are WIP)\n" \
               "mute: Permanently mutes a member\n" \
               "tempmute: Temporarily mutes a member(e.g =tempmute @member 1s)\n" \
                "poll: Creates a poll(Use quotation marks for using more than one word in a topic)\n" \
                "ticket: Creates a temporary channel with the length given (e.g =ticket 10m)\n" \
               "__**Other/Fun**__\n" \
           "say: Makes the bot say something\n" \
           "cat: Gets a picture of a cat\n"\
               "dog: Gets a picture of a dog\n" \
           "bird: Gets a picture of a bird\n" \
           "color: Gets a color using the given parameters: [r] [g] [b] Params must be from 0 to 255\n" \
           "random-color: Gets a random color\n" \
           "" \
               "roll: Rolls a dice from 1 to 6 on default\n" \
               "8ball: Shakes an 8ball\n" \
               "flip: Flips a coin\n" \
                "info: Gets info about a user. (Defaults to author, can mention)\n" \
               "google: Searches Google for URL\n" \
               "urban: Searches UrbanDictionary\n" \
               "randomurban: Gets a random definition from urban dictionary\n" \
               "invite: Sends an invite to the target user\n" \
               "character: Creates a random character(alignment, age, skin-tone, morality)\n" \
               "binary: Converts the given words to binary\n" \
               "meme-template: Gets a meme template from imgflip.com\n" \
           "__make-meme__: Makes a meme. Usage: ``=make-meme [id] [text1(in quotations)] [text2(also in quotations)]`` You can get a list of IDs from https://api.imgflip.com/popular_meme_ids\n" \
           "__Game Stats__\n" \
           "apex: Usage: ``=apex ['username'] [platform]``. Please note that username is case-sensitive. Valid platforms: xbl, psn, pc\n" \
           "fortnite: Usage: ``=fortnite ['username']`` Please note that this command only lists those who play PC\n" \
           "fortnite-shop: Gets the third-most items of the current Fortnite shop\n\n" \
            "vote: Gets the link to vote for me! (please do :c)"


class Help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
            await ctx.send(
                    embed=await macro.msg(
                    desc=get_help()
                 )
                )

def setup(bot:commands.Bot):
    bot.add_cog(Help(bot=bot))
