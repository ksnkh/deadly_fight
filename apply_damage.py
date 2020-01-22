from set_char_anim import set_char_anim


def apply_damage(char, effect):
    if not char.block:
        set_char_anim(char, effect[1])
        char.getting_damage = True
    char.get_damage(effect[2])
    char.vector = effect[3].copy()
    if char.side == 'left':
        char.vector[0] *= -1
