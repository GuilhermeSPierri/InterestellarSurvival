from Projetil import Projetil
import pygame

class Arma:
    def __init__(self, nome: str, projetil: Projetil):
        self.__nome = nome
        self.__projetil = projetil
        self.__disparos = self.__disparos = pygame.sprite.Group()

# Getters e setters
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

    def atirar(self, x: int, y: int, velocidade: int, dano: int, imagem: str, sprites):
        return Projetil(x, y, velocidade, dano, imagem, sprites)
        


    """def atirar(self):
        self.__projetil.y -= self.__projetil.velocidade
"""
    def trocar_projetil(self):
        pass