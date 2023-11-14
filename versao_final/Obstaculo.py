from Personagem import Personagem
from Arma import Arma
import random

class Obstaculo:
    def __init__(self, nome: str, vidas: int, x: int, y: int, velocidade: int, imagem:str, sprites):
        self.__nome = nome
        self.__vidas = vidas
        self.__velocidade = velocidade
        self.__imagem = imagem
        self.__sprites = sprites
        self.__x = x
        self.__y = y
        self.__maximo_vidas = vidas
    
    def mover_baixo(self):
        self.__y += self.__velocidade

    def respawn(self, largura, altura=None):
        self.posicao_aleatoria(largura, altura)
        self.vidas = self.__maximo_vidas

    def posicao_aleatoria(self, largura, altura = None):
        if altura == None:
            self.y = -100
        else:
            self.y = random.randint(altura, 0)
        self.x = random.randint(1, largura-40)

    @property
    def sprites(self):
        return self.__sprites
    
    @sprites.setter
    def sprites(self, sprites):
        self.__sprites = sprites
    
    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y