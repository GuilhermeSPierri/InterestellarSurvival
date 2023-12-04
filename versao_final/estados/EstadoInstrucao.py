import pygame
from estados.EstadoGenerico import EstadoGenerico
from singleton.Configuracoes import Configuracoes


class EstadoInstrucao(EstadoGenerico):
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
        self.font = pygame.font.Font(config.caminho_fonte1, 30)
        # Criando o texto que será exibido na tela, divido por linhas
        linhas = [
            "Seja bem-vindo(a) ao Interstellar Survival! Para continuar se divertindo",
            "irei lhe passar as instruções de como jogar, que são bem simples.",
            "Para mover a sua nave, você deve pressionar as setas do teclado,",
            "enquanto para atirar você deve pressionar espaço. Ao iniciar",
            "o jogo você terá 3 vidas, que podem ser perdidas ao colidir com",
            "naves inimigas e obstáculos. Ao perder todas as vidas, o jogo acaba."
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

        # Desenhando os textos na tela
        for i, texto in enumerate(self.textos):
            self.jogo.screen.blit(texto, self.rect_textos[i])