def update_anim(fighter):
    if fighter.getting_damage:
        return

    elif fighter.dead:
        if fighter.cur_anim != 'dead':
            fighter.set_anim('dead')

    elif fighter.attack:
        if fighter.attack == 'high_punch' and fighter.cur_anim != 'high_punch' and fighter.on_ground:
            if fighter.cur_anim == 'duck' and fighter.cur_anim != 'uppercut':
                fighter.set_anim('uppercut')
            elif fighter.cur_anim != 'duck' and fighter.cur_anim != 'uppercut':
                fighter.set_anim('high_punch')

        if fighter.attack == 'low_punch' and fighter.cur_anim != 'low_punch' and fighter.on_ground:
            if fighter.previos_moves:
                if len(fighter.previos_moves) >= 2:
                    if fighter.previos_moves[-2][0] == 'duck' and fighter.previos_moves[-1][0] == 'walk_b' \
                            and fighter.cur_anim != 'teleport' and fighter.name == 'Scorpion':
                        fighter.set_anim('teleport')
                if fighter.previos_moves[-1][0] == 'walk_f' and fighter.cur_anim != 'throw' and fighter.cur_anim != 'teleport':
                    fighter.set_anim('throw')
            elif fighter.cur_anim != 'throw':
                fighter.set_anim('low_punch')

        if fighter.attack == 'high_kick' and fighter.cur_anim != 'high_kick' and fighter.on_ground:
            if fighter.previos_moves:
                if fighter.previos_moves[-1][0] == 'walk_b' and fighter.cur_anim != 'roundhouse':
                    fighter.set_anim('roundhouse')
                if fighter.previos_moves[-1][0] == 'sweep_kick' and fighter.cur_anim != 'slide' and fighter.name == 'Sub-Zero':
                    fighter.set_anim('slide')
            elif fighter.cur_anim != 'roundhouse':
                fighter.set_anim('high_kick')

        if fighter.attack == 'low_kick' and fighter.cur_anim != 'low_kick':
            if fighter.previos_moves:
                if len(fighter.previos_moves) >= 2:
                    if fighter.previos_moves[-2][0] == 'duck' and fighter.previos_moves[-1][0] == 'walk_f' \
                            and fighter.cur_anim != 'leg_throw' and fighter.name == 'Sonya':
                        fighter.set_anim('leg_throw')
                if fighter.previos_moves[-1][0] == 'walk_b' and fighter.cur_anim != 'sweep_kick':
                    fighter.set_anim('sweep_kick')
            if not fighter.on_ground and fighter.cur_anim != 'air_kick' and fighter.cur_anim != 'sweep_kick':
                fighter.set_anim('air_kick')
            elif fighter.cur_anim != 'sweep_kick' and fighter.on_ground and fighter.cur_anim != 'leg_throw':
                fighter.set_anim('low_kick')

    else:
        if fighter.on_ground and fighter.ducked and fighter.cur_anim != 'duck':
            fighter.set_anim('duck')

        elif fighter.on_ground and not fighter.ducked and fighter.cur_anim == 'duck' and fighter.cur_frame == 2:
            fighter.cur_frame = 3

        elif fighter.on_ground and fighter.block and fighter.cur_anim != 'block':
            fighter.set_anim('block')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'walk_f' and fighter.on_ground and\
                (fighter.vector[0] > 0 and fighter.side == 'left' or fighter.vector[0] < 0 and fighter.side == 'right')\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('walk_f')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'walk_b' and fighter.on_ground and\
                (fighter.vector[0] < 0 and fighter.side == 'left' or fighter.vector[0] > 0 and fighter.side == 'right')\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('walk_b')

        elif fighter.vector[
            0] == 0 and fighter.cur_anim != 'stand' and fighter.cur_anim != 'duck' and fighter.on_ground\
                and not fighter.block and not fighter.attack:
            fighter.set_anim('stand')

        elif fighter.vector[
            0] == 0 and fighter.cur_anim != 'jump' and not fighter.on_ground\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('jump')

        elif fighter.vector[0] != 0 and fighter.cur_anim != 'move_jump' and not fighter.on_ground\
                and not fighter.block and not fighter.ducked:
            fighter.set_anim('move_jump')
