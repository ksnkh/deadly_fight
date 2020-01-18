from change_fighter_position import change_position


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx

    def apply_to_character(self, char):
        char.pos_x += self.dx
        change_position(char)

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x - 400)
