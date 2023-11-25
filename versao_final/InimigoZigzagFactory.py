import pygame, random
from GameObjectFactory import GameObjectFactory
from Inimigo import Inimigo
from ArmaInimigo import ArmaInimigo
from ProjetilInimigo import ProjetilInimigo
from InimigoZigzag import InimigoZigzag



class InimigoZigzagFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):

        img_inimigos_base = ['versao_final/assets/imgs/fighter.png']
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)

        if velocidade > 7:
            vel_projetil = velocidade+2
        else:
            vel_projetil = 9
        
        vida = random.randint(vida_min, vida_max)

        inimigo = InimigoZigzag("Inimigo base", vida, x, y, 
                                ArmaInimigo("Arma base",
                                                ProjetilInimigo(0, 0, vel_projetil, 1, []), 0
                                ), velocidade, img, None)
        return inimigo
