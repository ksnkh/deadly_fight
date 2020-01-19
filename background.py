import pygame
from load_image import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, picture, *groups):
        super().__init__(groups)
        self.image = load_image(picture)
        self.image = pygame.transform.scale(self.image, (1700, 600))
        self.rect = self.image.get_rect()
        self.rect.topleft = (-450, 0)
