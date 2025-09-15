from pyrogram import Client
from DreamExtraBot.config import Config
from DreamExtraBot.utils.logger import logger
import DreamExtraBot.handlers.quote

app = Client(
    "DreamExtraBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

if __name__ == "__main__":
    logger.info("🚀 DreamExtraBot is starting...")
    app.run()
