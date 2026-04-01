import asyncio
import sys

from discord.errors import LoginFailure

from seeker.bot.seeker_bot import SeekerBot
from seeker.config import DEFAULT_PREFIX, DISCORD_TOKEN
from seeker.log import seeker_logger as logger


async def main():
    if not DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN not defined.")

    bot = SeekerBot(DEFAULT_PREFIX)

    try:
        await bot.start(DISCORD_TOKEN)
    except LoginFailure:
        logger.critical("Invalid Discord token provided. Please check your .env.")
        sys.exit(1)
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
