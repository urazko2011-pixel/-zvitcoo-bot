from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

reports = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Відправ звіт у форматі:\nОбійшов 21\nЗробив 2"
    )

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reports[update.effective_user.first_name] = update.message.text
    await update.message.reply_text("Звіт прийнято ✅")

async def result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📊 Звіти:\n\n"
    for user, rep in reports.items():
        text += f"{user}:\n{rep}\n\n"
    await update.message.reply_text(text)

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("result", result))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, report))

app.run_polling()
