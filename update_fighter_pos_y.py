import pygame
from change_fighter_position import change_position


def update_y(fighter, f=False):
    # UPDATE Y
    change_position(fighter, [0, fighter.vector[1]], 'all')

    if fighter.actual_coords_y + fighter.rect.height > 540:
        dif = [0, (540 - fighter.rect.height) - fighter.actual_coords_y]
        change_position(fighter, dif, 'all')
        fighter.actual_coords_y = 540 - fighter.rect.height
        if fighter.cur_anim != 'slide':
            fighter.vector[0] = 0
        fighter.on_ground = 1
        fighter.vector[1] = 0
