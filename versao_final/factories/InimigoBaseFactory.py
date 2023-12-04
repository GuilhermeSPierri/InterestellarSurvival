import random
from logica_de_jogo.personagens.Inimigo import Inimigo
from logica_de_jogo.armas.ArmaInimigo import ArmaInimigo
from singleton.Configuracoes import Configuracoes
from factories.GameObjectFactory import GameObjectFactory


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