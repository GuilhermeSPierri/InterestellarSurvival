from Projetil import Projetil
from Arma import Arma
import random, pygame

class ProjetilInimigo(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, imagem: str, sprites):
        super().__init__(x, y, velocidade, dano, imagem, sprites)

    def update(self, largura):
        # Movimentar o projétil
        if self.y >= largura:
            self.kill()
        else:
            self.rect.y += self.velocidade