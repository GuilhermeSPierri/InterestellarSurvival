from Projetil import Projetil
from Configuracoes import Configuracoes
import pygame

class ProjetilInimigo(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        config = Configuracoes()
        self.image = pygame.image.load(config.img_projetil_inimigo)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, largura):
        # Movimentar o projétil
        if self.y >= largura:
            self.kill()
        else:
            self.rect.y += self.velocidade