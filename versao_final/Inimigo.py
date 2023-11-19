from Personagem import Personagem
from Arma import Arma
import random, pygame

class Inimigo(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, image:str, sprites):
        super().__init__(nome, vidas, x, y, arma, velocidade, image, sprites)
        self.__maximo_vidas = vidas

    def respawn(self, largura, altura=None):
        self.posicao_aleatoria(largura, altura)
        self.vidas = self.__maximo_vidas

    def posicao_aleatoria(self, largura, altura = None):
        if altura == None:
            self.y = -100
        else:
            self.y = random.randint(altura, 0)
        self.x = random.randint(1, largura-40)