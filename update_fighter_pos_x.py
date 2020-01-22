import pygame
from change_fighter_position import change_position


def update_x(fighter, walls, enemy, f=False):
    if not f:
        print(fighter.pos_x)
    # UPDATE X
    fighter.pos_x += fighter.vector[0]
    change_position(fighter)

    # WALL COLLISION
    if pygame.sprite.spritecollideany(fighter.collision_rect, walls) or \
            pygame.sprite.spritecollideany(enemy.collision_rect, walls):
        print('wall')
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
        print('char')
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

    if not f:
        print(fighter.pos_x)
        print('-----------------')
