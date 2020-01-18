import pygame
from load_image import load_image
from subzero_animations_settings import subzero_animations


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
        self.cur_anim = anim
        self.curent_animation_settings = self.animation_settings[anim]
        self.frame_time = self.curent_animation_settings[2][0]
        self.frames = []
        self.cur_frame = 0

        sheet = load_image(f"animations/{self.name}/{anim}.png", -1)
        height = sheet.get_rect().size[1]
        for i in range(self.curent_animation_settings[0]):
            frame_location = (self.curent_animation_settings[1] * i, 0)
            frame = sheet.subsurface(pygame.Rect(frame_location, [51, height]))
            color_key = frame.get_at((0, 0))
            frame.set_colorkey(color_key)
            self.frames.append(pygame.transform.scale(frame, (200, 300)))


    def get_damage(self, damage):
        self.health -= damage

