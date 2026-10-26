import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Your Bot Token from BotFather
TOKEN = 8579220355:AAGiDwN3Ho5mjzzoEn2vQAf8tSdX9S1604Y


async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text = update.message.text
  # Check if the message is a link/URL
  if text.startswith("http://") or text.startswith("https://"):
    # Simple shortening/formatting mock logic for demonstration
    shortened = f"https://t.me/DW_New_Link_bot?start={text}"
    await update.message.reply_text(
        f"🔗 **Your Link is Ready!**\n\n{shortened}", parse_mode="Markdown"
    )
  else:
    await update.message.reply_text(
        "⚠️ Please send a valid link starting with http:// or https://"
    )


def main():
  # Build the application with your token
  application = ApplicationBuilder().token(TOKEN).build()

  # Add message handler for text links
  application.add_handler(
      MessageHandler(filters.TEXT & (~filters.COMMAND), shorten_link)
  )

  print("Bot is running...")
  # Run the bot
  application.run_polling()


if __name__ == "__main__":
  main()
  
