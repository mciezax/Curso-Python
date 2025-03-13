import time
palabra= input("Ingrese una palabra: ")

palabra = palabra.upper()
vocales = ["A","E","I","O","U"]

for letra in palabra:

    if letra not in vocales:
        time.sleep(2)
        print(letra)