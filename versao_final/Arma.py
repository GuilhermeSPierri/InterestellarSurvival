from Projetil import Projetil
from Configuracoes import Configuracoes
import pygame

class Arma:
    def __init__(self, nome: str, cadencia):
        self.__nome = nome
        self.__cadencia = cadencia
        self.__disparos = pygame.sprite.Group()
        
# Getters e setters
    @property
    def cadencia(self):
        return self.__cadencia
    
    @cadencia.setter
    def cadencia(self, cadencia):
        self.__cadencia = cadencia
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def disparos(self):
        return self.__disparos
    
    @disparos.setter
    def disparos(self, disparos):
        self.__disparos = disparos

    def atirar(self, x: int, y: int):
        return [Projetil(x, y, 5, 1)]
        