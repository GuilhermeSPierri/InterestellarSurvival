import pygame, random
from Powerup import Powerup
from ArmaMaisDano import ArmaMaisDano
from Projetil import Projetil


class PowerupMaisDano(Powerup):
    def __init__(self, center):
        super().__init__(center)
        #self.type = random.choice(['shield', 'gun'])
        self.image = pygame.image.load('versao_final/assets/imgs/incrementar.png').convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2
    
    def implementar_power(self, jogador, tempo):
        jogador.arma = ArmaMaisDano("Arma com mais dano",
                                 Projetil(0, 0, 9, 5, []), 320
                        )
        jogador.coletou_power_up(tempo);
    