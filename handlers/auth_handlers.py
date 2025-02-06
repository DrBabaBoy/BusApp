# ------------ handlers/auth_handlers.py ------------
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
import json
from pathlib import Path
from utils import messages, keyboards

# Estados para las conversaciones
VERIFICAR, NOMBRE, APELLIDO, TELEFONO = range(4)
LOGIN = range(1)

# Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent.parent
CODES_PATH = BASE_DIR / "data/CODES.json"

# Cargar códigos de operadores
with open(CODES_PATH, "r") as file:
    operadores = json.load(file)

# Diccionario para mantener las sesiones activas
sesiones = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start."""
    nombre = update.effective_user.first_name
    await update.message.reply_text(
        messages.BIENVENIDA.format(nombre=nombre),
        reply_markup=keyboards.menu_principal
    )

async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja las opciones del menú principal."""
    text = update.message.text
    if text == 'Verificar Operador':
        return await verificar_operador(update, context)
    elif text == 'Iniciar Sesión':
        return await iniciar_sesion(update, context)
    elif text == 'Soporte':
        await update.message.reply_text(
            messages.OPERACION["soporte"],
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    elif text == 'Información':
        await update.message.reply_text(
            messages.INFORMACION,
            reply_markup=keyboards.menu_principal
        )
    else:
        await update.message.reply_text(
            messages.ERRORES["opcion_invalida"],
            reply_markup=keyboards.menu_principal
        )

async def verificar_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicia el proceso de verificación de operador."""
    await update.message.reply_text(
        messages.VERIFICACION["solicitar_codigo"],
        reply_markup=keyboards.remove_keyboard
    )
    return VERIFICAR

async def proceso_verificar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Verifica el código del operador."""
    codigo = update.message.text.strip()
    user_id = str(update.effective_user.id)
    
    if codigo in operadores["codigos"]:
        operador = operadores["codigos"][codigo]
        
        if operador["nombre"]:
            await update.message.reply_text(
                messages.VERIFICACION["ya_verificado"].format(nombre=operador["nombre"]),
                reply_markup=keyboards.menu_operador
            )
            sesiones[user_id] = codigo
            return ConversationHandler.END
        else:
            context.user_data["codigo"] = codigo
            await update.message.reply_text(messages.VERIFICACION["solicitar_datos"])
            return NOMBRE
            
    await update.message.reply_text(
        messages.VERIFICACION["codigo_incorrecto"],
        reply_markup=keyboards.menu_principal
    )
    return ConversationHandler.END

async def proceso_nombre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Solicita y guarda el nombre del operador."""
    context.user_data["nombre"] = update.message.text.strip()
    await update.message.reply_text(messages.VERIFICACION["solicitar_apellido"])
    return APELLIDO

async def proceso_apellido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Solicita y guarda el apellido del operador."""
    context.user_data["apellido"] = update.message.text.strip()
    await update.message.reply_text(messages.VERIFICACION["solicitar_telefono"])
    return TELEFONO

async def proceso_telefono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Solicita y guarda el teléfono del operador."""
    user_data = context.user_data
    codigo = user_data["codigo"]
    
    operadores["codigos"][codigo].update({
        "nombre": user_data["nombre"],
        "apellido": user_data["apellido"],
        "telefono": update.message.text.strip()
    })
    
    with open(CODES_PATH, "w") as file:
        json.dump(operadores, file, indent=4)
    
    await update.message.reply_text(
        messages.VERIFICACION["registro_completo"].format(
            nombre=user_data["nombre"],
            apellido=user_data["apellido"]
        ),
        reply_markup=keyboards.menu_operador
    )
    
    sesiones[str(update.effective_user.id)] = codigo
    return ConversationHandler.END

async def iniciar_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicia el proceso de inicio de sesión."""
    await update.message.reply_text(
        messages.VERIFICACION["solicitar_codigo"],
        reply_markup=keyboards.remove_keyboard
    )
    return LOGIN

async def proceso_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Verifica el código para iniciar sesión."""
    codigo = update.message.text.strip()
    user_id = str(update.effective_user.id)
    
    if codigo in operadores["codigos"] and operadores["codigos"][codigo]["nombre"]:
        sesiones[user_id] = codigo
        nombre = operadores["codigos"][codigo]["nombre"]
        await update.message.reply_text(
            messages.OPERACION["sesion_iniciada"].format(nombre=nombre),
            reply_markup=keyboards.menu_operador
        )
    else:
        await update.message.reply_text(
            messages.VERIFICACION["codigo_incorrecto"],
            reply_markup=keyboards.menu_principal
        )
    return ConversationHandler.END

async def cerrar_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cierra la sesión del operador."""
    user_id = str(update.effective_user.id)
    if user_id in sesiones:
        del sesiones[user_id]
    await update.message.reply_text(
        messages.OPERACION["cerrar_sesion"],
        reply_markup=keyboards.menu_principal
    )