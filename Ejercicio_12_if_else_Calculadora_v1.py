print("\n")
print("==================================================================")
print("||......++++........................***......***...........///..||")
print("||......++++.........................***....***...........///...||")
print("||...++++++++++++....============......******............///....||")
print("||...++++++++++++....============......******...........///.....||")
print("||......++++.........................***....***........///......||")
print("||......++++........................***......***......///.......||")
print("==================================================================\n")

while True:
    print("\n[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")
    print("[5] Salir\n")

    try:
        opcion = int(input("Ingrese una opción del menú: "))
        if opcion == 5:
            print("[!] Saliendo del programa...")
            break
        if opcion not in range(1, 5):  # Simplificado
            raise ValueError  # Lanza error si no está en el rango permitido
    except ValueError:
        print("\n[!] Opción no válida. Debe ser un número entre 1 y 5.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("\n[!] Número no válido.\n")
        continue

    if opcion == 1:
        resultado = num1 + num2
        operador = "+"
    elif opcion == 2:
        resultado = num1 - num2
        operador = "-"
    elif opcion == 3:
        resultado = num1 * num2
        operador = "*"
    elif opcion == 4:
        if num2 == 0:
            print("\n[!] Error: No se puede dividir entre 0.\n")
            continue
        resultado = num1 / num2
        operador = "/"

    print(f"\n[{operador}] El resultado de {num1} {operador} {num2} es: {resultado}\n")
