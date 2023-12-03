import pygame
from logica_de_jogo.powerups.Powerup import Powerup
from logica_de_jogo.armas.ArmaTripla import ArmaTripla
from singleton.Configuracoes import Configuracoes


class PowerupArmaTripla(Powerup):
    def __init__(self, center):
        super().__init__(center)
        config = Configuracoes()
        self.image = pygame.image.load(config.img_powerup_armatripla).convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2
    
    def implementar_power(self, jogador, tempo):
        jogador.arma = ArmaTripla("Arma tripla", 400
                        )
        jogador.coletou_power_up(tempo)
    