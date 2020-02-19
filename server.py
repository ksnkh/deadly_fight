from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pickle
import os


def accept_incoming_connections():  # новое подключение
    while not STOP_THREADS:
        client, client_address = SERVER.accept()
        print(f"Новый игрок {client_address}")
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    global STOP_THREADS
    global GAME_IS_ON
    global HOST_PLAYER
    global CLIENT_PLAYER
    player_id, status = client.recv(1024).decode("utf8").split()

    if HOST_PLAYER is not None and CLIENT_PLAYER is not None:
        return

    # [client, id, chosen fighter, ready]
    player = Player(client, player_id, status)
    if status == 'host':
        HOST_PLAYER = player
    elif status == 'client':
        CLIENT_PLAYER = player

    def broadcast(info):  # разослать сообщение всем клиентам
        send_info_to_host_player(info)
        send_info_to_client_player(info)

    def send_info_to_client_player(info):
        if CLIENT_PLAYER is not None:
            CLIENT_PLAYER.client.send(pickle.dumps(info))

    def send_info_to_host_player(info):
        HOST_PLAYER.client.send(pickle.dumps(info))

    def send_info_to_enemy(info):
        if status == 'host':
            send_info_to_client_player(info)
        elif status == 'client':
            send_info_to_host_player(info)

    def get_char_info(player, key):
        if key == 'update lobby':
            return [player.fighter_name]
        elif key == 'start fight':
            return [player.fighter_name, player.side]


    def start_fight():
        global GAME_IS_ON
        GAME_IS_ON = True
        send_info_to_host_player(['start fight',
                                  [get_char_info(HOST_PLAYER, 'start fight') + [CLIENT_PLAYER.fighter_name, MAP]]])
        send_info_to_client_player(['start fight',
                                    [get_char_info(CLIENT_PLAYER, 'start fight') + [HOST_PLAYER.fighter_name, MAP]]])

    global MAP

    # LOBBY CYCLE
    while not STOP_THREADS and not GAME_IS_ON:
        msg = client.recv(1024)
        s = pickle.loads(msg)
        if s[0] == 'exit':
            if status == 'host':
                send_info_to_client_player(['server is down'])
                STOP_THREADS = True
            else:
                send_info_to_host_player(['enemy disconnected'])
                CLIENT_PLAYER = None
                return

        player.fighter_name = s[0]
        player.ready = s[1]
        if player.status == 'host':
            MAP = s[2]
        if CLIENT_PLAYER is not None:
            if HOST_PLAYER.ready and CLIENT_PLAYER.ready:
                if GAME_IS_ON:
                    break
                else:
                    start_fight()
            else:
                send_info_to_enemy(['not ready'] + get_char_info(player, 'update lobby'))


    # GAME CYCLE
    while not STOP_THREADS:
        msg = client.recv(1024)
        s = pickle.loads(msg)

        if s[0] == 'end game':
            broadcast(['end game'])
            STOP_THREADS = True
        elif s[0] == 'exit':
            send_info_to_enemy(['end game'])
            STOP_THREADS = True
        elif s[0] == 'geting damage':
            if status == 'host':
                CLIENT_PLAYER.attack = []
            elif status == 'client':
                HOST_PLAYER.attack = []
        else:
            if 'hit' in s[0]:
                player.attack = s[-1]
            elif player.attack != []:
                s.append(player.attack.copy())
                s[0] += ' hit'

            send_info_to_enemy(s)


def execute():
    os.system("taskkill /F /PID " + str(os.getppid()))


class Player:
    def __init__(self, client, id, status):
        self.client = client
        self.id = id
        self.status = status
        self.ready = False
        self.fighter_name = ''
        if status == 'host':
            self.side = 'left'
        else:
            self.side = 'right'
        self.attack = []


HOST_PLAYER = None
CLIENT_PLAYER = None
GAME_IS_ON = False
MAP = None

HOST = ''
PORT = 33000

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

if __name__ == "__main__":
    SERVER.listen(1)
    print("Ждем подключения...")
    STOP_THREADS = False
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    while not STOP_THREADS:
        pass
    print('join on')
    SERVER.close()
    execute()
