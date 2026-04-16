import logging
from pathlib import Path

import discord
from discord import Intents
from discord.ext.commands import Bot

logger = logging.getLogger("seeker")


class SeekerBot(Bot):
    def __init__(self, intents: Intents, prefix: str = "!!") -> None:
        super().__init__(command_prefix=prefix, intents=intents)
        logger.info("Starting Seeker Bot")

    async def on_ready(self) -> None:
        logger.info("Logged in as %s", self.user)
        logger.info("Servers: %d", len(self.guilds))
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name="Seeker")
        )

    async def setup_hook(self) -> None:
        for path in (Path("./seeker/bot/events"), Path("./seeker/bot/commands")):
            for cog in path.rglob("*.py"):
                # Example:
                #   -> seeker/bot/events/messages.py
                #   -> seeker.bot.events.messages
                relative = cog.with_suffix("")
                extension = ".".join(relative.parts)
                try:
                    await self.load_extension(extension)
                    logger.info("Cog loaded successfully: %s (%s)", extension, cog)
                except FileNotFoundError:
                    logger.error("couldn't find %s", cog)
                except Exception as e:
                    logger.error("Cog failed: %s (%s) -> %s", extension, cog, e)
