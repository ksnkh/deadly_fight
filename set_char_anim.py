import pygame
from load_image import load_image


def set_char_anim(char, anim):
    char.cur_anim = anim
    char.curent_animation_settings = char.animation_settings[anim]
    char.can_turn = char.curent_animation_settings[4]
    char.frame_time = char.curent_animation_settings[2][0]
    char.frames = []
    char.cur_frame = 0

    sheet = load_image(f"animations/{char.name}/{anim}.png", -1)
    height = sheet.get_rect().size[1]
    for i in range(char.curent_animation_settings[0]):
        frame_location = (char.curent_animation_settings[1] * i, 0)
        frame = sheet.subsurface(pygame.Rect(frame_location, [51, height]))
        color_key = frame.get_at((0, 0))
        frame.set_colorkey(color_key)
        char.frames.append(pygame.transform.scale(frame, (200, 300)))
    # NECESSARY EDITING
    if anim == 'duck':
        char.frames += char.frames[1::-1]
    if anim == 'move_jump':
        char.frames += char.frames[0:1]
