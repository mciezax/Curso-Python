def quicksort(lista):
    if len(lista) <= 1:  # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return lista
    
    pivote = lista[len(lista) // 2]  # Se elige el pivote (en este caso, el del medio)
    izquierda = [x for x in lista if x < pivote]  # Elementos menores al pivote
    centro = [x for x in lista if x == pivote]  # Elementos iguales al pivote
    derecha = [x for x in lista if x > pivote]  # Elementos mayores al pivote

    return quicksort(izquierda) + centro + quicksort(derecha)  # Recursión

# Lista desordenada
numeros = [10, 5, 2, 3, 7, 13, 1, 9]
print("Lista original:", numeros)

# Aplicando QuickSort
ordenada = quicksort(numeros)

print("Lista ordenada:", ordenada)
