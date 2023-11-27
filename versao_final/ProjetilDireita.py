from Projetil import Projetil
from Configuracoes import Configuracoes
import pygame


class ProjetilDireita(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        config = Configuracoes()
        self.image = pygame.image.load(config.img_projetil_verde)
        self.image = pygame.transform.rotate(self.image, 70)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        # Movimentar o projétil
        if self.y <= 0:
            self.kill()
        else:
            self.rect.y -= self.velocidade
            self.rect.x += self.velocidade