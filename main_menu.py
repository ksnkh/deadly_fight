import pygame, sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

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
            return 'choose fighter h'
        elif paragraph_number == 2:
            return 'settings'
        elif paragraph_number == 3:
            return 'exit'

    def run(self):
        image_6 = pygame.image.load('backgrounds\он_скорпион3.jpg')
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
        return [called_menu]