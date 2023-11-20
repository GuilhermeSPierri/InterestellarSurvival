from Fase import Fase
from Obstaculo import Obstaculo
from Powerup import PowerUp
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
                    None,
                    Jogador("Player 1", 3, 640, 600,
                            Arma("Arma base",
                                 Projetil(0, 0, 9, 1, 'versao_final/assets/imgs/shot1_asset.png', [])
                            ),
                            6, 0, 'versao_final/assets/imgs/jogadorbase.png',
                            ['versao_final/assets/imgs/jogadorbase.png', 'versao_final/assets/imgs/jogadorbase2.png', 'versao_final/assets/imgs/jogadorbase3.png', 'versao_final/assets/imgs/jogadorbase4.png']
                    )
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
