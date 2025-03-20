import random

    # Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
puntaje = 0

# Se seleccionan preguntas aleatorias   
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
print(questions_to_ask)
print(questions_to_ask[0][2])

# El usuario deberá contestar 3 preguntas
for _ in range(3):

    # Se muestra la pregunta actual y las respuestas posibles
    print(questions_to_ask[_][0])
    for i, answer in enumerate(questions_to_ask[_][1]):
        print(f"{i + 1}. {answer}")
    once = False

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (int(input("Respuesta: "))) - 1

        #Se verifica que la respuesta sea un int valido
        if type(user_answer)!=int or user_answer not in range(0, 4): 
             print("Respuesta invalida. Escriba un numero de 1 a 4") 
             continue
        else:
             
        # Se verifica si la respuesta es correcta
             if (user_answer) == questions_to_ask[_][2]:
                 print("¡Correcto!")

                 #Se suma puntaje y se continua a la siguiente pregunta.
                 puntaje += 1
                 break
             else: 
                 
                 #Si es la primera vez que responde, se imprime un mensaje.
                 if not once:
                     print("Incorrecto, intente de nuevo.")
                     once = True

                 #Se resta puntaje y continua con el ultimo intento.    
                 puntaje -= 0.5
                 continue
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(questions_to_ask[_][1][(questions_to_ask[_][2])])
        #Se resetea la cantidad de intentos.
        once = False
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Puntaje final: {puntaje}")
