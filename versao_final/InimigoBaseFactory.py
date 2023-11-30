import pygame, random
from GameObjectFactory import GameObjectFactory
from Inimigo import Inimigo
from ArmaInimigo import ArmaInimigo
from ProjetilInimigo import ProjetilInimigo
from Configuracoes import Configuracoes


class InimigoBaseFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):
        config = Configuracoes()

        img_inimigos_base = config.inimigo_base
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)
        
        vida = random.randint(vida_min, vida_max)

        inimigo = Inimigo("Inimigo base", vida, x, y, 
                                ArmaInimigo("Arma base", 0
                                ), velocidade, img)
        return inimigo