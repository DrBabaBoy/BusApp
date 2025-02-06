# ------------ utils/keyboards.py ------------
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def crear_teclado(opciones):
    return ReplyKeyboardMarkup(opciones, resize_keyboard=True)

menu_principal = crear_teclado([
    ['Verificar Operador'],
    ['Iniciar Sesión'],
    ['Soporte', 'Información']
])

menu_operador = crear_teclado([
    ['Iniciar Viaje', 'Falla Mecanica'],
    ['Finalizar Viaje', 'Soporte'],
    ['Cerrar Sesión']
])

remove_keyboard = ReplyKeyboardRemove()