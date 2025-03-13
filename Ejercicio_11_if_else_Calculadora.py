print("\n")
print("==================================================================")
print("||......++++........................***......***...........///..||")
print("||......++++.........................***....***...........///...||")
print("||...++++++++++++....============.......******...........///....||")
print("||...++++++++++++....============.......******..........///.....||")
print("||......++++.........................***....***........///......||")
print("||......++++........................***......***......///.......||")
print("==================================================================\n")

while True:
   


    print("\n[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicacion")
    print("[4] division")
    print("[5] Salir\n")

    try:
        opcion=int(input("Ingrese una opcion del menu: "))
    except ValueError:
        print("\n[!] Opción no válida. Debe ser un número entre 1 y 5.")
        continue
    if opcion == 5:
        print("[!] Salieendo del programa...")
        break
        
    if opcion not in [1,2,3,4]:
        print("\n[!] Opcion fuera del rango. Intentalo de nuevo.")
        continue

            
    try:
        num1=float(input("Ingresa el primer numero: "))
        num2=float(input("Ingresa el Segundo numero: "))
        
    except ValueError:
        print("\n [!] numero no valido.\n")
        continue

    if opcion==1:
        print(f"\n[+] La suma de {num1} + {num2} es: ", num1 + num2)
    elif opcion==2:
        print(f"\n[-] La resta de {num1} - {num2} es: ", num1 - num2)
    elif opcion==3:
        print(f"\n[*] La multiplicacion de {num1} * {num2} es: ", num1 * num2)
    elif opcion==4:
        print(f"\n[/] La division de {num1} / {num2} es: ", num1 / num2)

    else:
        break




    

