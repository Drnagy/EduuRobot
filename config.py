from typing import List

# This is a template configuration file for EduuRobot.
# You can use this file as a base for your own config file by
# copying this file to `eduu/config.py` and filling in the values.
#


# API keys

# Bot token from Bot Father
TOKEN: str = "6156942689:AAHxJ8YZzKcXJKx-42BV-U1W6GNLqMs0X5U"

# Telegram API ID and API hash
# Get it from https://my.telegram.org/apps
API_ID: int = 13760933
API_HASH: str = "17cdd93b30aa096cb9e022fb71bf690c"

# Tenor API key
# Get it from https://tenor.com/developer/keyregistration
# Can be empty (but the /gif command won't work without it)
TENOR_API_KEY: str = ""


# Admins/sudoers settings

# Sudoers and super sudoers
SUPER_SUDOERS: List[int] = [5886877255]
SUDOERS: List[int] = [5886877255]

# All super sudoers should be sudoers as well
SUDOERS.extend(SUPER_SUDOERS)


# Other settings

# Database file path
DATABASE_PATH = "mongodb+srv://nagy4462:gotoemail1998@cluster0.9fiktsg.mongodb.net/?retryWrites=true&w=majority"

# Number of updates that can be processed in parallel
WORKERS = 24

# Chat used for logging
LOG_CHAT: int = -1001788420032

# Prefixes for commands
# e.g: /command and !command
PREFIXES: List[str] = ["/", "!"]

# List of disabled plugins
DISABLED_PLUGINS: List[str] = []
