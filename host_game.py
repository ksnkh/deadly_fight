import pygame, sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

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
        self.player_1 = pygame.image.load('heroes\джони_бой_з.jpg')
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
                self.player_1 = pygame.image.load('heroes\джони_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 1:
                hero_guest = 'скорпион'
                self.player_1 = pygame.image.load('heroes\скорпион_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 2:
                hero_guest = 'соня'
                self.player_1 = pygame.image.load('heroes\соня_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 3:
                hero_guest = 'лю кан'
                self.player_1 = pygame.image.load('heroes\люканг_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
                pygame.display.flip()
            elif self.paragraph == 4:
                hero_guest = 'саб зиро'
                self.player_1 = pygame.image.load('heroes\сабзиро_бой_з.jpg')
                screen.blit(self.player_1, (522, 42))
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
        image_5 = pygame.image.load('backgrounds\заднийфон.jpg')
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
            image_0 = pygame.image.load('heroes\джони.png')
            screen.blit(image_0, (203, 373))
            image_1 = pygame.image.load('heroes\скорпион.png')
            screen.blit(image_1, (323, 373))
            image_2 = pygame.image.load('heroes\соня.png')
            screen.blit(image_2, (443, 373))
            image_3 = pygame.image.load('heroes\луи.png')
            screen.blit(image_3, (563, 373))
            image_4 = pygame.image.load('heroes\сабзиро.png')
            screen.blit(image_4, (683, 373))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return called_menu