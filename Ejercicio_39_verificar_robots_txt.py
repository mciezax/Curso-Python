import requests

def verificar_robots_txt(url):
    if not url.startswith("http"):
        url = "http://" + url  # Agregar http si el usuario no lo escribe

    robots_url = url.rstrip("/") + "/robots.txt"

    try:
        respuesta = requests.get(robots_url, timeout=5)

        if respuesta.status_code == 200:
            print(f"\n[+] Encontrado: {robots_url}\n")
            print(respuesta.text)  # Muestra el contenido del archivo
        elif respuesta.status_code == 403:
            print(f"[!] Acceso denegado a {robots_url} (403 Forbidden)")
        else:
            print(f"[-] No se encontró robots.txt en {url} (Código: {respuesta.status_code})")

    except requests.RequestException as e:
        print(f"[!] Error al conectar con {url}: {e}")

# Solicitar URL al usuario
sitio = input("Ingrese la URL del sitio web (sin /robots.txt ): ")
verificar_robots_txt(sitio)
