from Projetil import Projetil
from ProjetilAmarelo import ProjetilAmarelo
from Arma import Arma
import random, pygame

class ArmaMaisDano(Arma):
    def __init__(self, nome: str, projetil: Projetil, cadencia):
        super().__init__(nome, projetil, cadencia)

    def atirar(self, x: int, y: int):
        return [ProjetilAmarelo(x, y, 5, 4, [])]