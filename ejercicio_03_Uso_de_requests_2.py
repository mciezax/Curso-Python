import requests


def verificar_sitio(sitio):

    if not sitio.startswith(("http://", "https://")):
        sitio = "http://" + sitio

    try:
        response = requests.get(sitio, timeout=5)

        if response.status_code == 200:
            print(f"El sitio '{sitio}' esta activo (Codigo:{response.status_code}).")

        else:
            print(f"El sitio '{sitio}' respondio con estado: {response.status_code}, podria estar inactivo.")

    except requests.exceptions.RequestException as e:
        print(f"Error al intentar acceder a '{sitio}':{e}")


print("\n verificar si un sitio web esta activo")

sitio=input("Ingresa la direccion( ejemplo: www.google.com o https://www.google.com):").strip()

verificar_sitio(sitio)


