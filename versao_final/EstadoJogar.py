import pygame
from EstadoGenerico import EstadoGenerico
from Jogo import Jogo

class EstadoJogar(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(self.jogo.estado_menu)

        
    def atualizar(self):
        pass

    def desenhar(self):
        p = Jogo()
        p.iniciar_jogo()
        self.jogo.mudar_estado(self.jogo.estado_game_over)