from Jogo import Jogo
from Obstaculo import Obstaculo
from Powerup import PowerUp
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo


"""j = Jogo(None,
        None,
        [
            Inimigo("Inimigo base", 1, 640, -100, None, 4, 'versao_final/assets/imgs/inimigobase.png', None),
            Inimigo("Inimigo base", 1, 640, -100, None, 7, 'versao_final/assets/imgs/inimigobase.png', None),
            Inimigo("Inimigo base", 1, 640, -100, None, 5, 'versao_final/assets/imgs/inimigobase.png', None),
            Inimigo("Inimigo base", 1, 640, -100, None, 6, 'versao_final/assets/imgs/inimigobase.png', None),
            Inimigo("Inimigo base", 1, 640, -100, None, 4, 'versao_final/assets/imgs/inimigobase.png', None)],
        None,
        Jogador("Player 1", 3, 640, 600,
                Arma("Arma base",
                     Projetil(0, 0, 9, 1, 'versao_final/assets/imgs/shot1_asset.png')),
                6, 0, 'versao_final/assets/imgs/jogadorbase.png',
                ['versao_final/assets/imgs/jogadorbase.png', 'versao_final/assets/imgs/jogadorbase2.png', 'versao_final/assets/imgs/jogadorbase3.png', 'versao_final/assets/imgs/jogadorbase4.png']
        )
    )"""
jogo = Jogo()
        
jogo.iniciar_jogo()
