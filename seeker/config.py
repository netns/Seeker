import os
from enum import StrEnum

import discord
from dotenv import load_dotenv

load_dotenv()


class Environment(StrEnum):
    development = "development"
    production = "production"


MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")
MARIADB_PORT = int(os.getenv("MARIADB_PORT", 3306))
MARIADB_HOST = os.getenv("MARIADB_HOST", "127.0.0.1")
MARIADB_USER = os.getenv("MARIADB_USER", "seeker")
MARIADB_DATABASE = os.getenv("MARIADB_DATABASE", "seeker")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
env_value = os.getenv("ENVIRONMENT", "production").lower()

try:
    ENVIRONMENT = Environment(env_value)
except ValueError:
    raise ValueError(f"Invalid ENVIRONMENT: {env_value}")

DEFAULT_PREFIX = "!!"

DEFAULT_INTENTS = discord.Intents.default()
DEFAULT_INTENTS.message_content = True
