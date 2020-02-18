import pygame
from char_movement import gravity, move, jump
from update_position_and_animation import update_pos_and_anim
from update_character_img import update_img
from update_combo_list import update_combo_list
from collision import collision
import pickle

pygame.init()
pygame.mixer.init()

fall = 1
pygame.time.set_timer(fall, 10)
clean_combo_list = 3
pygame.time.set_timer(clean_combo_list, 100)
camera_update = 4
fps = 80
clock = pygame.time.Clock()


def game_cycle(fight_settings):
    img_change = 0
    show_attack_list = False
    endgame = False
    endgame_timer = 0
    debug = 0
    while fight_settings.running:
        print(debug)
        debug += 1
        for event in pygame.event.get():
            if event.type == fall:
                for c in fight_settings.fighters:
                    gravity(c)

            if event.type == pygame.QUIT:
                fight_settings.running = False
                fight_settings.client_socket.send(pickle.dumps(['exit']))

            if event.type == clean_combo_list:
                for c in fight_settings.fighters:
                    update_combo_list(c)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if show_attack_list:
                        show_attack_list = False
                    else:
                        show_attack_list = True

                if event.key == pygame.K_y:
                    fight_settings.char.attack = 'low_punch'
                elif event.key == pygame.K_u:
                    fight_settings.char.attack = 'high_punch'
                elif event.key == pygame.K_i:
                    fight_settings.char.attack = 'low_kick'
                elif event.key == pygame.K_o:
                    fight_settings.char.attack = 'high_kick'
                elif fight_settings.char.cur_anim not in fight_settings.char.attack_animations:
                    fight_settings.char.attack = False

        # key press processing
        if not fight_settings.char.dead:
            if pygame.key.get_pressed()[pygame.K_a]:
                move(fight_settings.char, -1)

            if pygame.key.get_pressed()[pygame.K_d]:
                move(fight_settings.char, 1)

            if pygame.key.get_pressed()[pygame.K_w]:
                jump(fight_settings.char)

            if pygame.key.get_pressed()[pygame.K_s] and fight_settings.char.on_ground and not fight_settings.char.block:
                fight_settings.char.ducked = True
            else:
                fight_settings.char.ducked = False

            if pygame.key.get_pressed()[pygame.K_SPACE] and fight_settings.char.on_ground and not fight_settings.char.ducked:
                fight_settings.char.block = True
            else:
                fight_settings.char.block = False

        # char updates
        update_pos_and_anim(fight_settings.char, fight_settings.enemy, True)
        if img_change == 8:
            if fight_settings.char.pos_x <= fight_settings.enemy.pos_x:
                update_img(fight_settings.char, fight_settings.enemy, 'left', fight_settings.cf, True)
            else:
                update_img(fight_settings.char, fight_settings.enemy, 'right', fight_settings.cf, True)
            img_change = 0
        else:
            img_change += 1
        try:
            fight_settings.client_socket.send(pickle.dumps(['update', fight_settings.char.actual_coords_x,
                                                        fight_settings.char.actual_coords_y, fight_settings.char.cur_anim,
                                                        fight_settings.char.helth, fight_settings.char.cur_frame,
                                                        fight_settings.char.turn, fight_settings.char.side,
                                                        fight_settings.char.rect.width, fight_settings.char.rect.height]))
        except ConnectionResetError:
            break
        if pygame.sprite.collide_mask(fight_settings.char, fight_settings.enemy):
            effect = collision(fight_settings.char, fight_settings.enemy)
            if effect is not None:
                fight_settings.client_socket.send(pickle.dumps(['get damage', effect]))

        for hb in fight_settings.helth_bars:
            hb.update_helth_bar()

        # camera update
        if fight_settings.char.side == 'right':
            fight_settings.cf.update(fight_settings.char.actual_coords_x + fight_settings.char.rect.width,
                                     fight_settings.enemy.actual_coords_x)
        else:
            fight_settings.cf.update(fight_settings.char.actual_coords_x,
                                     fight_settings.enemy.actual_coords_x + fight_settings.enemy.rect.width)
        for i in range(3):
            for s in fight_settings.all_sprites:
                fight_settings.camera.apply(s)
            fight_settings.camera.apply(fight_settings.cf)

        if fight_settings.char.dead or fight_settings.enemy.dead:
            endgame = True

        if endgame_timer == 100:
            fight_settings.client_socket.send(pickle.dumps(['end game']))

        # drawing
        fight_settings.screen.fill(pygame.Color("black"))
        fight_settings.bground.draw(fight_settings.screen)
        fight_settings.screen.unlock()
        fight_settings.char.image.unlock()
        fight_settings.screen.blit(fight_settings.char.image, fight_settings.char.rect.topleft)
        fight_settings.enemy.image.unlock()
        fight_settings.screen.blit(fight_settings.enemy.image, fight_settings.enemy.rect.topleft)
        fight_settings.cfg.draw(fight_settings.screen)
        fight_settings.helth_bars.draw(fight_settings.screen)
        if show_attack_list:
            fight_settings.alg.draw(fight_settings.screen)
        if endgame:
            res = pygame.Surface([800, 600])
            res.fill(pygame.Color("black"))
            res.set_alpha(180)
            font = pygame.font.SysFont('RomanD', 100)
            if fight_settings.char.dead:
                text = font.render('Поражение', 0, (200, 128, 128))
            elif fight_settings.enemy.dead:
                text = font.render('Победа', 0, (128, 200, 128))
            res.blit(text, [250, 200])
            fight_settings.screen.blit(res, [0, 0])
            endgame_timer += 1
        clock.tick(fps)
        pygame.display.flip()
    return