from ProjetilInimigo import ProjetilInimigo
from Arma import Arma
import random, pygame

class ArmaInimigo(Arma):
    def __init__(self, nome: str, cadencia):
        super().__init__(nome, cadencia)

    def atirar(self, x: int, y: int, velocidade: int, dano: int):
        return [ProjetilInimigo(x, y, velocidade, dano)]