from abc import ABC


class EstadoGenerico(ABC):
    def __init__(self, jogo):
        self.jogo = jogo
    def lidar_com_eventos(self, eventos):
        pass

    def atualizar(self):
        pass

    def desenhar(self):
        pass