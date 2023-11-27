import pygame, random
from GameObjectFactory import GameObjectFactory
from Obstaculo import Obstaculo
from Configuracoes import Configuracoes


class ObstaculoFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):
        config = Configuracoes()
        
        img_inimigos_base = config.obstaculo_base
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)

        vida = random.randint(vida_min, vida_max)

        obstaculo = Obstaculo("Obstáculo", vida, x, y, velocidade, img, None)

        return obstaculo
