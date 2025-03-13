my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
i = 0
while i < len(my_list) - 1:
    if my_list[i] == my_list[i + 1]:
        del my_list[i]
    else:
        i += 1
#
print("La lista con elementos únicos:")
print(my_list)