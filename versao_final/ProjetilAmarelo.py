from Projetil import Projetil
from Configuracoes import Configuracoes
import pygame


class ProjetilAmarelo(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        config = Configuracoes()
        self.image = pygame.image.load(config.img_projetil_amarelo)
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect(center = (x, y))
