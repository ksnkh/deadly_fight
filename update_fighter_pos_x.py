import pygame
from change_fighter_position import change_position


def update_x(fighter, enemy, f=False):
    # UPDATE X
    change_position(fighter, [fighter.vector[0], 0], 'all')

    # CHAR COLLISION
    if fighter.cur_anim not in ['thrown'] and fighter.cur_anim not in fighter.attack_animations \
                and not (fighter.actual_coords_y < enemy.actual_coords_y and fighter.actual_coords_y + fighter.rect.height < enemy.actual_coords_y \
                or (enemy.actual_coords_y < fighter.actual_coords_y and enemy.actual_coords_y + enemy.rect.height < fighter.actual_coords_y)):
        if fighter.actual_coords_x > enemy.actual_coords_x and fighter.actual_coords_x + fighter.rect.width - 200 < enemy.actual_coords_x + 170:
            dif = [(enemy.actual_coords_x + 170) - (fighter.actual_coords_x + fighter.rect.width - 200), 0]
        elif fighter.actual_coords_x < enemy.actual_coords_x and fighter.actual_coords_x + 170 > enemy.actual_coords_x + enemy.rect.width - 200:
            dif = [(enemy.actual_coords_x + enemy.rect.width - 200) - (fighter.actual_coords_x + 170), 0]
        else:
            dif = [0, 0]
        if fighter.vector[0] != 0 and fighter.cur_anim != 'teleport':
            change_position(fighter, dif, 'all')

    # SCREEN BORDER COLLISION
    if fighter.pos_x < 0:
        dif = [0 - fighter.pos_x, 0]
    elif fighter.pos_x + fighter.rect.width > 800:
        dif = [800 - (fighter.pos_x + fighter.rect.width), 0]
    else:
        dif = [0, 0]
    if fighter.vector[0] != 0 and fighter.cur_anim != 'teleport':
        change_position(fighter, dif, 'all')



    # WALL COLLISION
    if fighter.actual_coords_x < 0:
        dif = [0 - fighter.actual_coords_x, 0]
    elif fighter.actual_coords_x + fighter.rect.width > 1700:
        dif = [1700 - (fighter.actual_coords_x + fighter.rect.width), 0]
    else:
        dif = [0, 0]
    change_position(fighter, dif, 'all')