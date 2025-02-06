# ------------ main.py ------------
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)
from config import API
from handlers import auth_handlers, operator_handlers, error_handlers
from utils import keyboards
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def setup_handlers(application):
    # Handlers principales
    application.add_handler(CommandHandler("start", auth_handlers.start))
    
    # Conversación de verificación
    conv_verificar = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^Verificar Operador$'), auth_handlers.verificar_operador)],
        states={
            auth_handlers.VERIFICAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handlers.proceso_verificar)],
            auth_handlers.NOMBRE: [MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handlers.proceso_nombre)],
            auth_handlers.APELLIDO: [MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handlers.proceso_apellido)],
            auth_handlers.TELEFONO: [MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handlers.proceso_telefono)]
        },
        fallbacks=[MessageHandler(filters.ALL, error_handlers.error)]
    )
    application.add_handler(conv_verificar)
    
    # Conversación de inicio de sesión
    conv_login = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^Iniciar Sesión$'), auth_handlers.iniciar_sesion)],
        states={
            auth_handlers.LOGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handlers.proceso_login)]
        },
        fallbacks=[MessageHandler(filters.ALL, error_handlers.error)]
    )
    application.add_handler(conv_login)
    
    # Handlers de operador
    application.add_handler(MessageHandler(
        filters.Regex('^(Iniciar Viaje|Falla Mecanica|Finalizar Viaje|Soporte)$'),
        operator_handlers.handle_menu_operador
    ))
    
    # Menú principal
    application.add_handler(MessageHandler(
        filters.Regex('^(Verificar Operador|Iniciar Sesión|Soporte|Información)$'),
        auth_handlers.handle_main_menu
    ))
    
    # Cerrar sesión
    application.add_handler(MessageHandler(
        filters.Regex('^Cerrar Sesión$'),
        auth_handlers.cerrar_sesion
    ))
    
    # Errores
    application.add_error_handler(error_handlers.error)

def main():
    application = ApplicationBuilder().token(API).build()
    setup_handlers(application)
    application.run_polling()

if __name__ == "__main__":
    main()