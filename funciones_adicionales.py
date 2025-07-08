# Importar módulos.
import logging
from colorama import Fore


def input_personalizado(n_min, n_max, letras_validas=[], texto="Escribe aquí: "):
    """
    Funciona como un input normal, pero realiza un bucle hasta que el usuario
    introduzca un input válido entre los deseados.

    Los inputs válidos se setean mediante los parámetros:
    n_min : (int) número más bajo, excluído.
    n_max : (int) número límite más alto, excluído.
    letras_validas : (list) con elementos válidos.
    texto : (str) se le muestra al usuario.

    ejemplo:
    input_personalizado(n_min=0, n_max=5, letras_validas=["m", "v"], texto="Opción: ")
    Esto ejecutaría un bucle hasta que el usuario introduzca un valor numérico entre
    1,2,3,4 o las letras "m" "v".
    """

    while True:
        # Se le pide el input.
        user_input = input(Fore.BLUE +texto)

        # Intentar convertir el input a número. Si funciona, y es válido, lo devuelve.
        try: 
            user_input_int = int(user_input)
            if n_min < user_input_int < n_max:
                return user_input_int
        # Verificar si es input válido o repetir bucle.
        except:
            if user_input.lower() in letras_validas:
                return user_input
        
        logging.warning("Se introdujo un input inválido")
        print(Fore.RED + "Ese no es un input válido \n" "Por favor intenta de nuevo:")


def input_numerico(texto):
    """
    Funciona como un input normal, pero convierte siempre el input a INT
    y en caso de que no sea posible, repite hasta que se cumpla.

    texto : (str) texto mostrado en la funcion input()
    """
    
    while True:
        input_usuario = input(Fore.YELLOW + texto)

        # Si es vacío, devuelve 0.
        if input_usuario == "":
            return 0
        
        # Intentar transformarlo en int y devolverlo.
        try:
            input_num = int(input_usuario)
            return input_num
        # Si no, informa que se introdujo un input inválido. Se repite.
        except:
            print(Fore.RED + "Solo se aceptan valores numericos")
            logging.warning("Se introdujo un input inválido")
    

def print_caja(texto):
    """
    Función utilizada para dibujar lineas de texto en forma de caja.
    Se introduce el texto a cubrir con la caja.
    La caja no es adaptable, tiene un ancho de 35 caracteres.

    texto : texto a excribir.
    """
    # Borrar espacios al inicio y al final.
    texto_bruto = texto.strip()
    # Separar el texto por lineas
    lineas = texto_bruto.split("\n")

    # Tamaño de la caja
    len_max = 36
    # Calcular cuanto ocupa el título (la primera linea)
    titulo_len = len(lineas[0])
    
    # Dibujar la primera linea.
    print(Fore.MAGENTA + "|" + "-"*len_max + "|")
    # Dibujar la segunda, con el título en medio.
    print("|------- " + lineas[0] + "-" * (len_max-len(lineas[0])-8) + "|")

    # Dibujar todas las otras líneas
    for linea in lineas[1: ]:
        print(Fore.GREEN + "|-- " + linea + " " * (len_max-len(linea)-3) + "|")

    # Dibujar la linea final.
    print(Fore.MAGENTA + "|" + "-"*len_max + "|")


