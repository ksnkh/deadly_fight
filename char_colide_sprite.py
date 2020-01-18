import pygame
import random


class ColisionRect(pygame.sprite.Sprite):
    def __init__(self, coords, *groups):
        super().__init__(groups)
        image = pygame.Surface([60, 200])
        image.fill((0, random.randint(0, 255), random.randint(0, 255)))
        image.set_alpha(0)
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = coords
        self.offset = 35
