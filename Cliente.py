# -*- coding: utf-8 -*-

import socket
import json
import sys
import threading
import codecs

sockets = {}


# lee los elementos del json
def parse_json(file):
    f = open(file)
    data = json.load(f)

    for s in data:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], int(s["puerto"])))
        sockets[s["nombre"]] = sock
        print(sock.recv(4096))


##funciones para procesar los comandos de consola
def receive_command(comando):
    c = comando.split(' ')
    com = c[0]

    if (c[1] == 'all'):
        for socket in sockets:
            send_command(socket, com)
        return

    for i in range(1, len(c)):
        send_command(c[i], com)


def send_command(server_name, command):
    sockets[server_name].send(bytes(command, 'utf-8'))
    threading.Thread(target=wait_for_answer, args=[sockets[server_name]]).start()


def wait_for_answer(socket):
    print('esperandorespuesta')
    ans = socket.recv(4096)
    print(ans)


#    while(True):
#       ans = socket.recv(4096)
#      if(ans!=''):
#         print(ans)
#        return


##MAIN EMPIEZA AQUI

if len(sys.argv) == 2:
    parse_json(sys.argv[1])

else:
    for i in range(1, len(sys.argv), 3):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[i + 1], sys.argv[i + 2]))
        sockets[sys.argv[i]] = sock
        sock.recv(4096)



while True:
    command = input()
    receive_command(command)
