import pygame


class CameraFocus(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        image = pygame.Surface([5, 5])
        image.fill(pygame.Color("#ff0000"))
        self.image = image
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 450)
        self.pos_x = 850

    def update(self, p1_x, p2_x):
        new_pos = (p1_x + p2_x) // 2
        dif = new_pos - self.rect.x
        if 400 > self.pos_x + dif:
            dif = 400 - self.pos_x
        elif self.pos_x + dif > 1300:
            dif = 1300 - self.pos_x
        self.rect.x += dif
        self.pos_x += dif
