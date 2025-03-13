import socket

ip = input("Ingresa una IP: ")
try:
    dominio = socket.gethostbyaddr(ip)
    print(f"[+] El dominio asociado a {ip} es: {dominio[0]}")
except socket.herror:
    print("[!] No se encontró un dominio para esta IP.")
