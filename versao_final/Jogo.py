from Fase import Fase
from Obstaculo import Obstaculo
from Powerup import PowerUp
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo

class Jogo:
    def __init__(self):
        self.__fases = []
        
    @property
    def fases(self):
        return self.__fases
    
    @fases.setter
    def fases(self, fases):
        self.__fases = fases
    
    def iniciar_jogo(self):
        fase1 = Fase(
                    [
                        Obstaculo("Meteoro 1", 1, 640, -100, 4, 'versao_final/assets/imgs/meteor.png', None),
                        Obstaculo("Meteoro 2", 2, 640, -100, 5, 'versao_final/assets/imgs/meteor2.png', None),
                        Obstaculo("Meteoro 3", 1, 640, -100, 3, 'versao_final/assets/imgs/meteor3.png', None),
                        Obstaculo("Meteoro 4", 2, 640, -100, 4, 'versao_final/assets/imgs/meteor4.png', None),
                    ],
                    None,
                    None,
                    [
                        Inimigo("Inimigo base", 1, 640, -100, None, 4, 'versao_final/assets/imgs/inimigobase.png', None),
                        Inimigo("Inimigo base", 1, 640, -100, None, 7, 'versao_final/assets/imgs/inimigobase.png', None),
                        Inimigo("Inimigo base", 1, 640, -100, None, 5, 'versao_final/assets/imgs/inimigobase.png', None),
                        Inimigo("Inimigo base", 1, 640, -100, None, 6, 'versao_final/assets/imgs/inimigobase.png', None),
                        Inimigo("Inimigo base", 1, 640, -100, None, 4, 'versao_final/assets/imgs/inimigobase.png', None)
                    ],
                    None,
                    Jogador("Player 1", 3, 640, 600,
                            Arma("Arma base",
                                 Projetil(0, 0, 9, 1, 'versao_final/assets/imgs/shot1_asset.png')
                            ),
                            6, 0, 'versao_final/assets/imgs/jogadorbase.png',
                            ['versao_final/assets/imgs/jogadorbase.png', 'versao_final/assets/imgs/jogadorbase2.png', 'versao_final/assets/imgs/jogadorbase3.png', 'versao_final/assets/imgs/jogadorbase4.png']
                    )
                )
        self.__fases.append(fase1)
        self.__fases[0].iniciar()