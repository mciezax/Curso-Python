import socket

dominio = input("Ingresa un dominio por ejemplo google.com: ")
ip = socket.gethostbyname(dominio)

print(f"[+] La IP de {dominio} es: {ip}")
