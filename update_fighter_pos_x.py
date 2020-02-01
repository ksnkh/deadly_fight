import pygame
from change_fighter_position import change_position


def update_x(fighter, walls, enemy, f=False):
    # UPDATE X
    change_position(fighter, [fighter.vector[0], 0])

    # CHAR COLLISION
    if fighter.cur_anim not in ['throw', 'thrown'] and enemy.cur_anim not in ['throw', 'thrown'] \
                   and max(fighter.pos_x, enemy.pos_x) < min(fighter.pos_x, enemy.pos_x) + 100:
        print(1)
        if not (fighter.actual_coords_y < enemy.actual_coords_y and fighter.actual_coords_y + fighter.rect.width < enemy.actual_coords_y \
                or (enemy.actual_coords_y < fighter.actual_coords_y and enemy.actual_coords_y + enemy.rect.width < fighter.actual_coords_y)):
            print(2)
            if fighter.side == 'left':
                shift = -1
            else:
                shift = 1
            while max(fighter.pos_x, enemy.pos_x) < min(fighter.pos_x, enemy.pos_x) + 100:
                change_position(fighter, [shift, 0])
            fighter.vector[0] = 0

    # WALL COLLISION
    if not 0 <= fighter.pos_x <= 800 - fighter.rect.width:
        if fighter.pos_x < 0:
            shift = 1
        elif fighter.pos_x > 800 - fighter.rect.width:
            shift = -1
        else:
            shift = 0
        while not 0 <= fighter.pos_x <= 800 - fighter.rect.width:
            change_position(fighter, [shift, 0])
            fighter.vector[0] = 0
