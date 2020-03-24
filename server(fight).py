import socket  # import AF_INET, socket, SOCK_STREAM, gethostbyname, gethostname
from threading import Thread
import pickle
from character import Character
from update_position_and_animation import update_pos_and_anim
from update_character_img import update_img
from apply_damage import apply_damage


def accept_incoming_connections():  # новое подключение
    while True:
        client, client_address = SERVER.accept()
        print(f"Новый игрок {client_address}")
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    def send_char_info(fighter):
        broadcast(pickle.dumps([player_id, fighter.pos_x, fighter.pos_y, fighter.actual_coords_x, fighter.actual_coords_y,
                                fighter.helth, fighter.cur_anim, fighter.cur_frame, fighter.turn, fighter.block,
                                fighter.ducked]))

    player_id, side = client.recv(BUFSIZE).decode("utf8").split()
    if len(fighters) < 3:
        if fighters:
            fighter = Character('Sub-Zero', 'right', player_id)
        else:
            fighter = Character('Sub-Zero', 'left', player_id)
        fighters[client] = fighter
    else:
        return

    while len(fighters) < 2:
        pass

    for f in fighters.items():
        if f != fighter:
            enemy = f

    # MAIN GAME CYCLE
    while True:
        try:
            msg = client.recv(BUFSIZE)
            if msg != bytes("{quit}", "utf8"):
                try:
                    s = pickle.loads(msg)
                except pickle.UnpicklingError:
                    continue
                if s[0] == 'update':
                    fighter.vector = s[1]
                    fighter.attack = s[2]
                    fighter.ducked = s[3]
                    fighter.block = s[4]
                    fighter.previos_moves = s[5]
                    new_anim = update_pos_and_anim(fighter, enemy)
                elif s[0] == 'img update':
                    update_img(fighter, fighter.side)
                elif s[0] == 'attack':
                    apply_damage(enemy, s[1])
                send_char_info(fighter)
                # print(positions)
            else:
                print(f"{player_name} вышел из игры")
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                del positions[player_id]
                broadcast(bytes(f"del {player_id}", "utf8"))
                break
        except ConnectionResetError:
            break


def broadcast(msg):  # разослать сообщение всем клиентам
    for sock in clients:
        sock.send(msg)


clients = {}
fighters = {}

HOST = socket.gethostbyname(socket.gethostname())
PORT = 33000
BUFSIZE = 1024

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

if __name__ == "__main__":
    SERVER.listen(5)
    print("Ждем подключения...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
