def change_position(fighter):
    fighter.rect.topleft = [fighter.pos_x, fighter.pos_y]
    fighter.collision_rect.rect.topleft = [fighter.pos_x + fighter.collision_rect.offset, fighter.pos_y]
    fighter.actual_coords_x = fighter.pos_x
    fighter.actual_coords_y = fighter.pos_y
