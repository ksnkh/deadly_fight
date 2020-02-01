import pygame
from ground import Ground
from background import Background
from character import Character
from camera import Camera
from camera_focus import CameraFocus
from wall import Wall
from game_cycle import game_cycle
from helth_bar import HelthBar
from attack_list import AttackExecution

size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Fight:
    def __init__(self, map_name, fighter_side, your_char, enemy_char):
        self.map_name = map_name
        self.fighter_side = fighter_side
        self.your_char = your_char
        self.enemy_char = enemy_char

    def run(self):
        # CREATING SPRITE GROUPS
        all_sprites = pygame.sprite.Group()
        fighters = pygame.sprite.Group()
        ground = pygame.sprite.Group()
        bground = pygame.sprite.Group()
        cfg = pygame.sprite.Group()
        walls = pygame.sprite.Group()
        camera_walls = pygame.sprite.Group()
        char_collider_rect = pygame.sprite.Group()
        helth_bars = pygame.sprite.Group()
        alg = pygame.sprite.Group()

        # CREATING SPRITES
        gr = Ground(all_sprites, ground)
        bgr = Background(f"maps/{self.map_name}.png", all_sprites, bground)
        lw = Wall([-500, 0], walls)
        rw = Wall([800, 0], walls)
        lcw = Wall([-500, 0], all_sprites, camera_walls)
        rcw = Wall([800, 0], all_sprites, camera_walls)
        cf = CameraFocus(camera_walls, cfg)
        if self.fighter_side == 'right':
            enemy = Character(self.enemy_char, 'left', fighters, all_sprites)
            char = Character(self.your_char, 'right', fighters, all_sprites)
        else:
            char = Character(self.your_char, 'left', fighters, all_sprites)
            enemy = Character(self.enemy_char, 'right', fighters, all_sprites)
        chb = HelthBar(char, helth_bars)
        ehb = HelthBar(enemy, helth_bars)
        camera = Camera(cf)
        al = AttackExecution(self.your_char, alg)

        # game cycle
        game_cycle(screen, char, enemy, camera, cf, gr, chb, ehb, alg, all_sprites, ground, cfg, walls, char_collider_rect,
                   fighters, bground, camera_walls, helth_bars)

        screen.fill(pygame.Color('black'))
        return 'main'
