import socket
import re
import concurrent.futures  # Para usar hilos y acelerar el escaneo

# Función para validar la IP ingresada
def obtener_ip():
    while True:
        ip = input("Ingresa una dirección IP: ")
        if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip):
            partes = ip.split(".")
            if all(0 <= int(p) <= 255 for p in partes):
                return ip
        print("[!] Dirección IP no válida. Inténtalo de nuevo.")

# Función para intentar conectar y verificar puertos abiertos
def escanear_puerto(ip, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        if sock.connect_ex((ip, puerto)) == 0:
            try:
                sock.send(b"Hello\r\n")  # Intento de banner grabbing
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No se pudo obtener información"
            print(f"[+] Puerto abierto: {puerto} | {banner}")
            return puerto
    return None

# Función para escanear puertos en paralelo
def escanear_puertos(ip):
    print(f"[+] Escaneando puertos en {ip}...")
    puertos_abiertos = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        resultados = executor.map(lambda p: escanear_puerto(ip, p), range(1, 1025))
    
    for puerto in resultados:
        if puerto:
            puertos_abiertos.append(puerto)

    if not puertos_abiertos:
        print("[!] No se encontraron puertos abiertos.")
    else:
        print(f"[+] Puertos abiertos: {puertos_abiertos}")

# Ejecutar el escaneo
ip_objetivo = obtener_ip()
escanear_puertos(ip_objetivo)
