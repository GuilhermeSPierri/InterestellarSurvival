from Personagem import Personagem
from Arma import Arma
import random

class Inimigo(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, imagem:str):
        super().__init__(nome, vidas, x, y, arma, velocidade, imagem)
        self.__maximo_vidas = vidas

    def respawn(self, largura):
        self.posicao_aleatoria(largura)
        self.vidas = self.__maximo_vidas

    def posicao_aleatoria(self, largura, altura = None):
        if altura == None:
            self.y = -100
        else:
            self.y = random.randint(altura, 0)
        self.x = random.randint(1, largura-40)