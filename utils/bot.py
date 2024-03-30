import discord
from utils import logger

log = logger.Logger.bot_logger


class Bot(discord.AutoShardedBot):
    async def on_ready(self):
        log.info(f"Logged in successfully as {self.user} with ID {self.user.id}")
