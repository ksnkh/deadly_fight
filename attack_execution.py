import pygame
import sys

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

attack_Sub_Zero = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Ледяной шар': 'вниз, вперед, низкий удар',
                   'Слайд': 'назад + низкий удар ногой + высокий удар ногой',
                   'Фаталити': 'вперед, вниз, вперед, высокий удар'}

attack_Scorpion = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Ручное копье': 'назад, назад, низкий удар',
                   'Телепорт пунш': 'вниз, назад, низкий удар',
                   'Фаталити': 'вверх, вверх'}

attack_Liu_Kang = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Огненный шар': 'вперед, вперед, высокий удар',
                   'Супер удар ногой': 'вперед, вперед, высокий удар ногой',
                   'Фаталити': 'D-pad, Вперед, Вниз, Назад, Вверх'}

attack_Johnny_Cage = {'Апперкот': 'вниз + высокий удар',
                      'Подножка': 'назад + низкий удар',
                      'Удар наотмашь': 'назад + высокий удар',
                      'Бросок противника': 'вперёд, низкий удар',
                      'Теневой удар ногой': 'назад, вперед, низкий удар ногой',
                      'Энергетический шар': 'назад, вперед, вниз + высокий удар ногой',
                      'Фаталити': 'вперед, вперед, вперед, высокий удар'}

attack_Sonya = {'Апперкот': 'вниз + высокий удар',
                'Подножка': 'назад + низкий удар',
                'Удар наотмашь': 'назад + высокий удар',
                'Бросок противника': 'вперёд, низкий удар',
                'Энергетические кольца': 'высокий удар, назад, высокий удар',
                'Бросок ногой': 'вниз + низкий удар + низкий удар ногой',
                'Летящий удар': 'Вперед, Назад, Высокий Удар',
                'Фаталити': 'вперед, вперед, назад, назад, блок'}


class attack_execution():
    def __init__(self, hero_attack):
        self.points = []
        if hero_attack == 'attack_Sub_Zero':
            y = 30
            for i in attack_Sub_Zero:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Sub_Zero[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'attack_Scorpion':
            y = 30
            for i in attack_Scorpion:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Scorpion[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'attack_Liu_Kang':
            y = 30
            for i in attack_Liu_Kang:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Liu_Kang[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'attack_Johnny_Cage':
            y = 30
            for i in attack_Johnny_Cage:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Johnny_Cage[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'attack_Sonya':
            y = 30
            for i in attack_Sonya:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Sonya[i])), (128, 128, 128)])
                y += 40

    def drawing(self, surface, font_menu):
        for i in self.points:
            surface.blit(font_menu.render(i[2], 2, i[3]), (i[0], i[1]))

    def run(self):
        running = True
        font = pygame.font.SysFont('ToughSansRegular', 28)
        while running:
            self.drawing(screen, font)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == 13:
                        # возвращает предыдущее окно
                        return None
            screen.blit(screen, (0, 0))
            pygame.display.flip()
        screen.fill(pygame.Color('black'))
