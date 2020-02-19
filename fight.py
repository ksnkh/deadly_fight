import pygame
from background import Background
from character import Character
from camera import Camera
from camera_focus import CameraFocus
from game_cycle import game_cycle
from helth_bar import HelthBar
from attack_list import AttackExecution
import pickle
from threading import Thread
from change_fighter_position import change_position
from apply_damage import apply_damage
from turn_frame import turn_frame

size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Fight:
    def __init__(self, data):
        # data = [socket, [fighter name, fighter side, enemy fighter name, map]]
        self.client_socket = data[0]

        self.your_char = data[1][0]
        self.fighter_side = data[1][1]
        self.enemy_char = data[1][2]
        self.map_name = data[1][3]

    def run(self):
        def receive(self):
            while True:
                try:
                    msg = self.client_socket.recv(1024)
                    try:
                        info = pickle.loads(msg)
                        key = info[0]
                        print(info)
                        if key == 'end game':
                            self.running = False
                        else:
                            change_position(self.enemy, [info[1] - self.enemy.actual_coords_x, info[2] - self.enemy.actual_coords_y], 'all')
                            if self.enemy.cur_anim != info[3]:
                                self.enemy.set_anim(info[3])
                            self.enemy.helth = info[4]
                            self.enemy.side = info[7]
                            if info[6]:
                                self.enemy.image = pygame.transform.flip(self.enemy.frames[info[5]], True, False)
                            else:
                                self.enemy.image = self.enemy.frames[info[5]]

                            self.enemy.rect.width = info[8]
                            self.enemy.rect.height = info[9]

                            if self.char.side == 'right':
                                self.cf.update(
                                    self.char.actual_coords_x + self.char.rect.width,
                                    self.enemy.actual_coords_x)
                            else:
                                self.cf.update(self.char.actual_coords_x,
                                                         self.enemy.actual_coords_x + self.enemy.rect.width)

                            if 'hit' in key:
                                apply_damage(self.char, info[10])
                                self.client_socket.send(pickle.dumps(['geting damage']))

                    except pickle.UnpicklingError:
                        print('unpikling error')
                        continue
                except OSError:  # Possibly client has left the chat.
                    break
        self.screen = screen

        # CREATING SPRITE GROUPS
        self.all_sprites = pygame.sprite.Group()
        self.fighters = pygame.sprite.Group()
        self.bground = pygame.sprite.Group()
        self.cfg = pygame.sprite.Group()
        self.helth_bars = pygame.sprite.Group()
        self.alg = pygame.sprite.Group()

        # CREATING SPRITES
        self.bgr = Background(f"maps/{self.map_name}.png", self.all_sprites, self.bground)
        self.cf = CameraFocus(self.cfg)
        if self.fighter_side == 'right':
            self.enemy = Character(self.enemy_char, 'left', self.fighters, self.all_sprites)
            self.char = Character(self.your_char, 'right', self.fighters, self.all_sprites)
        else:
            self.char = Character(self.your_char, 'left', self.fighters, self.all_sprites)
            self.enemy = Character(self.enemy_char, 'right', self.fighters, self.all_sprites)
        self.chb = HelthBar(self.char, self.helth_bars)
        self.ehb = HelthBar(self.enemy, self.helth_bars)
        self.camera = Camera(self.cf)
        self.al = AttackExecution(self.your_char, self.alg)
        self.running = True

        self.receive_thread = Thread(target=receive, args=(self, ))
        self.receive_thread.start()

        # game cycle
        game_cycle(self)
        print('game endedddddddddddd')
        screen.fill(pygame.Color('black'))
        return ['main']
