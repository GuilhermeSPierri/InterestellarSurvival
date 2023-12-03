import pygame
from singleton.Configuracoes import Configuracoes


class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.rect.y += self.speedy
        config = Configuracoes()
        if self.rect.top > config.altura_tela + 50:
            self.kill()
    
    def implementar_power(self, jogador, tempo):
        pass