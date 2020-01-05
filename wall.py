import pygame
from load_image import load_image


class Wall(pygame.sprite.Sprite):
    def __init__(self, *groups, picture=False):
        super().__init__(groups)
        image = pygame.Surface([10, 50])
        image.fill(pygame.Color("red"))
        if picture:
            self.image = load_image(picture)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = event.pos