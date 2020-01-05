import pygame
from load_image import load_image


class CameraFocus(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        image = pygame.Surface([1, 1])
        image.fill(pygame.Color("#ff0000"))
        image.set_alpha(255)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 450)

    def update(self, p1_x, p2_x):
        print(p1_x, p2_x)
        self.rect.topleft = ((p1_x + p2_x + 100) // 2, self.rect.topleft[1])
