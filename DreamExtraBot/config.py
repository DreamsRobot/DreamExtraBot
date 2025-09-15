import os

class Config:
    API_ID = int(os.getenv("API_ID", "24995612"))
    API_HASH = os.getenv("API_HASH", "69c7efab5fa104ed4ad3f9db5cacd96e")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    OWNER_ID = int(os.getenv("OWNER_ID", "6934809750"))
