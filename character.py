import pygame
from load_image import load_image

INITIAL_POSITION_X = 100
INITIAL_POSITION_Y = 250


class Character(pygame.sprite.Sprite):
    def __init__(self, walls, ground, side, *groups, picture=False):
        super().__init__(groups)
        image = pygame.Surface([100, 200])
        image.fill(pygame.Color("blue"))
        if picture:
            self.image = load_image(picture)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        if side == 'left':
            self.pos_x = 100
            self.pos_y = 340
        else:
            self.pos_x = 600
            self.pos_y = 340
        self.rect.topleft = [self.pos_x, self.pos_y]

        self.vector = [0, 0]
        self.on_ground = 0
        self.walls = walls
        self.ground = ground
        self.health = 100

    def fall(self):
        self.vector[1] += 0.3

    def move(self, shift):
        if self.on_ground:
            self.vector[0] = 4 * shift

    def jump(self):
        if self.on_ground:
            self.vector[1] -= 13
            self.vector[0] *= 1.5
            self.on_ground = 0
            print(self.vector)

    def update_pos(self):
        self.pos_x += self.vector[0]
        self.rect.topleft = [self.pos_x, self.pos_y]
        if pygame.sprite.spritecollideany(self, self.walls):
            self.pos_x -= self.vector[0]
            self.rect.topleft = [self.pos_x, self.pos_y]
        if self.on_ground:
            self.vector[0] = 0

        self.pos_y += self.vector[1]
        self.rect.topleft = [self.pos_x, self.pos_y]
        if pygame.sprite.spritecollideany(self, self.ground):
            for i in range(int(self.vector[1] + 0.9)):
                if pygame.sprite.spritecollideany(self, self.ground):
                    self.pos_y -= 1
                    self.rect.topleft = [self.pos_x, self.pos_y]
                else:
                    break
            self.vector[1] = 0
            self.on_ground = 1

    def get_damage(self, damage):
        self.health -= damage

