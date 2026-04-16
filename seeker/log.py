from logging.config import dictConfig

from seeker.config import ENVIRONMENT, Environment

LOG_LEVEL = "INFO" if ENVIRONMENT == Environment.production else "DEBUG"
DISCORD_LOG_LEVEL = "WARNING" if ENVIRONMENT == Environment.production else "INFO"

LOGGING_CONFIG = {  # type: ignore
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        # "file": {
        #     "level": "WARNING",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": "logs/seeker.log",
        #     "mode": "a",
        #     "maxBytes": 10 * 1024 * 1024,  # 10 MB
        #     "backupCount": 5,
        #     "formatter": "standard",
        # },
    },
    "loggers": {
        "": {  # root
            "handlers": ["console"],
            "level": LOG_LEVEL,
        },
        "seeker": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "discord": {
            "handlers": ["console"],
            "level": DISCORD_LOG_LEVEL,
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)
