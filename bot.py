import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from agent import async_combined_agent

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = await async_combined_agent(user_input)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

app.run_polling()