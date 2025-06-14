import random
import time
caracteres = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '{', '}', '[', ']', '|', ':',
    ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~'
]
def generar_contraseña():
    contraseña = ""
    longitud = int(input("ingresa la longitud de tu contraseña: "))
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    print("Generando tu contraseña...")
    time.sleep(1)
    print("aqui tienes tu contraseña:")
    print(contraseña)
    return contraseña
generar_contraseña()

    