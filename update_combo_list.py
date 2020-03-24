def update_combo_list(fighter):
    for m in fighter.previos_moves:
        m[1] += 1
        if m[1] == 15:
            fighter.previos_moves.remove(m)
