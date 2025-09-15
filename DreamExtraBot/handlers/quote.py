from pyrogram import Client, filters
from pyrogram.types import Message
from quotly import quotly

@Client.on_message(filters.command("q") & filters.reply)
async def quote_sticker(client: Client, message: Message):
    replied = message.reply_to_message

    if not replied:
        return await message.reply_text("⚠️ Reply to a message with /q to make a quote!")

    try:
        # Generate quote
        quote = await quotly.create(
            messages=[replied],
            reply_message=message,
        )
        await message.reply_sticker(quote)
    except Exception as e:
        await message.reply_text(f"❌ Failed to create quote: {e}")
