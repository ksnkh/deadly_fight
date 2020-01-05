import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        image = pygame.Surface([1700, 50])
        image.fill(pygame.Color("#000000"))
        image.set_alpha(0)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (-450, 540)
