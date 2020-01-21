from change_fighter_position import change_position


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, target):
        self.target = target

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        if type(obj).__name__ != 'Character':
            if self.target.rect.x > 400:
                obj.rect.x += -1
            elif self.target.rect.x < 400:
                obj.rect.x += 1
        else:
            if self.target.rect.x > 400:
                obj.pos_x += -1
            elif self.target.rect.x < 400:
                obj.pos_x += 1
            change_position(obj)


