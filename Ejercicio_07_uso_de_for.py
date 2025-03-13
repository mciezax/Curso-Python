#Sintaxis básica de for

#for variable in secuencia:
#Código dentro del bucle

#Ejemplo: Recorriendo una lista

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta) 


#Usando range() para iterar en un rango de números

for i in range(5):  # De 0 a 4
    print(i)


#Opciones de range():


#range(inicio, fin, paso)

#Ejemplo con range(1, 10, 2):


for i in range(1, 10, 2):  # Empieza en 1, hasta 9, con saltos de 2
    print(i)

# for con enumerate() (índices y valores)

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")

#for en cadenas de texto

palabra = "Python"
for letra in palabra:
    print(letra)

#for en diccionarios

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")


#Usando break y continue en for
# break: Sale del bucle antes de que termine


for numero in range(10):
    if numero == 5:
        break
    print(numero)

#continue: Salta una iteración y sigue con la siguiente


for numero in range(5):
    if numero == 2:
        continue
    print(numero)


#for con else (opcional)

#Si el for se ejecuta sin interrupciones (break), el else se ejecuta.


for i in range(3):
    print(i)
else:
    print("Bucle terminado correctamente")



