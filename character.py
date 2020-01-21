import pygame
from subzero_animations_settings import subzero_move_animations
from set_char_anim import set_char_anim


class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, collision_rect, *groups):
        super().__init__(groups)
        self.name = name
        if self.name == 'Sub-Zero':
            self.animation_settings = subzero_move_animations
        self.frames = []
        self.previos_moves = []
        self.cur_anim = 'stand'
        self.set_anim('stand')
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.side = side
        self.vector = [0, 0]
        self.collision_rect = collision_rect
        self.ducked = False
        self.block = False
        self.turn = False
        self.can_turn = True
        self.attack = False
        self.hit = False
        self.vector = [0, 0]
        self.on_ground = 0
        self.helth = 300
        self.damage = 0
        self.getting_damage = False

        if side == 'left':
            self.pos_x = 100
            self.pos_y = 240
            self.collision_rect.offset = 20
        else:
            self.pos_x = 500
            self.pos_y = 240
            self.collision_rect.offset = 50
        self.rect.topleft = [self.pos_x, self.pos_y]

    def set_anim(self, anim):
        set_char_anim(self, anim)

    def get_damage(self, damage):
        if self.cur_anim == 'block':
            self.helth -= damage // 10
        else:
            self.helth -= damage
