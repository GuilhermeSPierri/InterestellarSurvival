import pygame
import sys
from estados.EstadoGenerico import EstadoGenerico
from singleton.Configuracoes import Configuracoes


class EstadoGameOver(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(self.jogo.estado_menu)
            
            elif evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo.rect_voltar.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_menu)

                elif self.jogo.rect_tentar_novamente.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_jogar)

    def atualizar(self):
        pass

    def desenhar(self):

        config = Configuracoes()
        self.font = pygame.font.Font(config.caminho_fonte1, 36)
        # Criando o texto que será exibido na tela, divido por linhas
        
        linhas = [
            "GAME OVER",
        ]

        # Renderizando as linhas de texto
        self.textos = [self.font.render(linha, True, self.jogo.cor) for linha in linhas]

        # Calculando as posições verticais dos textos
        self.rect_textos = [texto.get_rect(center=(1100 // 2, ((660 // 2)-100) + i * 40)) for i, texto in enumerate(self.textos)]
       
        # Desenha os planos de fundo
        self.jogo.screen.blit(self.jogo.bg3, (0, self.jogo.bg3_y))
        self.jogo.screen.blit(self.jogo.bg4, (0, self.jogo.bg4_y))

        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_voltar, 2)
        self.jogo.screen.blit(self.jogo.texto_voltar, self.jogo.rect_voltar)
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_tentar_novamente, 2)
        self.jogo.screen.blit(self.jogo.texto_tentar_novamente, self.jogo.rect_tentar_novamente)
        
        # Desenhando os textos na tela
        for i, texto in enumerate(self.textos):
            self.jogo.screen.blit(texto, self.rect_textos[i])