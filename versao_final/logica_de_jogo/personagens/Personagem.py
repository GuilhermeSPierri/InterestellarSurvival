from abc import ABC
from logica_de_jogo.armas.Arma import Arma
import pygame


class Personagem(pygame.sprite.Sprite, ABC):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, image: str):
        super().__init__()
        self.__nome = nome
        self.__vidas = vidas
        self.__x = x
        self.__y = y
        self.__arma = arma
        self.__velocidade = velocidade
        self.__image = image
        self.__rect = None

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas

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

    @property
    def arma(self):
        return self.__arma
    
    @arma.setter
    def arma(self, arma):
        self.__arma = arma

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
