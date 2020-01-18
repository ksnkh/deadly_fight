import pygame
from subzero_animations_settings import subzero_animations
from set_char_anim import set_char_anim


class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, collision_rect, *groups):
        super().__init__(groups)
        self.name = name
        if self.name == 'Sub-Zero':
            self.animation_settings = subzero_animations
        self.frames = []
        self.set_anim('stand')
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.side = side
        self.vector = [0, 0]
        self.collision_rect = collision_rect
        self.ducked = False
        self.turn = False
        self.can_turn = True

        if side == 'left':
            self.pos_x = 100
            self.pos_y = 240
            self.collision_rect.offset = 20
        else:
            self.pos_x = 500
            self.pos_y = 240
            self.collision_rect.offset = 50
        self.rect.topleft = [self.pos_x, self.pos_y]

        self.vector = [0, 0]
        self.on_ground = 0
        self.health = 100

    def set_anim(self, anim):
        set_char_anim(self, anim)

    def get_damage(self, damage):
        self.health -= damage

