from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR-BOT-TOKEN" # Your Telegram-bot token from BotFather

# Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi")

if __name__ == "__main__":
    print("Бот запускается...")
    app = Application.builder().token(TOKEN).build()
  
    app.add_handler(CommandHandler("start", start_command))
    
    print("Telegram-bot started.")
    app.run_polling()
