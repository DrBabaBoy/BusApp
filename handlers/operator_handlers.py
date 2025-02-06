# ------------ handlers/operator_handlers.py ------------
from telegram import Update
from telegram.ext import ContextTypes
from utils import messages, keyboards

async def handle_menu_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Iniciar Viaje':
        await iniciar_viaje(update, context)
    elif text == 'Falla Mecanica':
        await falla_mecanica(update, context)
    elif text == 'Finalizar Viaje':
        await finalizar_viaje(update, context)
    elif text == 'Soporte':
        await soporte_operador(update, context)

async def iniciar_viaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.OPERACION["iniciar_viaje"],
        reply_markup=keyboards.menu_operador
    )

async def falla_mecanica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.OPERACION["falla_mecanica"],
        reply_markup=keyboards.menu_operador
    )

async def finalizar_viaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.OPERACION["finalizar_viaje"],
        reply_markup=keyboards.menu_operador
    )

async def soporte_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        messages.OPERACION["soporte"],
        parse_mode="Markdown",
        disable_web_page_preview=True
    )