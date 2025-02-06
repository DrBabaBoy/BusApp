# ------------ utils/messages.py ------------
BIENVENIDA = """
👋 Bienvenido, *{nombre}*.

Este es el *Bot de Operadores de Transporte* 🚍.
Selecciona una opción del menú para comenzar.
"""

VERIFICACION = {
    "solicitar_codigo": "🔑 Ingresa tu *código de operador* para continuar.",
    "codigo_incorrecto": "❌ El *código* no es válido.\n\nVerifícalo y vuelve a intentarlo. Contacta a soporte si el problema persiste.",
    "solicitar_datos": "✏️ Escribe tu *nombre completo* para continuar.",
    "solicitar_apellido": "📝 Ingresa tu *apellido* para completar el registro.",
    "solicitar_telefono": "📞 Proporciona tu *número de teléfono* para finalizar tu registro.",
    "registro_completo": "✅ *{nombre} {apellido}*, tu registro como operador se completó.\nYa puedes gestionar tus actividades. ¡Bienvenido! 🌟",
    "ya_verificado": "⚠️ Hola, *{nombre}*.\n\nYa completaste tu registro. Si necesitas ayuda, contáctanos."
}

OPERACION = {
    "iniciar_viaje": "🗺️ Selecciona tu ruta:\n1️⃣ *Mina-Canticas/Coatza*\n¡Buen viaje!",
    "falla_mecanica": "El servicio de la unidad x Esta suspendido temporalmente\n",
    "finalizar_viaje": "🏁 Viaje completado con éxito.\n\nGracias por tu esfuerzo. 🌟",
    "soporte": "📞 Contacto con soporte: [*Chat de Soporte*](https://t.me/xyzxgll).\n\nUn representante te asistirá pronto.",
    "cerrar_sesion": "🔒 Sesión cerrada.\n\nGracias por usar el sistema. ¡Hasta pronto! 👋",
    "sesion_iniciada": "🔓 Sesión activa. Hola, *{nombre}*.\nAdministra tus actividades sin problemas. 🚍"
}

ERRORES = {
    "general": "⚠️ Ha ocurrido un *error*.\n\nInténtalo más tarde o contacta a soporte.",
    "soporte": "⚠️ No fue posible conectarte al *soporte*.\n\nInténtalo más tarde.",
    "opcion_invalida": "❌ Selecciona una *opción* del menú disponible.",
}

INFORMACION = "ℹ️ Este bot te ayuda a gestionar tus tareas como operador de transporte.\nContáctanos para más detalles."