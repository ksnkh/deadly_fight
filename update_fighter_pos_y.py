import pygame
from change_fighter_position import change_position


def update_y(fighter, ground, enemy):
    # UPDATE Y
    fighter.pos_y += fighter.vector[1]
    change_position(fighter)
    if pygame.sprite.collide_rect(fighter.collision_rect, enemy.collision_rect) and\
            fighter.cur_anim not in ['throw', 'thrown'] and enemy.cur_anim not in ['throw', 'thrown']:
        fighter.pos_y -= fighter.vector[1]
        change_position(fighter)

    elif pygame.sprite.collide_rect(fighter.collision_rect, ground):
        fighter.pos_y -= fighter.vector[1]
        change_position(fighter)
        fighter.vector[1] = 0
        if not fighter.getting_damage:
            fighter.vector[0] = 0
        fighter.on_ground = 1
