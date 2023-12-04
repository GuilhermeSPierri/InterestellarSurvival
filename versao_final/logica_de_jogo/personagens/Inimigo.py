from logica_de_jogo.personagens.Personagem import Personagem
from logica_de_jogo.armas.Arma import Arma
import random


class Inimigo(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, image:str):
        super().__init__(nome, vidas, x, y, arma, velocidade, image)
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
        
    def mover(self):
        self.y += self.velocidade