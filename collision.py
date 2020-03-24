from apply_damage import apply_damage


def collision(sprite1, sprite2):
    if type(sprite1).__name__ == 'Character' and sprite1.damage and not sprite1.hit:
        sprite1.hit = True
        return sprite1.curent_animation_settings[5]
