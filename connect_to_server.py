import pygame

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Connect:
    def __init__(self):
        self.points = [[200, 35, 'Подключиться к серверу', (240, 240, 240), 3],
                       [250, 100, 'Введите ip сервера', (128, 128, 128), 0],
                       [175, 500, 'Назад', (128, 128, 128), 1],
                       [400, 500, 'Подключиться к серверу', (128, 128, 128), 1]]

    def drawing(self, surface, font_menu):
        screen.fill(pygame.Color('black'))
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))
            pygame.display.flip()

    def run(self):
        font = pygame.font.SysFont('mr_AfronikG', 38)
        self.drawing(screen, font)
        pygame.time.wait(2050)
        screen.fill(pygame.Color('black'))
        return 'main'