import pygame, random
from Powerup import Powerup
from ArmaTripla import ArmaTripla
from Projetil import Projetil


class PowerupArmaTripla(Powerup):
    def __init__(self, center):
        super().__init__(center)
        self.image = pygame.image.load('versao_final/assets/imgs/speed.png').convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2
    
    def implementar_power(self, jogador, tempo):
        jogador.arma = ArmaTripla("Arma tripla",
                                 Projetil(0, 0, 9, 1, []), 400
                        )
        jogador.coletou_power_up(tempo)
    