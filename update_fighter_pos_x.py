import pygame
from change_fighter_position import change_position


def update_x(fighter, walls, enemy, f=False):
    # UPDATE X
    fighter.pos_x += fighter.vector[0]
    change_position(fighter)

    # WALL COLLISION
    if f:
        print(fighter.pos_x)
    if fighter.pos_x < 0:
        shift = 1
    elif fighter.pos_x > 600:
        if f:
            print(1)
        shift = -1
    else:
        shift = 0
    while not 0 <= fighter.pos_x <= 600:
        fighter.pos_x += shift
        change_position(fighter)
        fighter.vector[0] = 0

    # CHAR COLLISION
    if fighter.cur_anim not in ['throw', 'thrown'] and enemy.cur_anim not in ['throw', 'thrown'] \
        and max(fighter.actual_coords_x, enemy.actual_coords_x) < min(fighter.actual_coords_x,
                                                                          enemy.actual_coords_x) + 100:
        print(1)
        if not (fighter.actual_coords_y < enemy.actual_coords_y and fighter.actual_coords_y + fighter.rect.width < enemy.actual_coords_y \
                or (
                enemy.actual_coords_y < fighter.actual_coords_y and enemy.actual_coords_y + enemy.rect.width < fighter.actual_coords_y)):
            print(2)
            if fighter.side == 'left':
                shift = -1
            else:
                shift = 1
            while pygame.sprite.collide_rect(fighter.collision_rect, enemy.collision_rect):
                fighter.pos_x += shift
                change_position(fighter)
            fighter.pos_x += shift
            change_position(fighter)
            fighter.vector[0] = 0
