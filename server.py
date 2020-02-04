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
    player_id, side = client.recv(BUFSIZE).decode("utf8").split()

    if len(PLAYERS) == 2:
        return
    # [id, chosen fighter, side, ready]
    PLAYERS[client] = Player(client, player_id, side)

    def broadcast(msg):  # разослать сообщение всем клиентам
        for f in PLAYERS:
            f.send(msg)

    def send_info_to_enemy(client, msg):
        for f in PLAYERS:
            if f != client:
                f.send(msg)

    def send_info_to_client(client, msg):
        for f in PLAYERS:
            if f == client:
                f.send(msg)

    def get_char_info(player, key):
        if key == 'start game':
            return [player.id, player.fighter, player.side]
        elif key == 'update_lobby':
            return [player.id, player.fighter]

    def start_game():
        global FIGHTER1
        global FIGHTER2
        fighters = [p for p in PLAYERS]
        FIGHTER1 = fighters[0]
        FIGHTER2 = fighters[1]
        broadcast(pickle.dumps([get_char_info(FIGHTER1, 'start game'), get_char_info(FIGHTER2, 'start game'), MAP]))

    global MAP
    global DISCONNECTING_PLAYER

    while not STOP_THREADS and not GAME_IS_ON:
        msg = client.recv(BUFSIZE)
        s = pickle.loads(msg)
        if s[0] == 'exit':
            if PLAYERS[client].side == 'left':
                send_info_to_enemy(client, pickle.dumps(['server is down']))
                STOP_THREADS = True
            else:
                DISCONNECTING_PLAYER = True
                send_info_to_enemy(client, pickle.dumps(['enemy disconnected']))
                return
        if DISCONNECTING_PLAYER and PLAYERS[client].side == 'left':
            print(PLAYERS)
            PLAYERS.popitem()
            DISCONNECTING_PLAYER = False
            print(PLAYERS)

        PLAYERS[client].fighter = s[0]
        PLAYERS[client].ready = s[1]
        if len(s) == 3:
            MAP = s[2]
        ready = [p.ready for p in PLAYERS.values()]
        if len(ready) == 2:
            if GAME_IS_ON:
                break
            if ready[0] and ready[1]:
                GAME_IS_ON = True
                info = ['start fight', [f[:3] for f in PLAYERS.values()]]
                broadcast(pickle.dumps(info))
                break
            else:
                info = ['not ready', [get_char_info(f, 'update_lobby') for f in PLAYERS.values()]]
                broadcast(pickle.dumps(info))

    return


def execute():
    print(1)
    os.system("taskkill /F /PID " + str(os.getppid()))


class Player:
    def __init__(self, client, id, side):
        self.client = client
        self.id = id
        self.side = side
        self.ready = False
        self.fighter = ''
        self.pos = []
        self.actual_pos = []
        self.cur_anim = ''
        self.cur_frame = 0
        self.frame_time = 0
        self.damage = 0
        self.on_ground = True
        self.getting_damage = False
        self.attacking = False
        self.hit = False

PLAYERS = {}
FIGHTER1 = None
FIGHTER2 = None
GAME_IS_ON = False
MAP = None
DISCONNECTING_PLAYER = None

HOST = ''
PORT = 33000
BUFSIZE = 1024

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
