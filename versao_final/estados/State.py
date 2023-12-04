import pygame
from singleton.Configuracoes import Configuracoes
from estados.EstadoMenu import EstadoMenu
from estados.EstadoJogar import EstadoJogar
from estados.EstadoInstrucao import EstadoInstrucao
from estados.EstadoGameOver import EstadoGameOver
from estados.EstadoCreditos import EstadoCreditos
from estados.EstadoRanking import EstadoRanking


# Classe principal responsável por cada estado
class GerenciadoraDeEstados:
    def __init__(self):

        config = Configuracoes()

        self.screen = pygame.display.set_mode((config.largura_tela, config.altura_tela))
        pygame.display.set_caption(config.titulo)
        self.font = pygame.font.Font(config.caminho_fonte1, 50)  
        self.cor = (255, 255, 255)

        # Carrega os planos de fundo
        self.bg3 = pygame.image.load(config.caminho_background).convert_alpha()
        self.bg4 = pygame.image.load(config.caminho_background).convert_alpha()
        self.bg3 = pygame.transform.scale(self.bg3, (config.largura_tela, config.altura_tela))
        self.bg4 = pygame.transform.scale(self.bg4, (config.altura_tela, config.largura_tela))
        self.som_game_over = pygame.mixer.Sound(config.audio_gameover)
        self.som_shoot_jogador = pygame.mixer.Sound(config.audio_tiro)
        self.contador_musica = 0
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

        #Chamando cada tela, ou seja, cada estado
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

