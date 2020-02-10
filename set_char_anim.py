import pygame
from load_image import load_image
from change_fighter_position import change_position
from turn_frame import turn_frame


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
        frame_location = (sum(char.curent_animation_settings[1][:i]), 0)
        frame = sheet.subsurface(pygame.Rect(frame_location, [char.curent_animation_settings[1][i], height]))
        color_key = frame.get_at((0, 0))
        frame.set_colorkey(color_key)
        char.frames.append(pygame.transform.scale(frame, (char.curent_animation_settings[1][i] * 4, height * 3)))

    if char.rect is None:
        t = 540
        char.rect = char.frames[0].get_rect()
    else:
        t = char.pos_y + char.rect.height
        char.rect.height = char.frames[0].get_rect()[3]
        change_position(char, [0, t - char.rect.height - char.pos_y], 'all')


    # NECESSARY EDITING
    if anim == 'duck':
        char.frames += char.frames[1::-1]
    if anim == 'move_jump':
        char.frames += char.frames[0:1]
    if anim == 'walk_b':
        char.frames = char.frames[::-1]
    if anim == 'thrown':
        for i in range(len(char.frames)):
            char.frames[i] = pygame.transform.flip(char.frames[i], True, False)
    if anim == 'slide':
        if char.side == 'left':
            char.vector[0] = 10
        else:
            char.vector[0] = -10


    if char.cur_anim != 'stand':
        if char.previos_moves and char.previos_moves[-1][0] == anim:
            char.previos_moves[-1][1] = 0
        else:
            char.previos_moves.append([char.cur_anim, 0])
