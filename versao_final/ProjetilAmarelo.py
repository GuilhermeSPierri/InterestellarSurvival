from Projetil import Projetil
import random, pygame

class ProjetilAmarelo(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        self.image = pygame.image.load("versao_final/assets/imgs/projetil_amarelo.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect(center = (x, y))
