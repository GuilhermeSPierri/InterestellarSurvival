from logica_de_jogo.personagens.Inimigo import Inimigo
from logica_de_jogo.armas.Arma import Arma
import random


class InimigoZigzag(Inimigo):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, image:str):
        super().__init__(nome, vidas, x, y, arma, velocidade, image)
        self.__direcao_x = 1

    def mover(self):
        self.y += self.velocidade

        # Alteração na direção gradual do movimento
        chance_mudanca_direcao = random.randint(0, 1000)
        if chance_mudanca_direcao < 5:  # Ajusta o valor para mudar a frequência da mudança
            self.__direcao_x *= -1  # Inverte a direção

        self.x += self.velocidade * self.__direcao_x  # Multiplica pela direção

        # Limita a posição do inimigo dentro dos limites da tela
        if self.x <= 0:
            self.x = 0
            self.__direcao_x *= -1  # Inverte a direção ao atingir o limite esquerdo
        elif self.x >= 1000:
            self.x = 1000
            self.__direcao_x *= -1  # Inverte a direção ao atingir o limite direito
