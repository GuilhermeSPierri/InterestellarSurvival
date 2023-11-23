from Projetil import Projetil
import random, pygame

class ProjetilEsquerda(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        self.image = pygame.image.load("versao_final/assets/imgs/shot1_asset.png")
        self.image = pygame.transform.rotate(self.image, 110)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        # Movimentar o projétil
        if self.y <= 0:
            self.kill()
        else:
            self.rect.y -= self.velocidade
            self.rect.x -= self.velocidade