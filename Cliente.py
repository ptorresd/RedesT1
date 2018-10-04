# -*- coding: utf-8 -*-

import socket
import json
import sys

sockets = {}

# lee los elementos del json
def parse_input():
    f = open('data.json')
    data = json.load(f)

    for s in data:
        print(s)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], s["puerto"]))
        sockets[s["nombre"]] = sock

def parse_json(file):
    f = open(file)
    data = json.load(f)

    for s in data:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], s["puerto"]))
        sockets[s["nombre"]] = sock

##funciones para procesar los comandos de consola
def receive_command(comando):
    c = comando.split(' ')
    com = c[0]

    if (c[1] == 'all'):
        for socket in sockets:
            send_command(socket, com)
        return

    for socket in range(1, len(c)):
        send_command(socket, com)


def send_command(server_name, command):
    sockets[server_name].send(bytes(command, 'utf-8'))
    wait_for_answer()

def wait_for_answer():
    pass


##MAIN EMPIEZA AQUI

if len(sys.argv)==2:
    parse_json(sys.argv[1])

else:
    for i in range(1,len(sys.argv),3):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[i+1], sys.argv[i+2]))
        sockets[sys.argv[i]] = sock
