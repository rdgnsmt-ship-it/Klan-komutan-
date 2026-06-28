import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN, CLAN_TAG

# Log ayarı
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Klan Komutanı aktif!\n\n"
        f"📌 Klan: {CLAN_TAG}\n"
        "⚔️ Savaş sistemi hazırlanıyor...\n"
        "🏆 Bildirimler aktif olacak."
    )

# /help komutu
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 KOMUTLAR\n\n"
        "/start - Botu başlat\n"
        "/help - Komutlar\n"
        "/klan - Klan bilgisi (yakında)\n"
        "/savas - Savaş durumu (yakında)\n"
    )

# /klan (şimdilik test)
async def clan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🛡️ Klan Takibi Aktif\n📌 Klan Etiketi: {CLAN_TAG}\n\n"
        "⚔️ Veriler API üzerinden çekilecek (bir sonraki adım)"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Komutlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("klan", clan))

    print("Klan Komutanı çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
