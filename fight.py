import pygame
from ground import Ground
from background import Background
from character import Character
from camera import Camera
from camera_focus import CameraFocus
from wall import Wall


pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()


class Fight:
    def __init__(self):
        pass

    def run(self):
        all_sprites = pygame.sprite.Group()
        character = pygame.sprite.Group()
        ground = pygame.sprite.Group()
        bground = pygame.sprite.Group()
        cfg = pygame.sprite.Group()
        walls = pygame.sprite.Group()

        gr = Ground(all_sprites, ground)
        bgr = Background(all_sprites, bground, picture='maps/1.jpg')
        lw = Wall([-450, 0], all_sprites, walls)
        rw = Wall([1250, 0], all_sprites, walls)
        enemy = Character(walls, ground, 'right', character)
        char = Character(walls, ground, 'left', character)
        camera = Camera()
        cf = CameraFocus(cfg, all_sprites)
        # game cycle
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
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
            # updates
            for c in character:
                c.fall()
                c.update_pos()
            cf.update(char.rect.x, enemy.rect.x)
            camera.update(cf)
            for s in all_sprites:
                camera.apply(s)
            for c in character:
                camera.apply_to_character(c)
            # drawing
            screen.fill(pygame.Color("black"))
            bground.draw(screen)
            character.draw(screen)
            cfg.draw(screen)
            ground.draw(screen)
            walls.draw(screen)
            clock.tick(fps)
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
        return 'main'
