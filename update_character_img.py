import pygame


def update_img(char, side):
    char.frame_time -= 1
    if char.frame_time == 0:
        if char.curent_animation_settings[3]:
            if char.cur_frame == char.curent_animation_settings[3][1]:
                char.cur_frame = char.curent_animation_settings[3][0] - 1

        if char.cur_frame == len(char.curent_animation_settings[2]) - 1:
            char.set_anim('stand')
            return

        char.cur_frame += 1
        char.frame_time = char.curent_animation_settings[2][char.cur_frame]
    char.image = char.frames[char.cur_frame]
    if char.turn:
        char.image = pygame.transform.flip(char.image, True, False)
        char.collision_rect.offset = 80
    else:
        char.collision_rect.offset = 40

    # TURN IMAGE
    char.side = side
    if char.can_turn:
        if char.side == 'right':
            char.turn = True
        else:
            char.turn = False
