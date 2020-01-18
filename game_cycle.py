import pygame
from char_movement import gravity, move, jump
from update_position_and_animation import update_pos_and_anim
from update_character_img import update_img

pygame.init()
pygame.mixer.init()

fall = 1
pygame.time.set_timer(fall, 10)
img_change = 2
pygame.time.set_timer(img_change, 90)
fps = 80
clock = pygame.time.Clock()


def game_cycle(screen, char, enemy, camera, cf, gr, all_sprites, ground, cfg, walls, char_collider_rect, fighters,
               bground, camera_walls):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == img_change:
                if char.rect.x <= enemy.rect.x:
                    update_img(char, 'left')
                    update_img(enemy, 'right')
                else:
                    update_img(enemy, 'left')
                    update_img(char, 'right')

        # key press processing
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            pass
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            move(char, -1)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            move(char, 1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            jump(char)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

        # char updates
        for c in fighters:
            gravity(c)
        update_pos_and_anim(char, walls, gr, enemy, True)
        update_pos_and_anim(enemy, walls, gr, char)

        # camera update
        cf.update(char.collision_rect.rect.x, enemy.collision_rect.rect.x)
        camera.update(cf)
        for s in all_sprites:
            camera.apply(s)
        for c in fighters:
            camera.apply_to_character(c)

        # drawing
        screen.fill(pygame.Color("black"))
        bground.draw(screen)
        fighters.draw(screen)
        char_collider_rect.draw(screen)
        cfg.draw(screen)
        ground.draw(screen)
        walls.draw(screen)
        camera_walls.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
