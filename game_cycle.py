import pygame
from char_movement import gravity, move, jump
from update_position_and_animation import update_pos_and_anim
from update_character_img import update_img
from update_combo_list import update_combo_list
from collision import collision
from subzero_animations_settings import subzero_attack_animations

pygame.init()
pygame.mixer.init()

fall = 1
pygame.time.set_timer(fall, 10)
img_change = 2
pygame.time.set_timer(img_change, 90)
clean_combo_list = 3
pygame.time.set_timer(clean_combo_list, 100)
camera_update = 4
fps = 80
clock = pygame.time.Clock()


def game_cycle(screen, char, enemy, camera, cf, gr, chb, ehb, alg, all_sprites, ground, cfg, walls, char_collider_rect, fighters,
               bground, camera_walls, helth_bars):
    show_attack_list = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == fall:
                for c in fighters:
                    gravity(c)

            if event.type == pygame.QUIT:
                running = False

            if event.type == img_change:
                if char.pos_x <= enemy.pos_x:
                    update_img(char, 'left', True)
                    update_img(enemy, 'right')
                else:
                    update_img(enemy, 'left')
                    update_img(char, 'right', True)

            if event.type == clean_combo_list:
                for c in fighters:
                    update_combo_list(c)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if show_attack_list:
                        show_attack_list = False
                    else:
                        show_attack_list = True

                if event.key == pygame.K_y:
                    char.attack = 'low_punch'
                elif event.key == pygame.K_u:
                    char.attack = 'high_punch'
                elif event.key == pygame.K_i:
                    char.attack = 'low_kick'
                elif event.key == pygame.K_o:
                    char.attack = 'high_kick'
                elif char.cur_anim not in char.attack_animations:
                    char.attack = False

        # key press processing
        if pygame.key.get_pressed()[pygame.K_s] and char.on_ground and not char.block:
            char.ducked = True
        else:
            char.ducked = False

        if pygame.key.get_pressed()[pygame.K_SPACE] and char.on_ground and not char.ducked:
            char.block = True
        else:
            char.block = False

        if pygame.key.get_pressed()[pygame.K_a]:
            move(char, -1)

        if pygame.key.get_pressed()[pygame.K_d]:
            move(char, 1)

        if pygame.key.get_pressed()[pygame.K_w]:
            jump(char)


        # char updates
        update_pos_and_anim(char, walls, gr, enemy, True)
        update_pos_and_anim(enemy, walls, gr, char)
        if pygame.sprite.collide_mask(char, enemy):
            collision(char, enemy)

        for hb in helth_bars:
            hb.update_helth_bar()

        # camera update
        for i in range(2):
            if char.cur_anim not in subzero_attack_animations and enemy.cur_anim not in subzero_attack_animations:
                if char.side == 'right':
                    cf.update(char.pos_x + char.rect.width, enemy.pos_x)
                else:
                    cf.update(char.pos_x, enemy.pos_x + enemy.rect.width)
            for s in all_sprites:
                camera.apply(s)
            camera.apply(cf)

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
        if show_attack_list:
            alg.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
