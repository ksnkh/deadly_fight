import pygame


class CameraFocus(pygame.sprite.Sprite):
    def __init__(self, walls, *groups):
        super().__init__(groups)
        image = pygame.Surface([1, 1])
        image.fill(pygame.Color("#ff0000"))
        image.set_alpha(0)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 450)
        self.walls = walls

    def update(self, p1_x, p2_x):
        t = self.rect.x
        self.rect.x = ((p1_x + p2_x + 100) // 2)
        if pygame.sprite.spritecollideany(self, self.walls):
            self.rect.x = t

