import pygame, random


class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        if self.type == 'shield':
            self.image = pygame.image.load('versao_final/assets/imgs/speed.png').convert()
            self.image = pygame.transform.scale(self.image, (30, 30))
        else:
             self.image = pygame.image.load('versao_final/assets/imgs/incrementar.png').convert()
             self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top > 720:
            self.kill()