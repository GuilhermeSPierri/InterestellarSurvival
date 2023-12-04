import pygame
from estados.EstadoGenerico import EstadoGenerico
from singleton.Configuracoes import Configuracoes


class EstadoMenu(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo.rect_iniciar.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_jogar)

                elif self.jogo.rect_how_to_play.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_instrucao)

                elif self.jogo.rect_creditos.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_creditos)

                elif self.jogo.rect_ranking.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_ranking)

    def atualizar(self):
        pass

    def desenhar(self):
        config = Configuracoes()

        # Desenha os planos de fundo
        self.jogo.screen.blit(self.jogo.bg3, (0, self.jogo.bg3_y))
        self.jogo.screen.blit(self.jogo.bg4, (0, self.jogo.bg4_y))


        # Desenha o contorno do retângulo
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_iniciar, 2)
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_how_to_play, 2)
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_creditos, 2)
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_ranking, 2)

        # Desenhando o texto na tela
        self.jogo.screen.blit(self.jogo.texto_iniciar, self.jogo.rect_iniciar)
        self.jogo.screen.blit(self.jogo.texto_how_to_play, self.jogo.rect_how_to_play)
        self.jogo.screen.blit(self.jogo.texto_creditos, self.jogo.rect_creditos)
        self.jogo.screen.blit(self.jogo.texto_ranking, self.jogo.rect_ranking)

        if self.jogo.contador_musica == 0:
            pygame.mixer.music.load(config.audio_home)
            pygame.mixer.music.play(-1)
            self.jogo.contador_musica += 1
