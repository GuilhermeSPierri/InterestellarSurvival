from logica_de_jogo.projeteis.ProjetilInimigo import ProjetilInimigo
from logica_de_jogo.armas.Arma import Arma


class ArmaInimigo(Arma):
    def __init__(self, nome: str, cadencia):
        super().__init__(nome, cadencia)

    def atirar(self, x: int, y: int, velocidade: int, dano: int):
        return [ProjetilInimigo(x, y, velocidade, dano)]