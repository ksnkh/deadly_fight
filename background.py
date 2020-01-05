import pygame
from load_image import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, *groups, picture=False):
        super().__init__(groups)
        image = pygame.Surface([1700, 600])
        image.fill(pygame.Color("red"))
        if picture:
            self.image = load_image(picture)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (-450, 0)
