import pygame, random
from GameObjectFactory import GameObjectFactory
from ArmaInimigo import ArmaInimigo
from ProjetilInimigo import ProjetilInimigo
from InimigoZigzag import InimigoZigzag
from Configuracoes import Configuracoes


class InimigoZigzagFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):
        config = Configuracoes()

        img_inimigos_base = config.inimigo_zigzag
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)
        
        vida = random.randint(vida_min, vida_max)

        inimigo = InimigoZigzag("Inimigo base", vida, x, y, 
                                ArmaInimigo("Arma base", 0
                                ), velocidade, img)
        return inimigo
