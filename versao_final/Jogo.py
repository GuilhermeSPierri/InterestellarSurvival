from Fase import Fase
from Obstaculo import Obstaculo
from Powerup import Powerup
from Arma import Arma
from ArmaInimigo import ArmaInimigo
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo

class Jogo:
    def __init__(self):
        self.__fases = [
            Fase(
                    [],
                    None,
                    None,
                    [],
                    None
                )
        ]
        
    @property
    def fases(self):
        return self.__fases
    
    @fases.setter
    def fases(self, fases):
        self.__fases = fases
    
    def iniciar_jogo(self):
        self.__fases[0].iniciar()
