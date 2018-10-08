# -*- coding: utf-8 -*-
import socket
import time
import random
import sys

# armamos el socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lo conectamos al server
if (len(sys.argv) == 1):
    serversocket.bind(('localhost', 8085))
else:
    serversocket.bind(('localhost', int(sys.argv[1])))

# hacemos que sea un server socket y le decimos que tenga a lo mas 5 conexiones
serversocket.listen(5)

# nos quedamos esperando como buen server
connection, address = serversocket.accept()
print('conectado')
connection.send(bytes('conectado', 'utf-8'))

while True:
    # sacamos los datitos de la conexion entrante (objeto, direccion)
    # sacamos los datos. Aca 64 es el tamaño máximo del buffer
    print('esperando mensaje')
    buf = connection.recv(4096)
    if len(buf) > 0:
        # mostramos lo que nos llegó y salimos del loop
        print('mensaje recibido')
        time.sleep(random.randint(1, 10))
        connection.send(buf)
