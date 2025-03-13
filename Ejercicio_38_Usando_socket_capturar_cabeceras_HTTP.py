import socket

host = input("Ingrese una dirección web (por ejemplo, google.com): ")

try:
    ip = socket.gethostbyname(host)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 80))

    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())  

    respuesta = sock.recv(4096)
    print(respuesta.decode())

    sock.close()

except Exception as e:
    print(f"[!] Error: {e}")
