import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola, soy el chat box de preguntas del ITLA', ['hola', 'klk', 'saludos', 'buenas', 'weo'], single_response = True)
        response('Estoy bien y tu?', [ 'estas', 'vas', 'vas',], required_words=['como'])
        response('Los numeros de telefonos del ITLA son: 809-738-4852 / 809-793-2557', ['contacto', 'celular', 'telefono'], single_response = True)
        response('El Itla fue inagurado el 13 de agosto del año 2000', ['fundacion', 'inaugurado', 'creacion'], single_response = True)
        response('El horario del Itla es: Lunes - viernes │ 8:00 a. m. - 4:00 p. m.', ['horario', 'labora', 'abre'], single_response = True)
        response('Las siglas ITLA significan: Instituto Tecnologico de las Americas', ['siglas', 'letras', 'palabras'], single_response = True)
        response('El rector actual del ITLA se llama Omar Mendez Lluberes', ['nombre', 'llama'], single_response = True)
        response('Estudiantes mayores de 16 años o en tercero de bachillerato para Educación Permanente', ['quienes', 'personas', 'quien'], single_response = True)
        response('Puede llamar a servicio al cliente al 809-738-4852', ['orientar', 'dirijo', 'guiar'], single_response = True)
        response('Pasar por Bedelería con su factura o comprobante de inscripción', ['averiguar', 'departamento', 'ir'], single_response = True)
        response('Segun el Art.49 Ningun(a) estudiante podra retirar una asignatura mas de dos (2) veces', ['retirar', 'ocasiones', 'ocasionalmente'], single_response = True)
        response('En el ITLA se imparten 15 carreras tecnologicas', ['tiene', 'posee', 'presenta'], single_response = True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'te debo una', 'muchas gracias por tu ayuda', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['me podrias especificar mejor tu pregunta?', 'no entiendo lo que me quieres decir', 'intenta buscarlo en google a ver que te dice',][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))