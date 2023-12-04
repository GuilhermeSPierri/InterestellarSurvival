from logica_de_jogo.obstaculos.Obstaculo import Obstaculo
import math


class ObstaculoPerseguidor(Obstaculo):
    def __init__(self, nome: str, vidas: int, x: int, y: int, velocidade: int, image:str):
        super().__init__(nome, vidas, x, y, velocidade, image)

    def mover(self, jogador_x, jogador_y):
        direcao_x = jogador_x - self.x
        direcao_y = jogador_y - self.y

        # Normaliza a direção para garantir que o inimigo se mova com a mesma velocidade em todas as direções
        comprimento = math.sqrt(direcao_x**2 + direcao_y**2)
        if comprimento != 0:
            direcao_x /= comprimento
            direcao_y /= comprimento

        # Atualiza a posição do inimigo com base na direção normalizada e na velocidade
        self.x += direcao_x * self.velocidade
        self.y += direcao_y * self.velocidade

