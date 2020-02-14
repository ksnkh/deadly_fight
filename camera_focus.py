import pygame


class CameraFocus(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        image = pygame.Surface([1, 1])
        image.fill(pygame.Color("#ff0000"))
        image.set_alpha(0)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 450)
        self.pos_x = 850

    def update(self, p1_x, p2_x):
        new_pos = (p1_x + p2_x) // 2
        if new_pos <= 400:
            self.pos_x = 400
            self.rect.x = 400
        elif new_pos >= 1200:
            self.pos_x = 1200
            self.rect.x = 400
        else:
            dif = new_pos - self.pos_x
            self.rect.x += dif
            self.pos_x = new_pos


