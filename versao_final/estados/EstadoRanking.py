import pygame
from estados.EstadoGenerico import EstadoGenerico
from singleton.Configuracoes import Configuracoes


class EstadoRanking(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(self.jogo.estado_menu)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo.rect_voltar.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_menu)

    def atualizar(self):
        pass

    def desenhar(self):
        config = Configuracoes()
        self.font = pygame.font.Font(config.caminho_fonte1, 36)
        titulo_fonte = pygame.font.Font(config.caminho_fonte1, 48)  # Nova fonte para o título

        # Criando o texto do título
        titulo_texto = titulo_fonte.render("Top 5 Melhores Pontuações", True, self.jogo.cor)
        titulo_rect = titulo_texto.get_rect(center=(1100 // 2, 50))

        # Criando o texto que será exibido na tela, divido por linhas
        highscores = config.persistencia.get_leaderboard()
        linhas_leaderboard = [f"{i + 1}º: {score['score']} pontos" for i, score in enumerate(highscores)]

        # Renderizando as linhas de texto
        self.textos = [self.font.render(linha, True, self.jogo.cor) for linha in linhas_leaderboard]

        # Calculando as posições verticais dos textos
        self.rect_textos = [texto.get_rect(center=(1100 // 2, ((660 // 2)-100) + i * 40)) for i, texto in enumerate(self.textos)]
       
        # Desenha os planos de fundo
        self.jogo.screen.blit(self.jogo.bg3, (0, self.jogo.bg3_y))
        self.jogo.screen.blit(self.jogo.bg4, (0, self.jogo.bg4_y))

        # Desenhando o título na tela
        self.jogo.screen.blit(titulo_texto, titulo_rect)

        # Desenhando o botão de voltar
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_voltar, 2)
        self.jogo.screen.blit(self.jogo.texto_voltar, self.jogo.rect_voltar)

        # Desenhando os textos na tela
        for i, texto in enumerate(self.textos):
            self.jogo.screen.blit(texto, self.rect_textos[i])
