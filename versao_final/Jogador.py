from typing import Any
from Personagem import Personagem
from Arma import Arma
import pygame

class Jogador(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, pontos: int, image:str, sprites):
        super().__init__(nome, vidas, x, y, arma, velocidade, image, sprites)
        self.__pontos= pontos
        self.__contador = 0

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos
    
    def diminuir_pontos(self, valor):
        if (self.__pontos - valor) < 0:
            self.__pontos = 0
        else:
            self.__pontos -= valor
    def update(self):
        #sprite basico
        if self.__contador >= len(self.sprites):
            self.__contador = 0
        else:
            self.__contador += 1
        
        self.image = pygame.image.load(self.sprites[self.__contador-1]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, 90)
            
