from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pickle
import os
import sys


def accept_incoming_connections():  # новое подключение
    while True:
        client, client_address = SERVER.accept()
        print(f"Новый игрок {client_address}")
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    player_id, side = client.recv(BUFSIZE).decode("utf8").split()

    if len(fighters) == 2:
        return
    # [id, chosen fighter, side, ready]
    fighters[client] = [player_id, '', side, False]

    global game_is_on
    global map_name

    while True:
        print(fighters)
        msg = client.recv(BUFSIZE)
        s = pickle.loads(msg)
        if s[0] == 'exit':

            if fighters[client][2] == 'left':
                execute()
            else:
                del fighters[client]
                break
        fighters[client][1] = s[0]
        fighters[client][3] = s[1]
        if len(s) == 3:
            map_name = s[2]
        ready = [c[3] for c in fighters.values()]
        if len(ready) == 2:
            if game_is_on:
                break
            if ready[0] and ready[1]:
                game_is_on = True
                info = ['start fight', [f[:3] for f in fighters.values()]]
                broadcast(pickle.dumps(info))
                break
            else:
                info = ['not ready', [f[:2] for f in fighters.values()]]
                broadcast(pickle.dumps(info))
    return


def broadcast(msg):  # разослать сообщение всем клиентам
    for sock in fighters:
        sock.send(msg)


def execute():
    os.system("taskkill /F /PID " + str(os.getppid()))

fighters = {}
game_is_on = False
map_name = None

HOST = ''
PORT = 33000
BUFSIZE = 1024

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

if __name__ == "__main__":
    SERVER.listen(5)
    print("Ждем подключения...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    print(23)
    ACCEPT_THREAD.join()
    print(76)
    SERVER.close()
