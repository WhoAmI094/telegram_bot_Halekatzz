from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import os

# Get Bot Token from Environment Variables
TOKEN = os.getenv("7763926224:AAHggKBUbtMITl8mo0mCm50dqQKrFS465ek")

# Create the bot application
app = Application.builder().token(TOKEN).build()

# Start command
async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your Telegram bot.")

# Message handler (echoes messages)
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot
app.run_polling()