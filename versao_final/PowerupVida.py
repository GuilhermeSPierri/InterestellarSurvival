import pygame, random
from Powerup import Powerup


class PowerupVida(Powerup):
    def __init__(self, center):
        super().__init__(center)
        #self.type = random.choice(['shield', 'gun'])
        self.image = pygame.image.load('versao_final/assets/imgs/coracao.png').convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2
    
    def implementar_power(self, jogador, tempo):
        if jogador.vidas < 5:
            jogador.vidas += 1
    