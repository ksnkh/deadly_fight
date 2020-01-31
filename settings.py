import pygame, sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
cycle = 0

control = {'ВВЕРХ': 'W',
           'ВНИЗ': 'S',
           'ВЛЕВО': 'A',
           'ВПРАВО': 'D',
           'УДАР': 'Y',
           'СИЛЬНЫЙ УДАР': 'U',
           'УДАР НОГОЙ': 'I',
           'СИЛЬНЫЙ УДАР НОГОЙ': 'O',
           'ПРЫЖОК': 'SPACE'}

handle = open("other\control.txt", "r")
data = handle.read()
data = data.split('\n')
for i in range(len(data)):
    if i == 0:
        control['ВВЕРХ'] = data[i]
    elif i == 1:
        control['ВНИЗ'] = data[i]
    elif i == 2:
        control['ВЛЕВО'] = data[i]
    elif i == 3:
        control['ВПРАВО'] = data[i]
    elif i == 4:
        control['УДАР'] = data[i]
    elif i == 5:
        control['СИЛЬНЫЙ УДАР'] = data[i]
    elif i == 6:
        control['УДАР НОГОЙ'] = data[i]
    elif i == 7:
        control['СИЛЬНЫЙ УДАР НОГОЙ'] = data[i]
    elif i == 8:
        control['ПРЫЖОК'] = data[i]

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

class Settings:
    def __init__(self, music_class, sound_class):
        global setting_music
        self.cycle = 0
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
        if paragraph_number == 2 and self.gold_egg == 'CREATORS3':
            if self.cycle == 0:
                self.cycle += 1
                return 'legendary_egg'
            else:
                return 'main'
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
                    keyboard_sym = ''
                    for i in range(13, 22):
                        self.gold_egg += self.points[i][2]
                        keyboard_sym += self.points[i][2] + '\n'
                    handle = open("other\control.txt", "w")
                    handle.write(keyboard_sym)
                    handle.close()
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
        image_5 = pygame.image.load('backgrounds\лес.png')
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

