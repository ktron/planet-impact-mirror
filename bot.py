from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from agent import satire_bot

#t.me/PlanetMirror_ktron_bot
#Use this token to access the HTTP API:
#7436113275:AAFzLfuu_bhsvInwmiI0Q9nBIULrEZ4Xko0
TOKEN = "7436113275:AAFzLfuu_bhsvInwmiI0Q9nBIULrEZ4Xko0"

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = satire_bot(user_input)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

app.run_polling()
