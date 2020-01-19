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


def game_cycle(screen, char, enemy, camera, cf, gr, chb, ehb, all_sprites, ground, cfg, walls, char_collider_rect, fighters,
               bground, camera_walls, helth_bars):
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
        if pygame.key.get_pressed()[pygame.K_DOWN] and char.on_ground:
            char.ducked = True
        else:
            char.ducked = False
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
        if pygame.sprite.collide_mask(char, enemy):
            print(1)

        for hb in helth_bars:
            hb.update_helth_bar()

        # camera update
        if char.side == 'left':
            cf.update(char.rect.x + 200, enemy.rect.x)
        else:
            cf.update(char.rect.x, enemy.rect.x + 200)
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
        helth_bars.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
