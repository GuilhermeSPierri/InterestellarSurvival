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
        self.__inimigos = inimigos
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = jogador

    def iniciar_jogo(self):
        # TAMANHO DA TELA
        x = 1100
        y = 660
         #inicia pygame
        pygame.init()

        #cria a janela do jogo
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('Interstellar Survival')

        #fonte do jogo
        font = pygame.font.SysFont('assets/fonts/PixelGameFont.ttf', 50)

        # Carrega os planos de fundo
        bg1 = pygame.image.load('prototipo/assets/imgs/bg.png').convert_alpha()
        bg2 = pygame.image.load('prototipo/assets/imgs/bg.png').convert_alpha()
        bg1 = pygame.transform.scale(bg1, (x, y))
        bg2 = pygame.transform.scale(bg2, (x, y))

        # Posições iniciais dos planos de fundo
        bg1_y = 0
        bg2_y = -bg1.get_height()

        #inicializa as imagens dos inimigos
        for inimigo in self.__inimigos:
            inimigo.imagem = pygame.image.load(inimigo.imagem).convert_alpha()
            inimigo.imagem = pygame.transform.scale(inimigo.imagem, (70, 70))

        #inicializa as imagens do jogador
        self.__jogador.imagem = pygame.image.load(self.__jogador.imagem).convert_alpha()
        self.__jogador.imagem = pygame.transform.scale(self.__jogador.imagem, (70, 70))
        self.__jogador.imagem = pygame.transform.rotate(self.__jogador.imagem, 90)

        #inicializa a imagem do projétil
        """Para as versões iniciais do jogo, como a de agora, vamos utilizar somente um projétil,
        que ficará escondido atrás da nave do jogador. Sendo assim só é possível atirar novamente
        quando o projétil anterior tiver já saído de tela ou atingido um inimigo"""
        self.__jogador.arma.projetil.imagem = pygame.image.load(self.__jogador.arma.projetil.imagem).convert_alpha()
        self.__jogador.arma.projetil.imagem = pygame.transform.scale(self.__jogador.arma.projetil.imagem, (40, 40))
        self.__jogador.arma.projetil.imagem = pygame.transform.rotate(self.__jogador.arma.projetil.imagem, 90)

        #coloca os inimigos inicialmente em posições aleatórias
        for inimigo in self.__inimigos:
            inimigo.posicao_aleatoria(x, -400)

        #coloca a nave do jogador na posição inicial
        self.__jogador.x = 640
        self.__jogador.y = 600

        #coloca o projétil escondido atrás da nave do jogador
        self.__jogador.arma.projetil.velocidade = 0
        self.__jogador.arma.projetil.x = self.__jogador.x +15
        self.__jogador.arma.projetil.y = self.__jogador.y +5

        #pega o rect da imagem jogador (usado para verificar colisões)
        player_rect = self.__jogador.imagem.get_rect()
        
        #pega o rect da imagem  de todos inimigos
        inimigos_rect = []
        for inimigo in self.__inimigos:
            inimigos_rect.append(inimigo.imagem.get_rect())
        
        #pega o rect do projétil
        projetil_rect = self.__jogador.arma.projetil.imagem.get_rect()

        #variável utilizada para saber se o jogador está atirando
        triggered = False

        #clock do jogo
        clock = pygame.time.Clock()

        #variável que controla o laço do jogo
        rodando = True

        #contador que vai ser utilizado pra saber se o jogo está na primeira execução
        contador = 0

        #laço principal
        while rodando:
            #laço de eventos
            for event in pygame.event.get():
                #sair do jogo
                if event.type == pygame.QUIT:
                    rodando = False

            # Desenha os planos de fundo
            screen.blit(bg1, (0, bg1_y))
            screen.blit(bg2, (0, bg2_y))

            # Move os planos de fundo na velocidade 2
            bg1_y += 2
            bg2_y += 2

            # Verifica se os planos de fundo saíram da tela
            if bg1_y >= y:
                bg1_y = bg2_y - bg2.get_height()

            if bg2_y >= y:
                bg2_y = bg1_y - bg1.get_height()
            
            #teclas pressionadas 
            #caso o jogador não esteja atirando, o projétil se move junto com a nave
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
                #jogador atirou seta triggered em true e a velocidade do projétil
                triggered = True 
                self.__jogador.arma.projetil.velocidade = 8

            #colisoes ou respawn
            if contador != 0: #verifica se não está no primeiro laço

                colisao = Colisao() #variavel que vai ser utilizada pra verificar colisão

                #laço dos inimigos
                for i in range(len(self.__inimigos)):

                    #checa se o inimigo da posição [i] da lista colidiu com o jogador
                    if colisao.check(player_rect, inimigos_rect[i]):
                        self.__jogador.vidas -= 1
                        self.__jogador.pontos -= 1
                        self.__inimigos[i].vidas -= 1
                    
                    #checa se o inimigo da posição [i] da lista foi acertado com o projétil
                    if colisao.check(projetil_rect, inimigos_rect[i]):
                        self.__inimigos[i].vidas -=1 
                        self.__jogador.pontos += 1
                        triggered = False
                        self.__jogador.arma.projetil.respawn(self.__jogador.x, self.__jogador.y)

                    #respawn inimigo morreu
                    if self.__inimigos[i].vidas <= 0:
                        self.__inimigos[i].respawn(x)

                    #respawn inimigo saiu da tela
                    if self.__inimigos[i].y >= y+20:
                        self.__inimigos[i].respawn(x)
                    
                    #posição do rect do inimigo
                    inimigos_rect[i].x = self.__inimigos[i].x
                    inimigos_rect[i].y = self.__inimigos[i].y
                
                    #movimentacao do inimigo, somente para baixo
                    self.__inimigos[i].mover_baixo()

                    #desenha o rect do inimigo [i]
                    pygame.draw.rect(screen, (0, 0, 0), inimigos_rect[i], 4)

                    #cria a imagem do inimigo [i]
                    screen.blit(self.__inimigos[i].imagem, (self.__inimigos[i].x, self.__inimigos[i].y))

            #verifica se as vidas do jogador acabaram
            #caso tenha acabado, encerra o laço principal
            if self.__jogador.vidas <= 0:
                rodando = False

            #respawn projetil quando sai da tela
            if self.__jogador.arma.projetil.y <= 0:
                triggered = False
                self.__jogador.arma.projetil.respawn(self.__jogador.x, self.__jogador.y)

            #posição do rect do jogador
            player_rect.x = self.__jogador.x
            player_rect.y = self.__jogador.y

            #posição do rect do projétil
            projetil_rect.x = self.__jogador.arma.projetil.x
            projetil_rect.y = self.__jogador.arma.projetil.y

            #caso o jogador atire, esse método vai fazer com que o tiro vá para frente
            self.__jogador.arma.atirar()

            #pontuação
            score = font.render(f'Vidas: {self.__jogador.vidas} | Pontos: {self.__jogador.pontos}', True, (255,255,255))
            screen.blit(score, (50, 50))

            #desenha o rect do projetil e jogador
            pygame.draw.rect(screen, (0, 0, 0), player_rect, 4)
            pygame.draw.rect(screen, (0, 0, 0), projetil_rect, 4)

            #criar imagens do projetil e jogador
            screen.blit(self.__jogador.arma.projetil.imagem, (self.__jogador.arma.projetil.x, self.__jogador.arma.projetil.y))
            screen.blit(self.__jogador.imagem, (self.__jogador.x, self.__jogador.y))

            pygame.display.update()
            clock.tick(60)  # Limita o jogo a 60 FPS

            contador += 1 #contador é atualizado de acordo com a execução

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

