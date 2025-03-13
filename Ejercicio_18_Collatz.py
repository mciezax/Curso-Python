numero=int(input("Ingrese un numero: "))
pasos = 0
if numero > -9999999 and numero != 0:

    c0 = numero

    while  c0 != 1:

        pasos += 1
        if c0 % 2 == 0:
            c0 = c0 // 2

        else:
            
            c0 = 3 * c0 + 1

        
        print(c0)
    print (f"pasos = {pasos}")
else:
    print("Número fuera del rango válido.")



    

    




