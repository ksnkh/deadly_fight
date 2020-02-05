import pygame
from background import Background
from character import Character
from camera import Camera
from camera_focus import CameraFocus
from game_cycle import game_cycle
from helth_bar import HelthBar
from attack_list import AttackExecution
import random

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
        bground = pygame.sprite.Group()
        cfg = pygame.sprite.Group()
        helth_bars = pygame.sprite.Group()
        alg = pygame.sprite.Group()

        # CREATING SPRITES
        bgr = Background(f"maps/{self.map_name}.png", all_sprites, bground)
        cf = CameraFocus(cfg)
        if self.fighter_side == 'right':
            enemy = Character(self.enemy_char, 'left', random.randint(0, 1000000), fighters, all_sprites)
            char = Character(self.your_char, 'right', random.randint(0, 1000000), fighters, all_sprites)
        else:
            char = Character(self.your_char, 'left', random.randint(0, 1000000), fighters, all_sprites)
            enemy = Character(self.enemy_char, 'right', random.randint(0, 1000000), fighters, all_sprites)
        chb = HelthBar(char, helth_bars)
        ehb = HelthBar(enemy, helth_bars)
        camera = Camera(cf)
        al = AttackExecution(self.your_char, alg)

        # game cycle
        game_cycle(screen, char, enemy, camera, cf, chb, ehb, alg, all_sprites, cfg,
                   fighters, bground, helth_bars)

        screen.fill(pygame.Color('black'))
        return 'main'
