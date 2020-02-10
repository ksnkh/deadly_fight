def change_position(fighter, vector, f):
    if vector == [0, 0]:
        return
    if f == 'act':
        fighter.actual_coords_x += vector[0]
        fighter.actual_coords_y += vector[1]
    elif f == 'scr':
        fighter.pos_x += vector[0]
        fighter.pos_y += vector[1]
        fighter.rect.topleft = [fighter.pos_x, fighter.pos_y]
    elif f == 'all':
        fighter.actual_coords_x += vector[0]
        fighter.actual_coords_y += vector[1]
        fighter.pos_x += vector[0]
        fighter.pos_y += vector[1]
        fighter.rect.topleft = [fighter.pos_x, fighter.pos_y]