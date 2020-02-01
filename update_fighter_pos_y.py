import pygame
from change_fighter_position import change_position


def update_y(fighter, f=False):
    # UPDATE Y
    change_position(fighter, [0, fighter.vector[1]])

    if fighter.pos_y + fighter.rect.height > 540:
        change_position(fighter, [0,  540 - (fighter.pos_y + fighter.rect.height)], True)
        fighter.vector[1] = 0
        if not fighter.getting_damage and fighter.cur_anim != 'slide':
            fighter.vector[0] = 0
        fighter.on_ground = 1
