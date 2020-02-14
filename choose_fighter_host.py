from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pygame
import pickle
import sys
import random
from load_image import load_image
import subprocess
import os


pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class ChooseFighterH:
    def __init__(self):
        self.chosen_button = None
        # COLOURS = (128, 128, 128), (204, 29, 0)
        self.buttons = [[[650, 525, 100, 25], 'Выход'],
                        [[650, 480, 100, 25], 'Готов']]
        self.heroes = [[[202, 372, 76], [200, 370, 81], 'Johny Cage', load_image('heroes\Johny Cage.png'), load_image('heroes\Johny Cage b.jpg')],
                       [[322, 372, 76], [320, 370, 81], 'Scorpion', load_image('heroes\Scorpion.png'), load_image('heroes\Scorpion b.jpg')],
                       [[442, 372, 76], [440, 370, 81], 'Sonya', load_image('heroes\Sonya.png'), load_image('heroes\Sonya b.jpg')],
                       [[562, 372, 76], [560, 370, 81], 'Liu Kang', load_image('heroes\Liu Kang.png'), load_image('heroes\Liu Kang b.jpg')],
                       [[682, 372, 76], [680, 370, 81], 'Sub-Zero', load_image('heroes\Sub-Zero.png'), load_image('heroes\Sub-Zero b.jpg')]]
        self.maps = [[[202, 482, 76], [200, 480, 81], "Courtyard", load_image('maps_avatar\Shang Tsung`s Courtyard.jpg')],
                     [[322, 482, 76], [320, 480, 81], 'Warrior Shrine', load_image('maps_avatar\Warrior Shrine.png')],
                     [[442, 482, 76], [440, 480, 81], 'Throne Room', load_image('maps_avatar\Shang Tsung`s Throne Room.jpg')]]
        self.other = [[[65, 380], 'Ваш'],
                      [[65, 415], 'герой'],
                      [[65, 490], 'Карта'],
                      [[65, 525], 'боя']]

        self.your_char = pygame.Surface([240, 240])
        self.your_char.fill((128, 128, 128))
        self.enemy_char = pygame.Surface([240, 240])
        self.enemy_char.fill((128, 128, 128))
        self.called_menu = None
        self.chosen_fighter = None
        self.enemys_fighter = None
        self.chosen_map = 'Courtyard'
        self.ready = False

    def draw(self):
        screen.fill(pygame.Color('black'))
        screen.blit(self.background, [0, 0])
        self.draw_heroes()
        self.draw_maps()
        self.draw_buttons()
        self.draw_other()

    def draw_maps(self):
        font = pygame.font.SysFont('RomanD', 16)
        for n, i in enumerate(self.maps):

            back = pygame.Surface([i[1][2], i[1][2]])
            back.fill([0, 0, 0])
            if i[2] == self.chosen_map:
                back.fill([128, 128, 128])
            if self.chosen_button == ['m', n]:
                back.fill([200, 0, 0])
            text = font.render(i[2], 0, [128, 128, 128])

            screen.blit(back, i[1][:2])
            screen.blit(text, [i[1][0], i[1][1] - 20])
            screen.blit(i[3], i[0][:2])

    def draw_heroes(self):
        font = pygame.font.SysFont('RomanD', 16)
        for n, i in enumerate(self.heroes):

            back = pygame.Surface([i[1][2], i[1][2]])
            back.fill([0, 0, 0])
            if i[2] == self.chosen_fighter:
                back.fill([128, 128, 128])
            if self.chosen_button == ['h', n]:
                back.fill([200, 0, 0])

            text = font.render(i[2], 0, [128, 128, 128])

            screen.blit(back, i[1][:2])
            screen.blit(text, [i[1][0], i[1][1] - 20])
            screen.blit(i[3], i[0][:2])
            screen.blit(self.your_char, [42, 42])
            screen.blit(self.enemy_char, [500, 42])

    def draw_buttons(self):
        font = pygame.font.SysFont('RomanD', 40)
        for n, i in enumerate(self.buttons):
            text = font.render(i[1], 0, [128, 128, 128])
            if self.chosen_button == ['b', n]:
                text = font.render(i[1], 0, [200, 0, 0])
            screen.blit(text, i[0])

    def draw_other(self):
        font = pygame.font.SysFont('RomanD', 40)
        for i in self.other:
            text = font.render(i[1], 0, [128, 128, 128])
            screen.blit(text, i[0])

    def clicked(self):
        if self.chosen_button is None:
            return None

        elif self.chosen_button[0] == 'h' and not self.ready:
            self.chosen_fighter = self.heroes[self.chosen_button[1]][2]
            self.your_char = pygame.Surface([240, 240])
            self.your_char.fill([128, 128, 128])
            self.your_char.blit(self.heroes[self.chosen_button[1]][4], [2, 2])

        elif self.chosen_button[0] == 'm' and not self.ready:
            self.chosen_map = self.maps[self.chosen_button[1]][2]

        elif self.chosen_button[0] == 'b':
            if self.chosen_button[1] == 0:
                self.client_socket.send(pickle.dumps(['exit']))
                return 'main'
            elif self.chosen_button[1] == 1:
                if self.ready:
                    self.buttons[1][1] = 'Готов'
                    self.ready = False
                else:
                    self.buttons[1][1] = 'Готов X'
                    self.ready = True

    def mark_chosen_button(self):
        mouse = pygame.mouse.get_pos()
        chosen = None
        for n, i in enumerate(self.buttons):
            if i[0][0] <= mouse[0] <= i[0][0] + i[0][2] and i[0][1] <= mouse[1] <= i[0][1] + i[0][3]:
                chosen = ['b', n]

        for n, i in enumerate(self.heroes):
            if i[1][0] <= mouse[0] <= i[1][0] + i[1][2] and i[1][1] <= mouse[1] <= i[1][1] + i[1][2]:
                chosen = ['h', n]

        for n, i in enumerate(self.maps):
            if i[1][0] <= mouse[0] <= i[1][0] + i[1][2] and i[1][1] <= mouse[1] <= i[1][1] + i[1][2]:
                chosen = ['m', n]

        self.chosen_button = chosen

    def run(self):

        def receive(self):
            while True:
                try:
                    msg = self.client_socket.recv(1024)
                    try:
                        info = pickle.loads(msg)
                        key = info[0]
                        if key == 'start fight':
                            self.called_menu = info[0]
                            self.info += [self.client_socket] + info[1]
                            print('sf', info[1])

                        elif key == 'not ready':
                            for h in self.heroes:
                                if h[2] == info[1] and h[2] != self.enemys_fighter:
                                    self.enemys_fighter = h[2]
                                    self.enemy_char = pygame.Surface([240, 240])
                                    self.enemy_char.fill((128, 128, 128))
                                    self.enemy_char.blit(pygame.transform.flip(h[4], True, False), [2, 2])

                        elif key == 'enemy disconnected':
                            self.enemys_fighter = None
                            self.enemy_char = pygame.Surface([240, 240])
                            self.enemy_char.fill((128, 128, 128))
                            self.enemy_char.blit(self.enemy_char, [2, 2])

                    except pickle.UnpicklingError:
                        continue
                except OSError:  # Possibly client has left the chat.
                    break

        os.startfile('start server.bat')

        HOST = "192.168.1.153"  # input('Enter host: ')
        PORT = 33000  # input('Enter port: ')
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        self.receive_thread = Thread(target=receive, args=(self, ))
        self.receive_thread.start()

        self.player_id = str(random.randint(1, 1000000))
        self.client_socket.send(bytes(f"{self.player_id} host", "utf8"))

        running = True
        self.called_menu = None
        self.info = []
        self.background = load_image(r"backgrounds\background.jpg")
        while running:

            self.mark_chosen_button()
            self.draw()

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    self.called_menu = self.clicked()

            if self.called_menu is not None:
                running = False
            self.client_socket.send(pickle.dumps([self.chosen_fighter, self.ready, self.chosen_map]))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return [self.called_menu, self.info]
