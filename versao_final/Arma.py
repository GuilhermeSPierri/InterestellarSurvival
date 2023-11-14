from Projetil import Projetil

class Arma:
    def __init__(self, nome: str, projetil: Projetil):
        self.__nome = nome
        self.__projetil = projetil

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

#Demais métodos

    def atirar(self):
        self.__projetil.y -= self.__projetil.velocidade

    def trocar_projetil(self):
        pass