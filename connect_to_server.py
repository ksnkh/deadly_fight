import pygame
import sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Connect:
    def __init__(self):
        self.points = [[200, 35, 'Подключиться к серверу', (240, 240, 240)],
                       [250, 100, 'Введите ip сервера', (228, 2, 11)],
                       [175, 500, 'Назад', (228, 2, 11), 0],
                       [400, 500, 'Подключиться к серверу', (228, 2, 11), 1]]

    def drawing(self, surface, font_menu):
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            pygame.display.flip()

    def clicked(self, paragraph_number):
        if paragraph_number == 0:
            self.change(3)
        elif paragraph_number == 1:
            self.change(4)

    def change(self, set):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        oops = True
        pygame.display.flip()
        a = 0
        while oops:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

    def run(self):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        running = True
        while running:
            self.drawing(screen, font)
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return 'main'