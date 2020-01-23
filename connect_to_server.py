import pygame
import sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

keyboard = {'49': '1',
            '50': '2',
            '51': '3',
            '52': '4',
            '53': '5',
            '54': '6',
            '55': '7',
            '56': '8',
            '57': '9',
            '48': '0',
            '32': '.'}


class Connect:
    def __init__(self):
        self.number_server = '12'
        self.paragraph = 0
        self.points = [[200, 35, 'Подключиться к серверу', (240, 240, 240), (240, 240, 240), 0],
                       [188, 200, 'Введите ip сервера через пробел', (240, 240, 240), (240, 240, 240), 0],
                       [175, 500, 'Назад', (128, 128, 128), (210, 50, 0), 0],
                       [400, 500, 'Подключиться к серверу', (128, 128, 128), (210, 50, 0), 1]]

    def drawing(self, surface, font_menu, number_point):
        pygame.display.flip()
        font1 = pygame.font.SysFont('ToughSansRegular', 60)
        pygame.draw.rect(screen, (255, 255, 255), (175, 250, 500, 75), 5)
        surface.blit(font1.render(self.number_server, 2, (255, 255, 255)), (185, 255))
        for i in self.points:
            if number_point == i[5]:
                surface.blit(font_menu.render(i[2], 2, i[4]), (i[0], i[1]))
            else:
                surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def clicked(self, paragraph_number):
        if paragraph_number == 0:
            return 'main'
        elif paragraph_number == 1:
            return 'connect to server'

    def run(self):
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
                    if i.key == pygame.K_RIGHT:
                        self.paragraph = (self.paragraph - 1) % 2
                    if i.key == pygame.K_LEFT:
                        self.paragraph = (self.paragraph + 1) % 2
                    # вызываем действия от подсвечиваемой кнопки при нажатии на enter
                    if i.key == 13:
                        called_menu = self.clicked(self.paragraph)
                        running = False
                    if str(i.key) in keyboard and len(self.number_server) < 15:
                        self.number_server += keyboard[str(i.key)]
                    if i.key == 8:
                        a = list(self.number_server)
                        b = a[0:-1]
                        self.number_server = ''.join(b)
                        screen.fill(pygame.Color('black'))
                # вызываем действия от подсвечиваемой кнопки при нажатии на левую кнопку мыши/enter
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    called_menu = self.clicked(self.paragraph)
                    running = False
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu
