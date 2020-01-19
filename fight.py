import pygame
from ground import Ground
from background import Background
from character import Character
from camera import Camera
from camera_focus import CameraFocus
from wall import Wall
from char_colide_sprite import ColisionRect
from game_cycle import game_cycle

size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Fight:
    def __init__(self, map_name, fighter_side, your_char, enemy_char):
        self.map_name = map_name
        self.fighter_side = fighter_side
        self.your_char = your_char
        self.enemy_char = enemy_char

    def run(self):
        all_sprites = pygame.sprite.Group()
        fighters = pygame.sprite.Group()
        ground = pygame.sprite.Group()
        bground = pygame.sprite.Group()
        cfg = pygame.sprite.Group()
        walls = pygame.sprite.Group()
        camera_walls = pygame.sprite.Group()
        char_collider_rect = pygame.sprite.Group()

        gr = Ground(all_sprites, ground)
        bgr = Background(f"maps/{self.map_name}.jpg", all_sprites, bground)
        lw = Wall([-400, 0], walls)
        rw = Wall([800, 0], walls)
        lcw = Wall([-400, 0], all_sprites, camera_walls)
        rcw = Wall([800, 0], all_sprites, camera_walls)
        lccr = ColisionRect([135, 340], char_collider_rect)
        rccr = ColisionRect([635, 340], char_collider_rect)
        if self.fighter_side == 'right':
            enemy = Character(self.enemy_char, 'left', rccr, fighters)
            char = Character(self.your_char, 'right', lccr, fighters)
        else:
            char = Character(self.your_char, 'left', rccr, fighters)
            enemy = Character(self.enemy_char, 'right', lccr, fighters)
        camera = Camera()
        cf = CameraFocus(camera_walls, cfg, all_sprites)

        # game cycle
        game_cycle(screen, char, enemy, camera, cf, gr, all_sprites, ground, cfg, walls, char_collider_rect, fighters,
                   bground, camera_walls)

        screen.fill(pygame.Color('black'))
        return 'main'
