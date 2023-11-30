from Projetil import Projetil
from ProjetilEsquerda import ProjetilEsquerda
from ProjetilDireita import ProjetilDireita
from Arma import Arma
import random, pygame


class ArmaTripla(Arma):
    def __init__(self, nome: str, cadencia):
        super().__init__(nome, cadencia)

    def atirar(self, x: int, y: int):
        return [ProjetilEsquerda(x, y, 5, 1),
                Projetil(x, y, 5, 1),
                ProjetilDireita(x, y, 5, 1)
                ]