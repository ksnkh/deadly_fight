import pygame
from update_anim import update_anim
from change_fighter_position import change_position
from turn_frame import turn_frame
from set_char_anim import set_char_anim


def update_img(char, enemy, side, cf, f=False):
    char.frame_time -= 1
    if char.frame_time == 0:

        if char.curent_animation_settings[3]:
            if char.cur_frame == char.curent_animation_settings[3][1]:
                char.cur_frame = char.curent_animation_settings[3][0] - 1

        if char.cur_frame == len(char.curent_animation_settings[2]) - 1:
            char.cur_anim = ''
            char.attack = False
            char.hit = False
            char.vector = [0, 0]
            char.can_turn = True
            turn_frame(char, side)
            if char.cur_anim in ['trip', 'thrown']:
                set_char_anim(char, 'stand_up')
            else:
                char.getting_damage = False
                update_anim(char)

        else:
            char.cur_frame += 1
        try:
            char.frame_time = char.curent_animation_settings[2][char.cur_frame]
        except IndexError:
            print(char.curent_animation_settings[2], char.cur_frame)

    char.image = char.frames[char.cur_frame]

    if char.side == 'right':
        t = char.actual_coords_x + char.rect.width
        char.rect.size = char.image.get_size()
        change_position(char, [(t - char.rect.width) - char.actual_coords_x, 0], 'all')

    else:
        char.rect.size = char.image.get_size()

    char.mask = pygame.mask.from_surface(char.image)
    char.damage = 0
    if char.curent_animation_settings[5]:
        if char.cur_frame in char.curent_animation_settings[5][0]:
            char.damage = char.curent_animation_settings[5][2]

    turn_frame(char, side)

    if char.side == 'right':
        cf.update(char.actual_coords_x + char.rect.width,
                                 enemy.actual_coords_x)
    else:
        cf.update(char.actual_coords_x,
                                 enemy.actual_coords_x + enemy.rect.width)

    # NECESSARY EDITING
    if char.cur_anim == 'leg_throw':
        if char.cur_frame <= 5:
            char.vector[0] = 3
        elif char.cur_frame > 5:
            char.vector[0] = -3
        if char.side == 'right':
            char.vector[0] *= -1

    if char.cur_anim == 'throw' and char.cur_frame == 3 and not char.hit:
        char.cur_anim = ''
        char.attack = False
        char.hit = False
        char.vector = [0, 0]
        char.can_turn = True
        turn_frame(char, side)
        char.getting_damage = False
        update_anim(char)
