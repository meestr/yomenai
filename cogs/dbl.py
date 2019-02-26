import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging


class DiscordBotsOrgAPI(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.token = ''  #  set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):

        while True:
            logger.info('attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('posted server count ({})'.format(len(self.bot.guilds)))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)


def setup(bot:commands.Bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
