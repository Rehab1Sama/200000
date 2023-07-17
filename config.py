from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "27886257"))
API_HASH = getenv("API_HASH", "698b9c79706423ac2919e2ce466262e5")
BOT_TOKEN = getenv("BOT_TOKEN", "5829569154:AAEKkTp4f7m5uvg4RsxEF1dzejdtdnZ2KIg")
SESSION_NAME = getenv("SESSION_NAME", "BAC9H-NnKarjJa0hWMz6jYg54k_2OLyOs-on1JLlJRff3W9s7GW0znn5HrIDLwco2HJaV5NQNQdSrHurU7NVSgOjbRCvL7iVGHHCF4D830uC1lmxhPhPOKI9yU66tQGsPf6ykICJ1_ztxTMRB5iptWdGXvqVHJ8lAXrzY9Kp0er37Op8v8Cx38aq1Ampnw5hhTNh4ffaSAUx0K5P54U2Ior9uCnQV46FQwLbRV3ow_dVlOPmD33oLMSX81fA3KyEaa5oVH0dgxDHtJiSK6PvWpvFYYONzIR80Y8j8-tzZD59Te6QKpG61DlZaxRMRjLwrB3yaZOd19fN7WtW4WgWJBIaAAAAAVAXiIwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Ree1Ree")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Rehab_bot1")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
