import pygame, random
from GameObjectFactory import GameObjectFactory
from Obstaculo import Obstaculo


class ObstaculoFactory(GameObjectFactory):

    def criar_objeto(self, x, y, vida_min, vida_max, velocidade_min, velocidade_max):

        img_inimigos_base = ['versao_final/assets/imgs/meteor.png', 'versao_final/assets/imgs/meteor2.png','versao_final/assets/imgs/meteor3.png', 'versao_final/assets/imgs/meteor4.png']
        img = random.choice(img_inimigos_base)
        
        velocidade = random.randint(velocidade_min, velocidade_max)

        vida = random.randint(vida_min, vida_max)

        obstaculo = Obstaculo("Obstáculo", vida, x, y, velocidade, img, None)

        return obstaculo
