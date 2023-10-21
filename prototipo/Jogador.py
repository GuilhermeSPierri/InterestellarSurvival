from Personagem import Personagem
from Arma import Arma

class Jogador(Personagem):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, pontos: int, imagem:str):
        super().__init__(nome, vidas, x, y, arma, velocidade, imagem)
        self.__pontos= pontos

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos
