from Jogo import Jogo
from Obstaculo import Obstaculo
from Powerup import PowerUp
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo


j = Jogo(None,
        None,
        [
            Inimigo("Inimigo base", 1, 640, -100, None, 4, 'prototipo/assets/imgs/inimigobase.png'),
            Inimigo("Inimigo base", 1, 640, -100, None, 7, 'prototipo/assets/imgs/inimigobase.png'),
            Inimigo("Inimigo base", 1, 640, -100, None, 5, 'prototipo/assets/imgs/inimigobase.png'),
            Inimigo("Inimigo base", 1, 640, -100, None, 6, 'prototipo/assets/imgs/inimigobase.png'),
            Inimigo("Inimigo base", 1, 640, -100, None, 4, 'prototipo/assets/imgs/inimigobase.png')],
        None,
        Jogador("Player 1", 3, 640, 600,
                Arma("Arma base",
                     Projetil(0, 0, 9, 1, 'prototipo/assets/imgs/shot1_asset.png')), 6, 0, 'prototipo/assets/imgs/jogadorbase.png'
        )
    )

        
j.iniciar_jogo()
