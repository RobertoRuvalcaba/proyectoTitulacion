def detectar_sintomas(texto):
    sintomas_infarto = ["dolor en el pecho", "falta de aire", "náuseas", "sudoración", "mareo"]
    sintomas_detectados = [sintoma for sintoma in sintomas_infarto if sintoma in texto]

    if sintomas_detectados:
        respuesta = "Parece que estás describiendo síntomas que podrían estar relacionados con un infarto. Estos son los síntomas que detecté: "
        respuesta += ', '.join(sintomas_detectados)
        respuesta += ". Por favor, busca atención médica inmediatamente si sientes que tu salud está en peligro."
        return respuesta

    respuestas_generales = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "gracias": "¡De nada! Estoy aquí para ayudar.",
        "adiós": "¡Hasta luego! Cuídate.",
        "¿cómo estás?": "Soy solo un programa, así que no tengo emociones, ¡pero gracias por preguntar! ¿En qué puedo ayudarte?"
    }

    return respuestas_generales.get(texto, "No tengo una respuesta para eso. Si tienes síntomas o preocupaciones de salud, te recomiendo consultar a un médico.")

print("Chatbot: Hola, ¿cómo puedo ayudarte?")
while True:
    user_input = input("Tú: ").lower()
    if user_input == 'salir':
        print("Chatbot: ¡Hasta luego! Cuídate.")
        break
    respuesta = detectar_sintomas(user_input)
    print(f"Chatbot: {respuesta}")


