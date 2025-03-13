import requests

def detectar_wordpress(url):
    if not url.startswith("http"):
        url = "http://" + url  # Agregar http si el usuario no lo escribe

    # Posibles URLs que revelan WordPress
    urls_wordpress = [
        "/wp-login.php",         
        "/wp-admin/",           
        "/wp-content/",          
        "/wp-includes/",         
        "/readme.html",           
        "/wp-json/wp/v2/",
        "/wp2/"
    ]

    print(f"\n[+] Verificando si {url} usa WordPress...\n")

    for path in urls_wordpress:
        full_url = url.rstrip("/") + path

        try:
            respuesta = requests.get(full_url, timeout=5)

            if respuesta.status_code == 200:
                print(f"[+] {full_url} encontrado (Código: 200) ✅ - Podría ser WordPress")
            elif respuesta.status_code == 403:
                print(f"[!] {full_url} restringido (Código: 403) 🚧 - Podría ser WordPress")
        except requests.RequestException:
            print(f"[-] No se pudo conectar a {full_url}")

# Solicitar URL
sitio = input("Ingrese la URL del sitio web: ")
detectar_wordpress(sitio)
