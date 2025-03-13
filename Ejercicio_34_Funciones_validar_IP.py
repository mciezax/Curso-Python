import re

def obtener_ip():
    while True:
        ip = input("Ingresa una dirección IP: ")
        # Expresión regular para validar IPv4
        if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip):
            partes = ip.split(".")
            if all(0 <= int(p) <= 255 for p in partes):
                return ip
        print("Dirección IP no válida. Inténtalo de nuevo.")

# Llamamos a la función
ip_objetivo = obtener_ip()
print("IP válida:", ip_objetivo)
