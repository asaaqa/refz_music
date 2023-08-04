from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/226d35be77cb3874ac445.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/226d35be77cb3874ac445.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/lPPPPPPI")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mcsec7")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://graph.org/file/226d35be77cb3874ac445.jpg"
