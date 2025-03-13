import time
abecedario=["a", "z" ,"j" ,"b" ,"q" ,"e" ,"r", "t", "y","c", "u", "i", "o", "p", "x", "s", "d", "f", "g", "h", "v", "k" ,"l", "m", "n", "w"]

cambio =True

while cambio:
    cambio = False
    
    for i in range (len(abecedario) - 1):
        if abecedario[i] > abecedario[i + 1]:
            cambio = True
            abecedario[i], abecedario[i + 1] = abecedario[i + 1], abecedario[i]
            
   
print("\nLista ordenada:", "".join(abecedario))


    
