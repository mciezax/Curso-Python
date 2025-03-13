def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()        # Usa el valor predeterminado
saludar("Luis")  # Usa el argumento proporcionado

# Explicación:

# nombre="amigo" establece un valor por defecto.
# saludar() usa "amigo", pero saludar("Luis") usa "Luis".