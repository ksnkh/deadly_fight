import pygame


def update_img(char, side):
    char.frame_time -= 1
    if char.cur_anim == 'move_jump':
        print(char.frame_time)
    if char.frame_time == 0:
        if char.curent_animation_settings[3]:
            if char.cur_frame == char.curent_animation_settings[3][1]:
                char.cur_frame = char.curent_animation_settings[3][0] - 1

        elif char.cur_frame == len(char.curent_animation_settings[2]):
            char.set_anim('stand')
            return

        char.cur_frame += 1
        char.frame_time = char.curent_animation_settings[2][char.cur_frame]
    char.image = char.frames[char.cur_frame]


    # TURN IMAGE
    char.side = side
    if char.side == 'right':
        char.image = pygame.transform.flip(char.image, True, False)
        char.collision_rect.offset = 50
    else:
        char.collision_rect.offset = 20
