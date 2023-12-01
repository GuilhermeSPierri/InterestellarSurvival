import pygame, random
from GameObjectFactory import GameObjectFactory
from ObstaculoPerseguidor import ObstaculoPerseguidor
from Configuracoes import Configuracoes


class ObstaculoPerseguidorFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):
        config = Configuracoes()
        
        img_inimigos_base = config.obstaculo_perseguidor
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)

        vida = random.randint(vida_min, vida_max)

        obstaculo = ObstaculoPerseguidor("Obstáculo perseguidor", vida, x, y, velocidade, img)

        return obstaculo
