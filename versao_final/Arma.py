from Projetil import Projetil
import pygame

class Arma:
    def __init__(self, nome: str, projetil: Projetil, cadencia):
        self.__nome = nome
        self.__projetil = projetil
        self.__cadencia = cadencia
        self.__disparos = self.__disparos = pygame.sprite.Group()

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
    def projetil(self):
        return self.__projetil
    
    @projetil.setter
    def projetil(self, projetil):
        self.__projetil = projetil
    
    @property
    def disparos(self):
        return self.__disparos
    
    @disparos.setter
    def disparos(self, disparos):
        self.__disparos = disparos

    def atirar(self, x: int, y: int):
        return [Projetil(x, y, 5, 1, [])]
        


    """def atirar(self):
        self.__projetil.y -= self.__projetil.velocidade
"""
    def trocar_projetil(self):
        pass