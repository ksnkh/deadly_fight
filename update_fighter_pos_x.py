import pygame
from change_fighter_position import change_position


def update_x(fighter, walls, enemy):
    # UPDATE X
    fighter.pos_x += fighter.vector[0]
    change_position(fighter)

    # WALL COLLISION
    if pygame.sprite.spritecollideany(fighter.collision_rect, walls) or \
            pygame.sprite.spritecollideany(enemy.collision_rect, walls):
        if fighter.side == 'left':
            shift = 1
        else:
            shift = -1
        while pygame.sprite.spritecollideany(fighter.collision_rect, walls):
            fighter.pos_x += shift
            change_position(fighter)
        fighter.vector[0] = 0

    # CHAR COLLISION
    if pygame.sprite.collide_rect(fighter.collision_rect, enemy.collision_rect):
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
