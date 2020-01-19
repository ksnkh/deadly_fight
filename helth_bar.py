import pygame


class HelthBar(pygame.sprite.Sprite):
    def __init__(self, fighter, *groups):
        super().__init__(*groups)
        self.fighter = fighter
        self.side = fighter.side
        self.update_helth_bar()

    def update_helth_bar(self):
        helth_bar = pygame.Surface([300, 20])
        helth_bar.fill(pygame.Color('#ff0000'))
        if self.is_dead():
            helth = pygame.Surface([0, 20])
        else:
            helth = pygame.Surface([self.fighter.helth, 20])
        helth.fill(pygame.Color('#00cc00'))
        font = pygame.font.Font(None, 30)
        text = font.render(self.fighter.name, 1, (255, 255, 100))

        if self.side == 'right':
            helth_bar.blit(helth, (300 - self.fighter.helth, 0))
            helth_bar.blit(text, (300 - 10 - text.get_width(), 2))
            self.image = helth_bar
            self.rect = self.image.get_rect()
            self.rect.topleft = (490, 30)

        else:
            helth_bar.blit(helth, (0, 0))
            helth_bar.blit(text, (10, 2))
            self.image = helth_bar
            self.rect = self.image.get_rect()
            self.rect.topleft = (10, 30)

    def is_dead(self):
        if self.fighter.helth <= 0:
            return True
        return False
