import pygame
import sys
from Jogo import Jogo
from Fase import Fase

# Definindo os estados
class Estado:
    def __init__(self, jogo):
        self.jogo = jogo

    def lidar_com_eventos(self, eventos):
        pass

    def atualizar(self):
        pass

    def desenhar(self):
        pass

# Implementando um estado para a tela de menu
class EstadoMenu(Estado):
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

# Implementando um estado para a tela de jogo (apenas um exemplo)
class EstadoJogar(Estado):
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



# Implementando um estado para a tela de jogo (apenas um exemplo)
class EstadoInstrucao(Estado):
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
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 32)
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

class EstadoCreditos(Estado):
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
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 36)
        
        # Criando o texto que será exibido na tela, divido por linhas
        linhas = [
            "Este jogo foi desenvolvido pelos estudantes",
            "Cid Fernando Sette de Borba, Guilherme da Silva",
            "Pierri e Henrique Mateus Teodoro, na disciplina",
            "Programação Orientada a Objetos II, do curso de",
            "Ciências da Computação na Universidade Federal de",
            "Santa Catarina, semestre 2023.2.",
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

class EstadoRanking(Estado):
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
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 36)
        # Criando o texto que será exibido na tela, divido por linhas
        
        linhas = [
            "1 - Cid: 1000 pontos",
            "2 - Guilherme: 723 pontos",
            "3 - Henrique: 425 pontos",
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

class EstadoGameOver(Estado):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(self.jogo.estado_menu)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo.rect_voltar.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_menu)

                elif self.jogo.rect_tentar_novamente.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_jogar)

    def atualizar(self):
        pass

    def desenhar(self):
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 36)
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


# Implementando uma classe principal que gerencia os estados
class GerenciadoraDeEstados:
    def __init__(self):
        self.screen = pygame.display.set_mode((1100, 660))
        pygame.display.set_caption("Interstellar Survival")
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 50)  
        self.cor = (255, 255, 255)

        # Carrega os planos de fundo
        self.bg3 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        self.bg4 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        self.bg3 = pygame.transform.scale(self.bg3, (1100, 660))
        self.bg4 = pygame.transform.scale(self.bg4, (1100, 660))

        # Posições iniciais dos planos de fundo
        self.bg3_y = 0
        self.bg4_y = -self.bg3.get_height()

        # Criando um texto para exibir na tela
        self.texto_iniciar = self.font.render("Jogar", True, self.cor)
        self.texto_how_to_play = self.font.render("Como jogar?", True, self.cor)
        self.texto_creditos = self.font.render("Creditos", True, self.cor)
        self.texto_ranking = self.font.render("Ranking", True, self.cor)
        self.texto_voltar = self.font.render("Voltar", True, self.cor)
        self.texto_tentar_novamente = self.font.render("Tentar novamente", True, self.cor)

        # Obtém o retângulo do texto e centraliza-o na tela
        self.rect_iniciar = self.texto_iniciar.get_rect(center=((1100 // 2), (660 // 2)-100))
        self.rect_how_to_play = self.texto_how_to_play.get_rect(center=((1100 // 2), (660 // 2)))
        self.rect_creditos = self.texto_creditos.get_rect(center=((1100 // 2), (660 // 2)+100))
        self.rect_ranking = self.texto_ranking.get_rect(center=((1100 // 2), (660 // 2)+200))
        self.rect_voltar = self.texto_voltar.get_rect(center=((1100 // 2), (660 // 2)+250))
        self.rect_tentar_novamente = self.texto_tentar_novamente.get_rect(center=((1100 // 2), (660 // 2)))

        self.estado_menu = EstadoMenu(self)
        self.estado_jogar = EstadoJogar(self)
        self.estado_instrucao = EstadoInstrucao(self)
        self.estado_creditos = EstadoCreditos(self)
        self.estado_ranking = EstadoRanking(self)
        self.estado_game_over = EstadoGameOver(self)

        self.estado_atual = self.estado_menu


    def mudar_estado(self, novo_estado):
        self.estado_atual = novo_estado

    def executar(self):
        clock = pygame.time.Clock()
        rodando = True

        while rodando:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    rodando = False

            self.estado_atual.lidar_com_eventos(eventos)
            self.estado_atual.desenhar()

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    jogo = GerenciadoraDeEstados()
    jogo.executar()
    pygame.quit()
    sys.exit()
