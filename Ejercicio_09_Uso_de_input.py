print("Dime algo: ")
algo = input()
print("Hmmm...", algo, "...en serio?")


palabra = input("Escripe una palabra: ")
print("la palabra es: ",palabra, "...cierto?")



numero = int(input("Ingrese un numero: "))
potencia = numero ** 2.0
print(numero, "al cuadrado es: ", potencia)

nombre = input("Ingresa es tu nombre: ")
apellido = input("Ingresa tu apellidp: ")
print("Gracias. ")
print("\nTu nombre es "+ nombre + " " + apellido + ".")


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))





# ingresa un valor flotante para la variable a aquí
a = float(input("Ingrese el valor : "))
# ingresa un valor flotante para la variable b aquí
b = float(input("Ingrese el valor : "))
# mostrar el resultado de la suma aquí
print(a + b)
# mostrar el resultado de la resta aquí
print(a - b)
# mostrar el resultado de la multiplicación aquí
print(a * b)
# mostrar el resultado de la división aquí
print(a / b)

print("\n¡Eso es todo, amigos!")


x = int(input("Ingresa un número: ")) 
print(x * "5")