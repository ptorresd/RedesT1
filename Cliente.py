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
        print('conectando a: ' + s["nombre"])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((s["dirección"], int(s["puerto"])))
        sockets[s["nombre"]] = sock
        print('conectado')
        threading.Thread(target=wait_for_answer, args=[s["nombre"]]).start()


##funciones para procesar los comandos de consola
def receive_command(comando, destinatarios):
    dest = destinatarios.split(' ')

    if (dest[0] == 'all'):
        for socket in sockets:
            send_command(socket, comando)
        return

    for i in range(len(dest)):
        send_command(dest[i], comando)


def send_command(server_name, command):
    print('enviando comando a ' + server_name)
    sockets[server_name].send(bytes(command, 'utf-8'))
    if(command == 'exit'):
        del sockets[server_name]
        return
    threading.Thread(target=wait_for_answer, args=[server_name]).start()


def wait_for_answer(server_name):
    socket = sockets[server_name]
    print('esperandorespuesta')
    while (True):
        ans = codecs.decode(socket.recv(4096))
        if (ans != ''):
            print('respuesta de ' + server_name + ': ' + ans)
        return


##MAIN EMPIEZA AQUI

if len(sys.argv) == 2:
    parse_json(sys.argv[1])

else:
    for i in range(1, len(sys.argv), 3):
        print('conectando a: ' + sys.argv[i])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[i + 1], int(sys.argv[i + 2])))
        sockets[sys.argv[i]] = sock
        threading.Thread(target=wait_for_answer, args=[sys.argv[i]]).start()
        print('conectado')

while True:
    command = input()
    dest = input('ingrese destinatarios: ')
    receive_command(command, dest)
