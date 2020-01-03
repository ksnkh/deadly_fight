import pygame
import os

pygame.init()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()


class Ground(pygame.sprite.Sprite):
    image = pygame.Surface([800, 150])
    image.fill(pygame.Color("gray"))

    def __init__(self, *groups, picture=False):
        super().__init__(groups)
        if picture:
            self.image = load_image(picture)
        else:
            self.image = Ground.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 450)


class Background(pygame.sprite.Sprite):
    image = pygame.Surface([800, 450])
    image.fill(pygame.Color("red"))

    def __init__(self, *groups, picture=False):
        super().__init__(groups)
        if picture:
            self.image = load_image(picture)
        else:
            self.image = Background.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


class Wall(pygame.sprite.Sprite):
    image = pygame.Surface([10, 50])
    image.fill(pygame.Color("red"))

    def __init__(self, *groups, picture=False):
        super().__init__(groups)
        if picture:
            self.image = load_image(picture)
        else:
            self.image = Wall.image
        self.image = Wall.image
        self.rect = self.image.get_rect()
        self.rect.topleft = event.pos


class Character(pygame.sprite.Sprite):
    image = pygame.Surface([100, 200])
    image.fill(pygame.Color("blue"))

    def __init__(self, walls, ground, *groups, picture=False):
        super().__init__(groups)
        if picture:
            self.image = load_image(picture)
        else:
            self.image = Character.image
        self.image = Character.image
        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 250]
        self.pos_x = 100
        self.pos_y = 250
        self.vector = [0, 0]
        self.on_ground = 0
        self.walls = walls
        self.ground = ground

    def fall(self):
        self.vector[1] += 0.3

    def move(self, shift):
        if self.on_ground:
            self.vector[0] = 4 * shift

    def jump(self):
        if self.on_ground:
            self.vector[1] -= 13
            self.on_ground = 0
            print(self.vector)

    def update_pos(self):
        self.pos_x += self.vector[0]
        self.rect.topleft = [self.pos_x, self.pos_y]
        if pygame.sprite.spritecollideany(self, self.walls):
            self.pos_x -= self.vector[0]
            self.rect.topleft = [self.pos_x, self.pos_y]
        if self.on_ground:
            self.vector[0] = 0

        self.pos_y += self.vector[1]
        self.rect.topleft = [self.pos_x, self.pos_y]
        if pygame.sprite.spritecollideany(self, self.ground):
            for i in range(int(self.vector[1] + 0.9)):
                if pygame.sprite.spritecollideany(self, self.ground):
                    self.pos_y -= 1
                    self.rect.topleft = [self.pos_x, self.pos_y]
                else:
                    break
            self.vector[1] = 0
            self.on_ground = 1


def start_game():
    all_sprites = pygame.sprite.Group()
    character = pygame.sprite.Group()
    ground = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    bground = pygame.sprite.Group()
    gr = Ground(all_sprites, ground)
    bgr = Background(all_sprites, bground)
    char = Character(walls, ground, all_sprites, character)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            pass
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            char.move(-1)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            char.move(1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            char.jump()
        char.fall()
        char.update_pos()
        screen.fill(pygame.Color("black"))
        bground.draw(screen)
        character.draw(screen)
        ground.draw(screen)
        clock.tick(fps)
        pygame.display.flip()


start_game()
pygame.quit()
exit()