import pygame, random
from GameObjectFactory import GameObjectFactory
from Inimigo import Inimigo
from ArmaInimigo import ArmaInimigo
from ProjetilInimigo import ProjetilInimigo



class InimigoBaseFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vidas, velocidade_min, velocidade_max):

        img_inimigos_base = ['versao_final/assets/imgs/inimigobase.png', 'versao_final/assets/imgs/inimigobase2.png','versao_final/assets/imgs/inimigobase3.png', 'versao_final/assets/imgs/inimigobase4.png', 'versao_final/assets/imgs/inimigobaseazul.png', 'versao_final/assets/imgs/inimigobaseverde.png']
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)

        if velocidade > 7:
            vel_projetil = velocidade+2
        else:
            vel_projetil = 9

        inimigo = Inimigo("Inimigo base", vidas, x, y, 
                                ArmaInimigo("Arma base",
                                                ProjetilInimigo(0, 0, vel_projetil, 1, 'versao_final/assets/imgs/shot1_asset.png', [])
                                ), velocidade, img, None)
        return inimigo