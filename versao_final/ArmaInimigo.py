from ProjetilInimigo import ProjetilInimigo
from Arma import Arma
import random, pygame

class ArmaInimigo(Arma):
    def __init__(self, nome: str, projetil: ProjetilInimigo, cadencia):
        super().__init__(nome, projetil, cadencia)

    def atirar(self, x: int, y: int, velocidade: int, dano: int, sprites):
        return [ProjetilInimigo(x, y, velocidade, dano, sprites)]