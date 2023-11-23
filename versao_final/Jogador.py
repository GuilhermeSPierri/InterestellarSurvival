from typing import Any
from Personagem import Personagem
from Arma import Arma
import pygame

class Jogador(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, pontos: int, image:str, sprites):
        super().__init__(nome, vidas, x, y, arma, velocidade, image, sprites)
        self.__arma_base = arma
        self.__pontos= pontos
        self.__contador = 0
        self.__power = 0


    @property
    def arma_base(self):
        return self.__arma_base
    
    @arma_base.setter
    def arma_base(self, arma_base):
        self.__arma_base = arma_base

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
    
    def coletou_power_up(self, tempo):
        self.__power = tempo

    def update(self):
        #sprite basico
        if self.__contador >= len(self.sprites):
            self.__contador = 0
        else:
            self.__contador += 1

        if pygame.time.get_ticks() - self.__power > 20000:
            self.arma = self.__arma_base
            self.__power = 0
        
        self.image = pygame.image.load(self.sprites[self.__contador-1]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, 90)
            
