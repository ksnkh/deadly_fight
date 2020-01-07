import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()

settings = {'music': 1, 'sound': 1}


class Music:
    def __init__(self):
        self.on = True
        pygame.mixer.music.load('music.mp3')

    def play(self):
        pygame.mixer.music.play(-1)
        pass

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
        self.points = [(30, 100, 'Подключиться к серверу', (250, 250, 30), (250, 30, 250), 0),
                       (30, 200, 'Создать сервер', (250, 250, 30), (250, 30, 250), 1),
                       (30, 300, 'Настройки', (250, 250, 30), (250, 30, 250), 2),
                       (30, 400, 'Выход', (250, 250, 30), (250, 30, 250), 3)]
        self.font = pygame.font.SysFont('serif', 30)
        self.called_menu = None

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph_number):
        if paragraph_number == 0:
            # В будующем надо будет вызывать меню подключения к серверу
            return 'connect to server'
        elif paragraph_number == 1:
            # В будующем надо будет вызывать меню выбора персонажа место начала игры
            return 'fight'
        elif paragraph_number == 2:
            return 'settings'
        elif paragraph_number == 3:
            sys.exit()

    def run(self):
        running = True
        font = pygame.font.SysFont('serif', 30)
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
            '274': 'ARROW_DOWN',
            '275': 'ARROW_RIGHT',
            '276': 'ARROW_LEFT'}

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


class Settings:
    def __init__(self, music_class, sound_class):
        self.paragraph = 0
        self.points = [(30, 100, 'Музыка: вкл/выкл', (250, 250, 30), (250, 30, 250), 0),
                       (30, 200, 'Звуки: вкл/выкл', (250, 250, 30), (250, 30, 250), 1),
                       (30, 300, 'Назад', (250, 250, 30), (250, 30, 250), 2),
                       (450, 35, 'Управление', (250, 250, 30), (250, 30, 250), 3),
                       [350, 100, 'ВВЕРХ', (250, 250, 30), (250, 30, 250), 3],
                       (350, 140, 'ВНИЗ', (250, 250, 30), (250, 30, 250), 4),
                       (350, 180, 'ВЛЕВО', (250, 250, 30), (250, 30, 250), 5),
                       (350, 220, 'ВПРАВО', (250, 250, 30), (250, 30, 250), 6),
                       (350, 260, 'УДАР', (250, 250, 30), (250, 30, 250), 7),
                       (350, 300, 'СИЛ.УДАР', (250, 250, 30), (250, 30, 250), 8),
                       (350, 340, 'УДАР НОГОЙ', (250, 250, 30), (250, 30, 250), 9),
                       (350, 380, 'СИЛ.УДАР НОГОЙ', (250, 250, 30), (250, 30, 250), 10),
                       (350, 420, 'ПРЫЖОК', (250, 250, 30), (250, 30, 250), 11),
                       (350, 460, 'X-RAY', (250, 250, 30), (250, 30, 250), 12),
                       [620, 100, control['ВВЕРХ'], (250, 250, 30), (250, 30, 250), 3],
                       [620, 140, control['ВНИЗ'], (250, 250, 30), (250, 30, 250), 4],
                       [620, 180, control['ВЛЕВО'], (250, 250, 30), (250, 30, 250), 5],
                       [620, 220, control['ВПРАВО'], (250, 250, 30), (250, 30, 250), 6],
                       [620, 260, control['УДАР'], (250, 250, 30), (250, 30, 250), 7],
                       [620, 300, control['СИЛЬНЫЙ УДАР'], (250, 250, 30), (250, 30, 250), 8],
                       [620, 340, control['УДАР НОГОЙ'], (250, 250, 30), (250, 30, 250), 9],
                       [620, 380, control['СИЛЬНЫЙ УДАР НОГОЙ'], (250, 250, 30), (250, 30, 250), 10],
                       [620, 420, control['ПРЫЖОК'], (250, 250, 30), (250, 30, 250), 11],
                       [620, 460, control['X-RAY'], (250, 250, 30), (250, 30, 250), 12]]
        self.music_class = music_class
        self.sound_class = sound_class

    def clicked(self, paragraph_number):
        if paragraph_number == 0:
            if self.music_class.on:
                self.music_class.not_play()
                self.music_class.on = False
            else:
                self.music_class.play()
                self.music_class.on = True
        elif paragraph_number == 1:
            if self.sound_class.on:
                self.sound_class.on = False
            else:
                self.sound_class.on = True
        elif paragraph_number == 2:
            return 'main'
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
        elif paragraph_number == 12:
            self.change(12)

    def change(self, set):
        font = pygame.font.SysFont('serif', 30)
        oops = True
        screen.blit(font.render(self.points[set + 11][2], 2, (255, 36, 0)),
                    (self.points[set + 11][0], self.points[set + 11][1]))
        pygame.display.flip()
        a = 0
        while oops:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    key = i.key
                    print(key)
                    control[self.points[set + 1][2]] = str(key)
                    for i in self.points:
                        if i == self.points[set + 11]:
                            if str(key) in keyboard:
                                i[2] = keyboard[str(key)]
                            else:
                                i[2] = str(key)
                    oops = False

    def drawing(self, surface, font_menu, number_point):
        for i in self.points:
            if i != self.points[3]:
                # print(i[2])
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
        font = pygame.font.SysFont('serif', 30)
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
                        self.paragraph = (self.paragraph - 1) % 13
                    if i.key == pygame.K_DOWN:
                        self.paragraph = (self.paragraph + 1) % 13
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
    def run(self):
        print(1)
        return 'main'


def select_fighter():
    pass


m = Music()
s = Sound()
m.play()
mainC = MainMenu()
settingsC = Settings(m, s)
fightC = Fight()
current_menu = mainC
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = settingsC
    elif t == 'main':
        current_menu = mainC
    elif t == 'fight':
        current_menu = fightC
