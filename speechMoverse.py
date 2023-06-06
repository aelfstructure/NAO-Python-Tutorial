# -*- coding: cp1252 -*-
import sys
import math
from naoqi import ALProxy

def main(robot_ip, robot_port):
    # Inicializar la conexi�n con el robot NAO
    try:
        tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
        asr = ALProxy("ALSpeechRecognition", robot_ip, robot_port)
        motion = ALProxy("ALMotion", robot_ip, robot_port)
    except Exception as e:
        print("Error al conectar con el robot:", e)
        sys.exit(1)

    # Configurar las preguntas y respuestas
    preguntas_respuestas = {
        "hola": "�Hola! �C�mo est�s?",
        "como estas": "Estoy bien, gracias por preguntar.",
    }

    # Configurar la gram�tica de reconocimiento de voz
    vocabulary = preguntas_respuestas.keys()
    asr.setVocabulary(vocabulary, False)

    # Definir la funci�n de respuesta a la voz
    def procesar_respuesta(value):
        if value in preguntas_respuestas:
            respuesta = preguntas_respuestas[value]
            tts.say(respuesta)
            if value == "ven hacia mi":
                # Moverse 5 cent�metros hacia adelante
                motion.move(0.05, 0, 0)
        else:
            tts.say("Lo siento, no puedo responder a esa pregunta.")

    # Conectar la funci�n de respuesta al evento de reconocimiento de voz
    asr.subscribe("Test_ASR")
    asr.signal.connect(procesar_respuesta)

    # Mantener el programa en ejecuci�n hasta que se presione Ctrl + C
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    # Desconectar y limpiar recursos antes de finalizar
    asr.unsubscribe("Test_ASR")

if __name__ == "__main__":
    robot_ip = "192.168.1.100"  # Reemplaza con la direcci�n IP de tu robot NAO
    robot_port = 9559

    main(robot_ip, robot_port)


