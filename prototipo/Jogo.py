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
            
            #teclas
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_LEFT] and self.__jogador.x > 1:
                self.__jogador.mover_esquerda()
                if not triggered:
                    self.__jogador.arma.projetil.mover_esquerda(self.__jogador.velocidade)
            if tecla[pygame.K_RIGHT] and self.__jogador.x < (x - 55):
                self.__jogador.mover_direita()
                if not triggered:
                    self.__jogador.arma.projetil.mover_direita(self.__jogador.velocidade)
            if tecla[pygame.K_UP] and self.__jogador.y > 1:
                self.__jogador.mover_cima()
                if not triggered:
                    self.__jogador.arma.projetil.mover_cima(self.__jogador.velocidade)
            if tecla[pygame.K_DOWN] and self.__jogador.y <(y -55):
                self.__jogador.mover_baixo()
                if not triggered:
                    self.__jogador.arma.projetil.mover_baixo(self.__jogador.velocidade)
            if tecla[pygame.K_SPACE]:
                triggered = True
                self.__jogador.arma.projetil.velocidade = 8

            
            #colisoes ou respawn
            if contador != 0:
                colisao = Colisao()

                if colisao.check(player_rect, inimigo_rect):
                    self.__jogador.vidas -= 1
                    self.__jogador.pontos -= 1
                    inimigo.vidas -= 1
                
                if colisao.check(projetil_rect, inimigo_rect):
                    inimigo.vidas -=1 
                    self.__jogador.pontos += 1

            if inimigo.vidas <= 0:
                inimigo.respawn(x)

            if self.__jogador.vidas <= 0:
                rodando = False
            
            #respawn
            if inimigo.y >= y+20:
                inimigo.respawn(x)

            if self.__jogador.arma.projetil.y <= 0:
                triggered = False
                self.__jogador.arma.projetil.respawn(self.__jogador.x, self.__jogador.y)

            #posição rect
            player_rect.x = self.__jogador.x
            player_rect.y = self.__jogador.y

            projetil_rect.x = self.__jogador.arma.projetil.x
            projetil_rect.y = self.__jogador.arma.projetil.y

            inimigo_rect.x = inimigo.x
            inimigo_rect.y = inimigo.y
            
            #movimentacao
            inimigo.mover_baixo()

            self.__jogador.arma.atirar()

            #pontuação
            score = font.render(f'Vidas: {self.__jogador.vidas} | Pontos: {self.__jogador.pontos}', True, (255,255,255))
            screen.blit(score, (50, 50))

            pygame.draw.rect(screen, (0, 0, 0), player_rect, 4)
            pygame.draw.rect(screen, (0, 0, 0), projetil_rect, 4)
            pygame.draw.rect(screen, (0, 0, 0), inimigo_rect, 4)

            #criar imagens
            screen.blit(inimigo.imagem, (inimigo.x, inimigo.y))
            screen.blit(self.__jogador.arma.projetil.imagem, (self.__jogador.arma.projetil.x, self.__jogador.arma.projetil.y))
            screen.blit(self.__jogador.imagem, (self.__jogador.x, self.__jogador.y))

            pygame.display.update()
            clock.tick(60)  # Limita o jogo a 60 FPS

            contador += 1

        pygame.quit()
        

#Getters e setters da classe

    @property
    def projeteis(self):
        return self.__projeteis
    
    @projeteis.setter
    def projeteis(self, projeteis):
        self.__projeteis = projeteis

    @property
    def powerUps(self):
        return self.__powerUps
    
    @powerUps.setter
    def powerUps(self, powerUps):
        self.__powerUps = powerUps

    @property
    def inimigos(self):
        return self.__inimigos
    
    @inimigos.setter
    def inimigos(self, inimigos):
        self.__inimigos = inimigos

    @property
    def tempo_decorrido(self):
        return self.__tempo_decorrido
    
    @tempo_decorrido.setter
    def tempo_decorrido(self, tempo_decorrido):
        self.__tempo_decorrido = tempo_decorrido

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

#Demais métodos
    
    def cadastrar_jogador(self):
        pass
    
    def pausar(self):
        pass

    def derrota(self):
        pass

    def renderizar(self):
        pass

    def atualizar(self):
        pass

    def gerar_power_up(self):
        pass

    def coletar_power_up(self):
        pass

    def incrementar_pontos(self):
        pass

