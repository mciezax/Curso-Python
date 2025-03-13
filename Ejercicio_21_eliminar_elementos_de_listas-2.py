lista = [1, 2, 3, 4, 5]

central=(int(input("Ingrese un numero entero para reemplazar el numero central de la lista: ")))

lista[2]=central

print(lista)
del lista[-1] #elimina el ultimo elemento de la lista

print(lista)

print(len(lista)) #imprime el numero de elemntos

lista.append(34) #Agregar un elemento

print(lista)