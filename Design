import pygame
import sys
import os
import time
import random

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()

settings = {'music': 1, 'sound': 1}
hero_creator = 'джонни'
hero_guest = 'джонни'
main_map = ''


class Music:
    def __init__(self):
        self.on = True
        # pygame.mixer.music.load('music.mp3')

    def play(self):
        # pygame.mixer.music.play(-1)
        pass

    def not_play(self):
        # pygame.mixer.music.pause()
        pass


class Music_Flex:
    def __init__(self):
        self.on = True
        pygame.mixer.music.load('flex.mp3')

    def play(self):
        pygame.mixer.music.play(-1)

    def not_play(self):
        pygame.mixer.music.pause()


class Sound:
    def __init__(self):
        self.on = True

    def play(self, file_name):
        sound1 = pygame.mixer.Sound(file_name)
        if self.on:
            sound1.play()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


# В main_menu добавляются ф-ии меню, которые могут быть открыты
# Вместо game потом надо добавить select_character
class MainMenu:
    def __init__(self):
        self.paragraph = 0
        self.points = [(40, 100, 'Подключиться к серверу', (128, 128, 128), (210, 50, 0), 0),
                       (40, 200, 'Создать сервер', (128, 128, 128), (204, 29, 0), 1),
                       (40, 300, 'Настройки', (128, 128, 128), (204, 29, 0), 2),
                       (40, 400, 'Выход', (128, 128, 128), (204, 29, 0), 3)]
        self.font = pygame.font.SysFont(None, 30)
        self.called_menu = None

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph_number):
        if paragraph_number == 0:
            return 'connect to server'
        elif paragraph_number == 1:
            return 'fight'
        elif paragraph_number == 2:
            return 'settings'
        elif paragraph_number == 3:
            sys.exit()

    def run(self):
        image_6 = pygame.image.load('он_скорпион3.jpg')
        screen.blit(image_6, (90, 60))
        running = True
        font = pygame.font.SysFont('ToughSansRegular', 30)
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    self.paragraph = i[5]
            self.drawing(screen, font, self.paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                    if i.key == pygame.K_UP:
                        self.paragraph = (self.paragraph - 1) % 4
                    if i.key == pygame.K_DOWN:
                        self.paragraph = (self.paragraph + 1) % 4
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(self.paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


keyboard = {'113': 'Q',
            '119': 'W',
            '101': 'E',
            '114': 'R',
            '116': 'T',
            '121': 'Y',
            '117': 'U',
            '105': 'I',
            '111': 'O',
            '112': 'P',
            '97': 'A',
            '115': 'S',
            '100': 'D',
            '102': 'F',
            '103': 'G',
            '104': 'H',
            '106': 'J',
            '107': 'K',
            '108': 'L',
            '122': 'Z',
            '120': 'X',
            '99': 'C',
            '118': 'V',
            '98': 'B',
            '110': 'N',
            '109': 'M',
            '49': '1',
            '50': '2',
            '51': '3',
            '52': '4',
            '53': '5',
            '54': '6',
            '55': '7',
            '56': '8',
            '57': '9',
            '48': '0',
            '301': 'CAPS LOCK',
            '304': 'SHIFT_L',
            '306': 'CTRL',
            '308': 'ALT',
            '32': 'SPACE',
            '282': 'F1',
            '283': 'F2',
            '284': 'F3',
            '285': 'F4',
            '286': 'F5',
            '287': 'F6',
            '288': 'F7',
            '289': 'F8',
            '290': 'F9',
            '291': 'F10',
            '292': 'F11',
            '293': 'F12',
            '305': 'CTRL',
            '8': 'BACKSPACE',
            '13': 'ENTER',
            '303': 'SHIFT_R',
            '273': 'ARROW_UP',
            '274': 'ARROW_DN',
            '275': 'ARROW_R',
            '276': 'ARROW_L'}

control = {'ВВЕРХ': 'W',
           'ВНИЗ': 'S',
           'ВЛЕВО': 'A',
           'ВПРАВО': 'D',
           'УДАР': 'Y',
           'СИЛЬНЫЙ УДАР': 'U',
           'УДАР НОГОЙ': 'I',
           'СИЛЬНЫЙ УДАР НОГОЙ': 'O',
           'ПРЫЖОК': 'SPACE',
           'X-RAY': 'T',
           'ПАУЗА': 'P'}

setting_music = ['Музыка: вкл',
                 'Звуки: вкл']

gold_egg = '0'


class Settings:
    def __init__(self, music_class, sound_class):
        global setting_music
        self.gold_egg = ''
        self.paragraph = 0
        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), (210, 50, 0), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), (210, 50, 0), 1],
                       (30, 260, 'Назад', (128, 128, 128), (210, 50, 0), 2),
                       (420, 35, 'Управление', (240, 240, 240), (240, 240, 240), 3),
                       [350, 100, 'ВВЕРХ', (128, 128, 128), (210, 50, 0), 3],
                       (350, 140, 'ВНИЗ', (128, 128, 128), (210, 50, 0), 4),
                       (350, 180, 'ВЛЕВО', (128, 128, 128), (210, 50, 0), 5),
                       (350, 220, 'ВПРАВО', (128, 128, 128), (210, 50, 0), 6),
                       (350, 260, 'УДАР', (128, 128, 128), (210, 50, 0), 7),
                       (350, 300, 'СИЛ.УДАР', (128, 128, 128), (210, 50, 0), 8),
                       (350, 340, 'УДАР НОГОЙ', (128, 128, 128), (210, 50, 0), 9),
                       (350, 380, 'СИЛ.УДАР НОГОЙ', (128, 128, 128), (210, 50, 0), 10),
                       (350, 420, 'ПРЫЖОК', (128, 128, 128), (210, 50, 0), 11),
                       [620, 100, control['ВВЕРХ'], (128, 128, 128), (210, 50, 0), 3],
                       [620, 140, control['ВНИЗ'], (128, 128, 128), (210, 50, 0), 4],
                       [620, 180, control['ВЛЕВО'], (128, 128, 128), (210, 50, 0), 5],
                       [620, 220, control['ВПРАВО'], (128, 128, 128), (210, 50, 0), 6],
                       [620, 260, control['УДАР'], (128, 128, 128), (210, 50, 0), 7],
                       [620, 300, control['СИЛЬНЫЙ УДАР'], (128, 128, 128), (210, 50, 0), 8],
                       [620, 340, control['УДАР НОГОЙ'], (128, 128, 128), (210, 50, 0), 9],
                       [620, 380, control['СИЛЬНЫЙ УДАР НОГОЙ'], (128, 128, 128), (210, 50, 0), 10],
                       [620, 420, control['ПРЫЖОК'], (128, 128, 128), (210, 50, 0), 11]]
        self.music_class = music_class
        self.sound_class = sound_class

    def clicked(self, paragraph_number):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        print(self.gold_egg)
        # if paragraph_number == 2 and self.gold_egg == 'CREATORS3':
        if paragraph_number == 2 and self.gold_egg == 'CREATORS3':
            print('egg')
            return 'legendary_egg'
        elif paragraph_number == 2:
            return 'main'
        elif paragraph_number == 0:
            if self.music_class.on:
                self.music_class.not_play()
                self.music_class.on = False
                self.points[0][2] = 'Музыка: выкл'
            else:
                self.music_class.play()
                self.music_class.on = True
                self.points[0][2] = 'Музыка: вкл'
            self.drawing(screen, font, self.paragraph)
        elif paragraph_number == 1:
            if self.sound_class.on:
                self.sound_class.on = False
                self.points[1][2] = 'Звуки: выкл'
            else:
                self.sound_class.on = True
                self.points[1][2] = 'Звуки: вкл'
        # УПРАВЛЕНИЕ
        elif paragraph_number == 3:
            self.change(3)
        elif paragraph_number == 4:
            self.change(4)
        elif paragraph_number == 5:
            self.change(5)
        elif paragraph_number == 6:
            self.change(6)
        elif paragraph_number == 7:
            self.change(7)
        elif paragraph_number == 8:
            self.change(8)
        elif paragraph_number == 9:
            self.change(9)
        elif paragraph_number == 10:
            self.change(10)
        elif paragraph_number == 11:
            self.change(11)

    def change(self, set):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        oops = True
        screen.blit(font.render(self.points[set + 10][2], 2, (240, 200, 200)),
                    (self.points[set + 10][0], self.points[set + 10][1]))
        pygame.display.flip()
        a = 0
        self.gold_egg = ''
        while oops:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    key = i.key
                    control[self.points[set + 1][2]] = str(key)
                    for i in self.points:
                        if i == self.points[set + 10]:
                            if str(key) in keyboard:
                                i[2] = keyboard[str(key)]
                            else:
                                i[2] = str(key)
                    for i in range(13, 22):
                        self.gold_egg += self.points[i][2]
                    oops = False

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if i != self.points[3]:
                if number_point == i[5]:
                    surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            else:
                if number_point == i[5]:
                    surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
                else:
                    surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def run(self):
        image_5 = pygame.image.load('чёрныйфон.jpg')
        screen.blit(image_5, (0, 0))
        font = pygame.font.SysFont('mr_AfronikG', 38)
        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    self.paragraph = i[5]
            self.drawing(screen, font, self.paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        self.paragraph = (self.paragraph - 1) % 12
                    if i.key == pygame.K_DOWN:
                        self.paragraph = (self.paragraph + 1) % 12
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(self.paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


class Fight:
    def __init__(self):
        global main_map
        global hero_creator
        self.paragraph = 0
        self.points = [(65, 380, 'Ваш', (128, 128, 128), (204, 29, 0), 0),
                       (65, 415, 'герой', (128, 128, 128), (204, 29, 0), 0),
                       (65, 490, 'Карта', (128, 128, 128), (204, 29, 0), 1),
                       (65, 525, 'боя', (128, 128, 128), (204, 29, 0), 1),
                       (650, 525, 'Выход', (128, 128, 128), (204, 29, 0), 2)]
        self.heroes = [(185, 347, 'Джонни Кейдж', (128, 128, 128), (204, 29, 0), 0),
                       (322, 347, 'Скорпион', (128, 128, 128), (204, 29, 0), 1),
                       (433, 347, 'Соня Блейд', (128, 128, 128), (204, 29, 0), 2),
                       (568, 347, 'Лю Кан', (128, 128, 128), (204, 29, 0), 3),
                       (681, 347, 'Саб-зиро', (128, 128, 128), (204, 29, 0), 4)]
        self.rects = [('1', (200, 370, 81, 81), (128, 128, 128), (204, 29, 0), 0),
                      ('2', (320, 370, 81, 81), (128, 128, 128), (204, 29, 0), 1),
                      ('3', (440, 370, 81, 81), (128, 128, 128), (204, 29, 0), 2),
                      ('4', (560, 370, 81, 81), (128, 128, 128), (204, 29, 0), 3),
                      ('5', (680, 370, 81, 81), (128, 128, 128), (204, 29, 0), 4)]
        self.maps = [(192, 567, 'Храм воина', (128, 128, 128), (204, 29, 0), 0),
                     (334, 567, 'Китай', (128, 128, 128), (204, 29, 0), 1),
                     (433, 567, 'Подземелье', (128, 128, 128), (204, 29, 0), 2)]
        self.rects_maps = [('1', (200, 480, 81, 81), (128, 128, 128), (204, 29, 0), 0),
                           ('2', (320, 480, 81, 81), (128, 128, 128), (204, 29, 0), 1),
                           ('3', (440, 480, 81, 81), (128, 128, 128), (204, 29, 0), 2)]
        self.player_1 = pygame.image.load('джони_бой.jpg')
        self.called_menu = None

    def drawing(self, surface, font_menu, number_point):
        pygame.draw.rect(surface, (255, 255, 255), (40, 40, 240, 240), 3)
        pygame.draw.rect(surface, (255, 255, 255), (520, 40, 240, 240), 3)
        for i in range(5):
            pygame.draw.rect(surface, self.rects[i][2], self.rects[i][1], 3)
        for i in range(3):
            pygame.draw.rect(surface, self.rects_maps[i][2], self.rects_maps[i][1], 3)
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        for i in self.heroes:
            font_menu = pygame.font.SysFont('RomanD', 14)
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        for i in self.maps:
            font_menu = pygame.font.SysFont('RomanD', 14)
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph_number):
        font = pygame.font.SysFont('mr_AfronikG', 40)
        oops = True
        if paragraph_number == 0:
            while oops:
                mouse = pygame.mouse.get_pos()
                for i in self.heroes:
                    # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                    if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 150:
                        self.paragraph = i[5]
                self.drawing_heroes(screen, font, self.paragraph)
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                    elif i.type == pygame.KEYDOWN:
                        # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                        if i.key == pygame.K_LEFT:
                            self.paragraph = (self.paragraph - 1) % 5
                        if i.key == pygame.K_RIGHT:
                            self.paragraph = (self.paragraph + 1) % 5
                        # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                        if i.key == 13:
                            oops = False
                    # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        oops = False
                screen.blit(screen, (0, 0))
                pygame.display.flip()
            if self.paragraph == 0:
                hero_creator = 'джонни'
                self.player_1 = pygame.image.load('джони_бой.jpg')
                screen.blit(self.player_1, (42, 42))
                pygame.display.flip()
            elif self.paragraph == 1:
                hero_creator = 'скорпион'
                self.player_1 = pygame.image.load('скорпион_бой.jpg')
                screen.blit(self.player_1, (42, 42))
                pygame.display.flip()
            elif self.paragraph == 2:
                hero_creator = 'соня'
                self.player_1 = pygame.image.load('соня_бой.jpg')
                screen.blit(self.player_1, (42, 42))
                pygame.display.flip()
            elif self.paragraph == 3:
                hero_creator = 'лю кан'
                self.player_1 = pygame.image.load('люканг_бой.jpg')
                screen.blit(self.player_1, (42, 42))
                pygame.display.flip()
            elif self.paragraph == 4:
                hero_creator = 'саб зиро'
                self.player_1 = pygame.image.load('сабзиро_бой.jpg')
                screen.blit(self.player_1, (42, 42))
            self.paragraph = 0
            pygame.display.flip()
        elif paragraph_number == 1:
            while oops:
                mouse = pygame.mouse.get_pos()
                for i in self.maps:
                    # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                    if mouse[0] > i[0] and mouse[0] < i[0] + 150 and mouse[1] > i[1] and mouse[1] < i[1] + 155:
                        self.paragraph = i[5]
                self.drawing_maps(screen, font, self.paragraph)
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                    elif i.type == pygame.KEYDOWN:
                        # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                        if i.key == pygame.K_LEFT:
                            self.paragraph = (self.paragraph - 1) % 3
                        if i.key == pygame.K_RIGHT:
                            self.paragraph = (self.paragraph + 1) % 3
                        # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                        if i.key == 13:
                            oops = False
                    # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        oops = False
                screen.blit(screen, (0, 0))
                pygame.display.flip()
            if self.paragraph == 0:
                main_map = 'храм воина'
            elif self.paragraph == 1:
                main_map = 'китай'
            elif self.paragraph == 2:
                main_map = 'подземелье'
            self.paragraph = 0
        elif self.paragraph == 2:
            return 'main'

    def drawing_maps(self, surface, font_menu, number_point):
        cycle = 0
        font_menu = pygame.font.SysFont('RomanD', 14)
        for i in self.maps:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
                pygame.draw.rect(surface, self.rects_maps[number_point][3], self.rects_maps[number_point][1], 4)
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
                pygame.draw.rect(surface, (0, 0, 0), self.rects_maps[cycle][1], 4)
                pygame.draw.rect(surface, self.rects_maps[cycle][2], self.rects_maps[cycle][1], 3)
            cycle += 1

    def drawing_heroes(self, surface, font_menu, number_point):
        cycle = 0
        font_menu = pygame.font.SysFont('RomanD', 14)
        for i in self.heroes:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
                pygame.draw.rect(surface, self.rects[number_point][3], self.rects[number_point][1], 4)
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
                pygame.draw.rect(surface, (0, 0, 0), self.rects[cycle][1], 4)
                pygame.draw.rect(surface, self.rects[cycle][2], self.rects[cycle][1], 3)
            cycle += 1

    def run(self):
        image_5 = pygame.image.load('заднийфон.jpg')
        screen.blit(image_5, (0, 0))
        screen.blit(self.player_1, (42, 42))
        pygame.display.flip()
        running = True
        font = pygame.font.SysFont('mr_AfronikG', 40)
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    self.paragraph = i[5]
            self.drawing(screen, font, self.paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                    if i.key == pygame.K_UP:
                        self.paragraph = (self.paragraph - 1) % 3
                    if i.key == pygame.K_DOWN:
                        self.paragraph = (self.paragraph + 1) % 3
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                    if i.key == pygame.K_RIGHT and (self.paragraph == 0 or self.paragraph == 1):
                        called_menu = self.clicked(self.paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(self.paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            image_map = pygame.image.load('map_2_full.jpg')
            screen.blit(image_map, (323, 483))
            image_map = pygame.image.load('map_1_full.png')
            screen.blit(image_map, (203, 483))
            image_map = pygame.image.load('map_3_full.png')
            screen.blit(image_map, (443, 483))
            image_0 = pygame.image.load('джони.png')
            screen.blit(image_0, (203, 373))
            image_1 = pygame.image.load('скорпион.png')
            screen.blit(image_1, (323, 373))
            image_2 = pygame.image.load('соня.png')
            screen.blit(image_2, (443, 373))
            image_3 = pygame.image.load('луи.png')
            screen.blit(image_3, (563, 373))
            image_4 = pygame.image.load('сабзиро.png')
            screen.blit(image_4, (683, 373))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


class select_fighter():
    def __init__(self):
        global hero_guest
        self.paragraph = 0
        self.points = [(65, 380, 'Ваш', (128, 128, 128), (204, 29, 0), 0),
                       (65, 415, 'герой', (128, 128, 128), (204, 29, 0), 0),
                       (65, 500, 'Выход', (128, 128, 128), (204, 29, 0), 1)]
        self.heroes = [(185, 347, 'Джони Кейдж', (128, 128, 128), (204, 29, 0), 0),
                       (322, 347, 'Скорпион', (128, 128, 128), (204, 29, 0), 1),
                       (433, 347, 'Соня Блейд', (128, 128, 128), (204, 29, 0), 2),
                       (568, 347, 'Лю Кан', (128, 128, 128), (204, 29, 0), 3),
                       (681, 347, 'Саб-зиро', (128, 128, 128), (204, 29, 0), 4)]
        self.rects = [('1', (200, 370, 81, 81), (128, 128, 128), (204, 29, 0), 0),
                      ('2', (320, 370, 81, 81), (128, 128, 128), (204, 29, 0), 1),
                      ('3', (440, 370, 81, 81), (128, 128, 128), (204, 29, 0), 2),
                      ('4', (560, 370, 81, 81), (128, 128, 128), (204, 29, 0), 3),
                      ('5', (680, 370, 81, 81), (128, 128, 128), (204, 29, 0), 4)]
        self.player_1 = pygame.image.load('джони_бой_з.jpg')
        self.called_menu = None

    def drawing(self, surface, font_menu, number_point):
        pygame.draw.rect(surface, (255, 255, 255), (40, 40, 240, 240), 3)
        pygame.draw.rect(surface, (255, 255, 255), (520, 40, 240, 240), 3)
        for i in range(5):
            pygame.draw.rect(surface, self.rects[i][2], self.rects[i][1], 3)
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
        for i in self.heroes:
            font_menu = pygame.font.SysFont('RomanD', 14)
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph_number):
        font = pygame.font.SysFont('mr_AfronikG', 40)
        oops = True
        if paragraph_number == 0:
            while oops:
                mouse = pygame.mouse.get_pos()
                for i in self.heroes:
                    # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                    if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 150:
                        self.paragraph = i[5]
                self.drawing_heroes(screen, font, self.paragraph)
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        sys.exit()
                    elif i.type == pygame.KEYDOWN:
                        # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                        if i.key == pygame.K_LEFT:
                            self.paragraph = (self.paragraph - 1) % 5
                        if i.key == pygame.K_RIGHT:
                            self.paragraph = (self.paragraph + 1) % 5
                        # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                        if i.key == 13:
                            oops = False
                    # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        oops = False
                screen.blit(screen, (0, 0))
                pygame.display.flip()
            if self.paragraph == 0:
                hero_guest = 'джонни'
                self.player_1 = pygame.image.load('джони_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 1:
                hero_guest = 'скорпион'
                self.player_1 = pygame.image.load('скорпион_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 2:
                hero_guest = 'соня'
                self.player_1 = pygame.image.load('соня_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 3:
                hero_guest = 'лю кан'
                self.player_1 = pygame.image.load('люканг_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 4:
                hero_guest = 'саб зиро'
                self.player_1 = pygame.image.load('сабзиро_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
            print(hero_guest)
            self.paragraph = 0
            pygame.display.flip()
        elif self.paragraph == 1:
            return 'main'

    def drawing_heroes(self, surface, font_menu, number_point):
        cycle = 0
        font_menu = pygame.font.SysFont('RomanD', 14)
        for i in self.heroes:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
                pygame.draw.rect(surface, self.rects[number_point][3], self.rects[number_point][1], 4)
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
                pygame.draw.rect(surface, (0, 0, 0), self.rects[cycle][1], 4)
                pygame.draw.rect(surface, self.rects[cycle][2], self.rects[cycle][1], 3)
            cycle += 1

    def run(self):
        image_5 = pygame.image.load('заднийфон.jpg')
        screen.blit(image_5, (0, 0))
        screen.blit(self.player_1, (522, 42))
        pygame.display.flip()
        running = True
        font = pygame.font.SysFont('mr_AfronikG', 40)
        while running:
            mouse = pygame.mouse.get_pos()
            for i in self.points:
                # меняем подсвечиваемую кнопку, при наведении на неё мышкой
                if mouse[0] > i[0] and mouse[0] < i[0] + 155 and mouse[1] > i[1] and mouse[1] < i[1] + 50:
                    self.paragraph = i[5]
            self.drawing(screen, font, self.paragraph)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # меняем подсвечиваемую кнопку кнопками верх/вниз, если это возможно
                    if i.key == pygame.K_UP:
                        self.paragraph = (self.paragraph - 1) % 2
                    if i.key == pygame.K_DOWN:
                        self.paragraph = (self.paragraph + 1) % 2
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                    if i.key == pygame.K_RIGHT and self.paragraph == 0:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(self.paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            image_0 = pygame.image.load('джони.png')
            screen.blit(image_0, (203, 373))
            image_1 = pygame.image.load('скорпион.png')
            screen.blit(image_1, (323, 373))
            image_2 = pygame.image.load('соня.png')
            screen.blit(image_2, (443, 373))
            image_3 = pygame.image.load('луи.png')
            screen.blit(image_3, (563, 373))
            image_4 = pygame.image.load('сабзиро.png')
            screen.blit(image_4, (683, 373))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu


class Egg:
    def __init__(self, music_class):
        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [30, 260, 'Назад', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [350, 260, 'УДАР', (128, 128, 128), 7],
                       [350, 300, 'СИЛ.УДАР', (128, 128, 128), 8],
                       [350, 340, 'УДАР НОГОЙ', (128, 128, 128), 9],
                       [350, 380, 'СИЛ.УДАР НОГОЙ', (128, 128, 128), 10],
                       [350, 420, 'ПРЫЖОК', (128, 128, 128), 11],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9],
                       [620, 380, 'S', (128, 128, 128), 10],
                       [620, 420, '3', (128, 128, 128), 11]]
        self.music_class = music_class

    def drawing(self, surface, font_menu):
        screen.fill(pygame.Color('black'))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            #screen.blit(screen, (0, 0))
            pygame.display.flip()
        # n.play()

    def run(self):
        self.points = [[30, 100, 'Музыка: вкл', (128, 128, 128), 0],
                       [30, 180, 'Звуки: вкл', (128, 128, 128), 1],
                       [30, 260, 'Назад', (128, 128, 128), 1],
                       [420, 35, 'Управление', (240, 240, 240), 3],
                       [350, 100, 'ВВЕРХ', (128, 128, 128), 3],
                       [350, 140, 'ВНИЗ', (128, 128, 128), 4],
                       [350, 180, 'ВЛЕВО', (128, 128, 128), 5],
                       [350, 220, 'ВПРАВО', (128, 128, 128), 6],
                       [350, 260, 'УДАР', (128, 128, 128), 7],
                       [350, 300, 'СИЛ.УДАР', (128, 128, 128), 8],
                       [350, 340, 'УДАР НОГОЙ', (128, 128, 128), 9],
                       [350, 380, 'СИЛ.УДАР НОГОЙ', (128, 128, 128), 10],
                       [350, 420, 'ПРЫЖОК', (128, 128, 128), 11],
                       [620, 100, 'C', (128, 128, 128), 3],
                       [620, 140, 'R', (128, 128, 128), 4],
                       [620, 180, 'E', (128, 128, 128), 5],
                       [620, 220, 'A', (128, 128, 128), 6],
                       [620, 260, 'T', (128, 128, 128), 7],
                       [620, 300, 'O', (128, 128, 128), 8],
                       [620, 340, 'R', (128, 128, 128), 9],
                       [620, 380, 'S', (128, 128, 128), 10],
                       [620, 420, '3', (128, 128, 128), 11]]
        font = pygame.font.SysFont('mr_AfronikG', 38)
        self.drawing(screen, font)
        self.flex()
        pygame.time.wait(2050)
        return 'main'

    def flex(self):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        for i in range(13, 22):
            points = list(self.points[i][2])
            points[0] = '-'
            self.points[i][2] = ''.join(points)
            pygame.time.wait(250)
            self.drawing(screen, font)
        for i in range(13, 21):
            sym = ['П', 'А', 'С', 'Х', 'А', 'Л', 'К', 'А']
            points = list(self.points[i][2])
            points[0] = sym[i - 13]
            self.points[i][2] = ''.join(points)
            pygame.time.wait(250)
            self.drawing(screen, font)
        for i in range(0, 22):
            points = list(self.points[i][2])
            for j in range(len(points)):
                points[j] = ''
                self.points[i][2] = ''.join(points)
                pygame.time.wait(10)
                self.drawing(screen, font)

m = Music()
s = Sound()
n = Music_Flex()
m.play()
mainC = MainMenu()
settingsC = Settings(m, s)
fightC = Fight()
fighterC = select_fighter()
current_menu = mainC
eggC = Egg(n)
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = settingsC
    elif t == 'main':
        current_menu = mainC
    elif t == 'fight':
        current_menu = fightC
    elif t == 'connect to server':
        current_menu = fighterC
    elif t == 'legendary_egg':
        current_menu = eggC
