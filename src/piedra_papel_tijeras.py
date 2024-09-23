import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    print("Te damos la bienvenida al juego")
    eleccion_ordenador = ordenador_decide_jugada()
    eleccion_usuario = usuario_decide_jugada()
    print("El ordenador eligió: ", eleccion_ordenador)
    resultado = determina_ganador(eleccion_usuario, eleccion_ordenador)
    print("Resultado: ", resultado)

def jugar_torneo():
    '''
    Juega un torneo donde el primer jugador que alcance 3 puntos gana.
    '''
    puntos_usuario = 0
    puntos_ordenador = 0
    
    while puntos_usuario < 3 and puntos_ordenador < 3:
        print("Puntuación Usuario: ", puntos_usuario, "\nPuntuación Ordenador: ", puntos_ordenador)
        jugada_ordenador = ordenador_decide_jugada()
        jugada_usuario = usuario_decide_jugada()
        print("El ordenador eligió: ", jugada_ordenador)
        resultado = determina_ganador(jugada_usuario, jugada_ordenador)
        print("Resultado de la ronda: ", resultado)
        
        if resultado == "Ganaste":
            puntos_usuario += 1
        elif resultado == "Perdiste":
            puntos_ordenador += 1
    
    if puntos_usuario == 3:
        print("¡Felicidades! Ganaste el torneo.")
    else:
        print("Lo siento, perdiste el torneo.")