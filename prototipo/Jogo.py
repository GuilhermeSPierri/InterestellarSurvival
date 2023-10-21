from Obstaculo import Obstaculo
from Powerup import PowerUp
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo
from Colisao import Colisao
import pygame

class Jogo:
    def __init__(self, projeteis, powerUps, inimigos, tempo_decorrido: float, jogador: Jogador):
        self.__projeteis = projeteis
        self.__powerUps = powerUps
        self.__inimigos = [Inimigo("Inimigo base", 1, 640, -100, None, 4, 'prototipo/assets/imgs/inimigobase.png')]
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = Jogador("Player 1", 3, 640, 600, Arma("Arma base", Projetil(0, 0, 9, 1, 'prototipo/assets/imgs/shot1_asset.png')), 6, 0, 'prototipo/assets/imgs/jogadorbase.png')

    """#ARQUIVOS
    BG = 'assets/imgs/bg.png'
    FONTE = 'assets/fonts/PixelGameFont.ttf'
    ALVO ='assets/imgs/target.png'
    MIRA = 'assets/imgs/mouse.png'
    DISPARO = 'assets/audio/disparo.mp3'"""

    def iniciar_jogo(self):
        # TAMANHO DA TELA
        x = 1100
        y = 660

        pygame.init()

        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('Space Shooters')

        font = pygame.font.SysFont('assets/fonts/PixelGameFont.ttf', 50)

        # Carregue os planos de fundo
        bg1 = pygame.image.load('prototipo/assets/imgs/bg.png').convert_alpha()
        bg2 = pygame.image.load('prototipo/assets/imgs/bg.png').convert_alpha()
        bg1 = pygame.transform.scale(bg1, (x, y))
        bg2 = pygame.transform.scale(bg2, (x, y))

        # Posições iniciais dos planos de fundo
        bg1_y = 0
        bg2_y = -bg1.get_height()

        inimigo = self.__inimigos[0]

        inimigo.imagem = pygame.image.load(inimigo.imagem).convert_alpha()
        inimigo.imagem = pygame.transform.scale(inimigo.imagem, (70, 70))

        self.__jogador.imagem = pygame.image.load(self.__jogador.imagem).convert_alpha()
        self.__jogador.imagem = pygame.transform.scale(self.__jogador.imagem, (70, 70))
        self.__jogador.imagem = pygame.transform.rotate(self.__jogador.imagem, 90)

        self.__jogador.arma.projetil.imagem = pygame.image.load(self.__jogador.arma.projetil.imagem).convert_alpha()
        self.__jogador.arma.projetil.imagem = pygame.transform.scale(self.__jogador.arma.projetil.imagem, (40, 40))
        self.__jogador.arma.projetil.imagem = pygame.transform.rotate(self.__jogador.arma.projetil.imagem, 90)

        inimigo.x = 640
        inimigo.y = -100

        self.__jogador.x = 640
        self.__jogador.y = 600

        self.__jogador.arma.projetil.velocidade = 0
        self.__jogador.arma.projetil.x = self.__jogador.x +15 #ver
        self.__jogador.arma.projetil.y = self.__jogador.y +5

        player_rect = self.__jogador.imagem.get_rect()
        inimigo_rect = inimigo.imagem.get_rect()
        projetil_rect = self.__jogador.arma.projetil.imagem.get_rect()


        triggered = False

        clock = pygame.time.Clock()

        rodando = True

        contador = 0

        while rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

            # Desenhe os planos de fundo
            screen.blit(bg1, (0, bg1_y))
            screen.blit(bg2, (0, bg2_y))

            # Move os planos de fundo
            bg1_y += 2
            bg2_y += 2

            # Verifique se os planos de fundo saíram da tela
            if bg1_y >= y:
                bg1_y = bg2_y - bg2.get_height()

            if bg2_y >= y:
                bg2_y = bg1_y - bg1.get_height()

