import pygame
import sys

pygame.init()
pygame.mixer.init()

attack_Sub_Zero = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Слайд': 'назад + низкий удар ногой + высокий удар ногой'}

attack_Scorpion = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Телепорт': 'вниз, назад, низкий удар'}

attack_Liu_Kang = {'Апперкот': 'вниз + высокий удар',
                   'Подножка': 'назад + низкий удар',
                   'Удар наотмашь': 'назад + высокий удар',
                   'Бросок противника': 'вперёд, низкий удар',
                   'Супер удар ногой': 'вниз, вперед, высокий удар ногой'}

attack_Johnny_Cage = {'Апперкот': 'вниз + высокий удар',
                      'Подножка': 'назад + низкий удар',
                      'Удар наотмашь': 'назад + высокий удар',
                      'Бросок противника': 'вперёд, низкий удар',
                      'Теневой удар ногой': 'назад, вперед, низкий удар ногой'}

attack_Sonya = {'Апперкот': 'вниз + высокий удар',
                'Подножка': 'назад + низкий удар',
                'Удар наотмашь': 'назад + высокий удар',
                'Бросок противника': 'вперёд, низкий удар',
                'Бросок ногой': 'вниз + низкий удар + низкий удар ногой'}


class AttackExecution(pygame.sprite.Sprite):
    def __init__(self, hero_attack, g):
        super().__init__(g)
        self.image = pygame.Surface([800, 600])
        self.image.fill(pygame.Color("#000000"))
        self.points = []
        if hero_attack == 'Sub-Zero':
            y = 30
            for i in attack_Sub_Zero:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Sub_Zero[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'Scorpion':
            y = 30
            for i in attack_Scorpion:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Scorpion[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'Liu Kang':
            y = 30
            for i in attack_Liu_Kang:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Liu_Kang[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'Johnny Cage':
            y = 30
            for i in attack_Johnny_Cage:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Johnny_Cage[i])), (128, 128, 128)])
                y += 40
        elif hero_attack == 'Sonya':
            y = 30
            for i in attack_Sonya:
                self.points.append([30, y, (str(i) + ': ' + str(attack_Sonya[i])), (128, 128, 128)])
                y += 40

        font = pygame.font.SysFont('ToughSansRegular', 28)
        for i in self.points:
            self.image.blit(font.render(i[2], 2, i[3]), (i[0], i[1]))
        self.image.set_alpha(200)
        self.rect = self.image.get_rect()
