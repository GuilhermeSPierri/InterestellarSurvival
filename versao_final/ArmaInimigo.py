from ProjetilInimigo import ProjetilInimigo
from Arma import Arma
import random, pygame

class ArmaInimigo(Arma):
    def __init__(self, nome: str, projetil: ProjetilInimigo):
        super().__init__(nome, projetil)

    def atirar(self, x: int, y: int, velocidade: int, dano: int, imagem: str, sprites):
        return ProjetilInimigo(x, y, velocidade, dano, imagem, sprites)