# ------------ handlers/error_handlers.py ------------
from telegram import Update
from telegram.ext import ContextTypes
from utils import messages, keyboards

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.ERRORES["general"],
        reply_markup=keyboards.menu_principal
    )

async def opcion_invalida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.ERRORES["opcion_invalida"],
        reply_markup=keyboards.menu_principal
    )