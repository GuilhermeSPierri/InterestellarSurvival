from logica_de_jogo.projeteis.Projetil import Projetil
from logica_de_jogo.projeteis.ProjetilEsquerda import ProjetilEsquerda
from logica_de_jogo.projeteis.ProjetilDireita import ProjetilDireita
from logica_de_jogo.armas.Arma import Arma


class ArmaTripla(Arma):
    def __init__(self, nome: str, cadencia):
        super().__init__(nome, cadencia)

    def atirar(self, x: int, y: int):
        return [ProjetilEsquerda(x, y, 5, 1),
                Projetil(x, y, 5, 1),
                ProjetilDireita(x, y, 5, 1)
                ]