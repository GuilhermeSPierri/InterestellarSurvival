from logica_de_jogo.projeteis.ProjetilAmarelo import ProjetilAmarelo
from logica_de_jogo.armas.Arma import Arma


class ArmaMaisDano(Arma):
    def __init__(self, nome: str, cadencia):
        super().__init__(nome, cadencia)

    def atirar(self, x: int, y: int):
        return [ProjetilAmarelo(x, y, 5, 4)]