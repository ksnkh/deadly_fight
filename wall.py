import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, coords, *groups):
        super().__init__(groups)
        image = pygame.Surface([1, 600])
        image.fill(pygame.Color("#ffffff"))
        image.set_alpha(0)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
