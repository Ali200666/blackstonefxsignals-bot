import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Foydalanuvchilar ro'yxati (ruxsat berilganlar)
allowed_users = [123456789, 987654321]  # O'zingiz va do'stlaringiz Telegram ID'sini kiriting

# Loglarni sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in allowed_users:
        await update.message.reply_text(
            "Assalomu alaykum! BlackstoneFXsignals botiga xush kelibsiz."
        )
    else:
        await update.message.reply_text("Kechirasiz, sizda ushbu botdan foydalanishga ruxsat yo‘q.")

# Signal yuborish funksiyasi (admin uchun)
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in allowed_users:
        text = " ".join(context.args)
        for user_id in allowed_users:
            if user_id != update.effective_user.id:
                await context.bot.send_message(chat_id=user_id, text=f"YANGI SIGNAL:\n{text}")
        await update.message.reply_text("Signal yuborildi.")
    else:
        await update.message.reply_text("Siz signal yuborolmaysiz.")

# TP yoki SL natijasini yuborish
async def result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in allowed_users:
        text = " ".join(context.args)
        for user_id in allowed_users:
            if user_id != update.effective_user.id:
                await context.bot.send_message(chat_id=user_id, text=f"Natija:\n{text}")
        await update.message.reply_text("Natija yuborildi.")
    else:
        await update.message.reply_text("Siz natija yuborolmaysiz.")

# Botni ishga tushirish
if __name__ == '__main__':
    import asyncio

    async def main():
        app = ApplicationBuilder().token("7860157520:AAE3Uf-CxAjEO_HRLH0V_XHLYHxXh8Wpl_8").build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("signal", signal))
        app.add_handler(CommandHandler("natija", result))

        print("Bot ishga tushdi...")
        await app.run_polling()

    asyncio.run(main())
    python3 bot.py
    Bot ishga tushdi...