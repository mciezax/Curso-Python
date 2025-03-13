    
    
while True:
    try:
        n1=float(input("Ingresa un numero: "))
        n2=float(input("Ingresa un numero: "))
    except ValueError:
        print("Error, Ingresa un numero valido")
        continue    

    if n1 > n2:
        print(f"{n1} es mayor que {n2}")
    elif n2 > n1:
        print(f"{n2} es mayor que {n1}")
    else:
        print(f"{n1} y {n2} son iguales")    

    break        