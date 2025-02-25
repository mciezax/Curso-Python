import requests

print("Verificar si un sitio web está activo")
sitio = input("Ingresa la dirección (ejemplo: http://www.google.com): ")

try:
    response = requests.get(sitio)

    if response.status_code == 200:
        print("Sitio activo")
    else:
        print("Sitio inactivo")

except requests.exceptions.RequestException:
    print("Error al intentar acceder al sitio")

