# -*- coding: utf-8 -*-

import socket
import json
import sys

sockets = {}

def parse_input():

    f=open('data.json')
    data = json.load(f)

    for s in data:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], s["puerto"]))
        sockets[s["nombre"]]=sock


# armamos el socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lo conectamos al puerto acordado
clientsocket.connect(('localhost', 8086))

# mandamos un mensajito
print("mandamos cositas...")
clientsocket.send('Holi c:')
print("enviado")
