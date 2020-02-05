def change_position(fighter, vector, f=False):
    if vector == [0, 0]:
        return
    fighter.pos_x += vector[0]
    fighter.pos_y += vector[1]
    fighter.rect.topleft = [fighter.pos_x, fighter.pos_y]
    fighter.actual_coords_x += vector[0]
    fighter.actual_coords_y += vector[1]
