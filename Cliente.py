# -*- coding: utf-8 -*-

import socket
import json
import sys

sockets = {}

def parse_json(file):
    f = open(file)
    data = json.load(f)

    for s in data:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], s["puerto"]))
        sockets[s["nombre"]] = sock


if len(sys.argv)==2:
    parse_json(sys.argv[1])

else:
    for i in range(1,len(sys.argv),3):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[i+1], sys.argv[i+2]))
        sockets[sys.argv[i]] = sock


# armamos el socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lo conectamos al puerto acordado
clientsocket.connect(('localhost', 8086))

# mandamos un mensajito
print("mandamos cositas...")
clientsocket.send('Holi c:')
print("enviado")
