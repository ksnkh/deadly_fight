import pygame
from subzero_animations_settings import subzero_move_animations, subzero_attack_animations
from scorpion_animations_settings import scorpion_move_animations, scorpion_attack_animations
from jonny_cage_animations_settings import johny_cage_move_animations, johny_cage_attack_animations
from sonya_animations_settings import sonya_attack_animations, sonya_move_animations
from lu_kang_animation_settings import liu_kang_attack_animations, liu_kang_move_animations
from set_char_anim import set_char_anim
from change_fighter_position import change_position


class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, *groups):
        super().__init__(groups)
        self.name = name
        self.side = side
        if self.name == 'Sub-Zero':
            self.animation_settings = subzero_move_animations
            self.attack_animations = subzero_attack_animations
        elif self.name == 'Scorpion':
            self.animation_settings = scorpion_move_animations
            self.attack_animations = scorpion_attack_animations
        elif self.name == 'Johny Cage':
            self.animation_settings = johny_cage_move_animations
            self.attack_animations = johny_cage_attack_animations
        elif self.name == 'Sonya':
            self.animation_settings = sonya_move_animations
            self.attack_animations = sonya_attack_animations
        elif self.name == 'Liu Kang':
            self.animation_settings = liu_kang_move_animations
            self.attack_animations = liu_kang_attack_animations

        if self.side == 'left':
            self.pos_x = 100
            self.pos_y = 240
        else:
            self.pos_x = 500
            self.pos_y = 240

        self.actual_coords_x = self.pos_x + 450
        self.actual_coords_y = self.pos_y
        self.frames = []
        self.previos_moves = []
        self.cur_anim = 'stand'
        self.rect = None
        self.set_anim('stand')
        self.image = self.frames[self.cur_frame]
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.mask = pygame.mask.from_surface(self.image)
        self.vector = [0, 0]
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
        self.dead = False
        change_position(self, self.vector, 'all')

    def set_anim(self, anim):
        set_char_anim(self, anim)

    def get_damage(self, damage):
        if self.cur_anim == 'block':
            self.helth -= damage // 10
        else:
            self.helth -= damage
