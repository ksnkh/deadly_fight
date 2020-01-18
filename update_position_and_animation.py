from update_fighter_pos_x import update_x
from update_fighter_pos_y import update_y


def update_pos_and_anim(fighter, walls, ground, enemy, f=False):
    if fighter.vector[0] != 0 and fighter.cur_anim != 'walk' and fighter.on_ground and not fighter.ducked:
        fighter.set_anim('walk')
        if fighter.vector[0] < 0 and fighter.side == 'left' or fighter.vector[0] > 0 and fighter.side == 'right':
            fighter.frames.reverse()
    if fighter.vector[0] == 0 and fighter.cur_anim != 'stand' and fighter.on_ground and not fighter.ducked:
        fighter.set_anim('stand')
    if fighter.vector[0] == 0 and fighter.cur_anim != 'jump' and not fighter.on_ground and not fighter.ducked:
        fighter.set_anim('jump')
    if fighter.vector[0] != 0 and fighter.cur_anim != 'move_jump' and not fighter.on_ground:
        fighter.set_anim('move_jump')
    if fighter.on_ground and fighter.ducked and fighter.cur_anim != 'duck' and fighter.on_ground:
        fighter.set_anim('duck')
    if fighter.on_ground and not fighter.ducked and fighter.cur_anim == 'duck':
        fighter.set_anim('stand')

    update_x(fighter, walls, enemy)
    update_y(fighter, ground, enemy)
