from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("IP")  # Xosting ip manzili
DOMAIN = env.str("DOMAIN")
ERROR_NOTIFY_CHANNEL_ID = env.str("ERROR_NOTIFY_CHANNEL_ID")
ERROR_NOTIFY_BOT_TOKEN = env.str("ERROR_NOTIFY_BOT_TOKEN")
