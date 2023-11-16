from Obstaculo import Obstaculo
from Powerup import PowerUp
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo
from Colisao import Colisao
import pygame


class Fase:
    def __init__(self, obstaculos,  projeteis, powerUps, inimigos, tempo_decorrido: float, jogador: Jogador):
        self.__obstaculos = obstaculos
        self.__projeteis = projeteis
        self.__powerUps = powerUps
        self.__inimigos = inimigos
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = jogador

    def iniciar(self):
        # TAMANHO DA TELA
        x = 1100
        y = 660
         #inicia pygame
        pygame.init()

        #cria a janela do jogo
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('Interstellar Survival')

        #clock do jogo
        clock = pygame.time.Clock()

        #fonte do jogo
        font = pygame.font.SysFont('versao_final/assets/fonts/PixelGameFont.ttf', 50)

        # Carrega os planos de fundo
        bg1 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        bg2 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        bg1 = pygame.transform.scale(bg1, (x, y))
        bg2 = pygame.transform.scale(bg2, (x, y))

        # Posições iniciais dos planos de fundo
        bg1_y = 0
        bg2_y = -bg1.get_height()

        #carrega e deixa as imagens dos inimigos numa determinada escala
        for inimigo in self.__inimigos:
            inimigo.image = pygame.image.load(inimigo.image).convert_alpha()
            inimigo.image = pygame.transform.scale(inimigo.image, (70, 70))
        
        #carrega e deixa as imagens dos obstaculos numa determinada escala
        for obstaculo in self.__obstaculos:
            obstaculo.image = pygame.image.load(obstaculo.image).convert_alpha()
            obstaculo.image = pygame.transform.scale(obstaculo.image, (70, 70))

        #carrega e deixa as imagens do jogador e rotaciona numa determinada escala
        self.__jogador.image = pygame.image.load(self.__jogador.image).convert_alpha()
        self.__jogador.image = pygame.transform.scale(self.__jogador.image, (80, 40))
        self.__jogador.image = pygame.transform.rotate(self.__jogador.image, 90)

        #deixa as imagens do jogador e rotaciona numa determinada escala
        """Para as versões iniciais do jogo, como a de agora, vamos utilizar somente um projétil,
        que ficará escondido atrás da nave do jogador. Sendo assim só é possível atirar novamente
        quando o projétil anterior tiver já saído de tela ou atingido um inimigo"""
        """self.__jogador.arma.projetil.image = pygame.image.load(self.__jogador.arma.projetil.image).convert_alpha()
        self.__jogador.arma.projetil.image = pygame.transform.scale(self.__jogador.arma.projetil.image, (40, 40))
        self.__jogador.arma.projetil.image = pygame.transform.rotate(self.__jogador.arma.projetil.image, 90)"""


        #coloca os inimigos inicialmente em posições aleatórias
        for inimigo in self.__inimigos:
            inimigo.posicao_aleatoria(x, -1000)
        
        #coloca os obstáculos inicialmente em posições aleatórias
        for obstaculo in self.__obstaculos:
            obstaculo.posicao_aleatoria(x, -1000)

        #coloca a nave do jogador na posição inicial
        self.__jogador.x = 640
        self.__jogador.y = 600

        #coloca o projétil escondido atrás da nave do jogador
        #self.__jogador.arma.projetil.velocidade = 0
        horizontal, vertical = self.__jogador.image.get_size()
        """print(horizontal, vertical)
        self.__jogador.arma.projetil.x = self.__jogador.x + round(vertical/12) -4
        self.__jogador.arma.projetil.y = self.__jogador.y + round(horizontal/4)"""

        #pega o rect da image jogador (usado para verificar colisões)
        self.__jogador.rect = self.__jogador.image.get_rect()
        
        #pega o rect da image  de todos inimigos
        for inimigo in self.__inimigos:
            inimigo.rect = inimigo.image.get_rect()
        
        #pega o rect da image  de todos obstaculos
        for obstaculo in self.__obstaculos:
            obstaculo.rect = obstaculo.image.get_rect()
        
        #pega o rect do projétil
        #self.__jogador.arma.projetil.rect = self.__jogador.arma.projetil.image.get_rect()

        #variável utilizada para saber se o jogador está atirando
        #triggered = False

        #variável que controla o laço do jogo
        rodando = True

        #contador que vai ser utilizado pra saber se o jogo está na primeira execução
        contador = 0

        #adiciona jogador aos sprites
        player_group = pygame.sprite.Group()
        player_group.add(self.__jogador)

        #adiciona projetil aos sprites
        projetil_group = pygame.sprite.Group()

        contPrite = 0

        tempo_ultimo_tiro = pygame.time.get_ticks()
        delay_entre_tiros = 500  # Defina o atraso desejado em milissegundos (por exemplo, 500 ms).

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
                """if not triggered:
                    self.__jogador.arma.projetil.mover_esquerda(self.__jogador.velocidade)"""
            if tecla[pygame.K_RIGHT] and self.__jogador.x < (x - 55):
                self.__jogador.mover_direita()
                """if not triggered:
                    self.__jogador.arma.projetil.mover_direita(self.__jogador.velocidade)"""
            if tecla[pygame.K_UP] and self.__jogador.y > 1:
                self.__jogador.mover_cima()
                """if not triggered:
                    self.__jogador.arma.projetil.mover_cima(self.__jogador.velocidade)"""
            if tecla[pygame.K_DOWN] and self.__jogador.y <(y -55):
                self.__jogador.mover_baixo()
                """if not triggered:
                    self.__jogador.arma.projetil.mover_baixo(self.__jogador.velocidade)"""
            tempo_atual = pygame.time.get_ticks()
            if tecla[pygame.K_SPACE] and (tempo_atual - tempo_ultimo_tiro) > delay_entre_tiros:
                projetil_group.add(self.__jogador.arma.atirar(self.__jogador.x + round(horizontal/2), self.__jogador.y ,5, 1, 'versao_final/assets/imgs/shot1_asset.png', []))
                tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro
                #jogador atirou seta triggered em true e a velocidade do projétil
                #triggered = True 
                #self.__jogador.arma.projetil.velocidade = 8

            #colisoes ou respawn
            if contador != 0: #verifica se não está no primeiro laço

                colisao = Colisao() #variavel que vai ser utilizada pra verificar colisão

                #laço dos inimigos
                for i in range(len(self.__inimigos)):

                    #checa se o inimigo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__inimigos[i].rect):
                        self.__jogador.vidas -= 1
                        self.__jogador.diminuir_pontos(1)
                        self.__inimigos[i].vidas -= 1
                    
                    #checa se o inimigo da posição [i] da lista foi acertado com o projétil
                    """if colisao.check(projetil_group, self.__inimigos[i].rect):
                        self.__inimigos[i].vidas -=1 
                        self.__jogador.pontos += 1
                        triggered = False"""
                    # Verifica colisões do projétil com inimigos
                    for projetil in projetil_group:
                        #for inimigo in self.__inimigos:
                        if colisao.check(self.__inimigos[i].rect, projetil.rect):
                            self.__inimigos[i].vidas -= 1
                            projetil.kill()  # Remove o projétil após acertar um inimigo
                        

                    #respawn inimigo morreu
                    if self.__inimigos[i].vidas <= 0:
                        self.__inimigos[i].respawn(x)
                        self.__jogador.pontos += 1

                    #respawn inimigo saiu da tela
                    if self.__inimigos[i].y >= y+20:
                        self.__inimigos[i].respawn(x)
                    
                    #posição do rect do inimigo
                    self.__inimigos[i].rect.x = self.__inimigos[i].x
                    self.__inimigos[i].rect.y = self.__inimigos[i].y
                
                    #movimentacao do inimigo, somente para baixo
                    self.__inimigos[i].mover_baixo()

                    #desenha o rect do inimigo [i]
                    pygame.draw.rect(screen, (0, 0, 0), self.__inimigos[i].rect, 4)

                    #cria a image do inimigo [i]
                    screen.blit(self.__inimigos[i].image, (self.__inimigos[i].x, self.__inimigos[i].y))
            
                #laço dos obstaculos
                for i in range(len(self.__obstaculos)):

                    #checa se o obstaculo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__obstaculos[i].rect):
                        self.__jogador.vidas = 0
                        self.__jogador.diminuir_pontos(1)
                        #self.__obstaculos[i].vidas -= 1
                    
                    #checa se o obstaculo da posição [i] da lista foi acertado com o projétil
                    """if colisao.check(self.__jogador.arma.projetil.rect, self.__obstaculos[i].rect):
                        #self.__obstaculos[i].vidas -=1 
                        #self.__jogador.pontos += 1
                        triggered = False
                        self.__jogador.arma.projetil.respawn(self.__jogador.x, (round(vertical/12) -4), self.__jogador.y, round(horizontal/4))"""
                    for projetil in projetil_group:
                        #for inimigo in self.__inimigos:
                        if colisao.check(self.__obstaculos[i].rect, projetil.rect):
                            self.__obstaculos[i].vidas -= 1
                            projetil.kill()  # Remove o projétil após acertar um inimigo

                    #respawn obstaculo destruido
                    if self.__obstaculos[i].vidas <= 0:
                        self.__obstaculos[i].respawn(x, -1000)
                        self.__jogador.pontos += 1

                    #respawn obstaculo saiu da tela
                    if self.__obstaculos[i].y >= y+20:
                        self.__obstaculos[i].respawn(x, -1000)
                    
                    #posição do rect do obstaculo
                    self.__obstaculos[i].rect.x = self.__obstaculos[i].x
                    self.__obstaculos[i].rect.y = self.__obstaculos[i].y
                
                    #movimentacao do obstaculo, somente para baixo
                    self.__obstaculos[i].mover_baixo()

                    #desenha o rect do obstaculo [i]
                    pygame.draw.rect(screen, (0, 0, 0), self.__obstaculos[i].rect, 4)

                    #cria a image do obstaculo [i]
                    screen.blit(self.__obstaculos[i].image, (self.__obstaculos[i].x, self.__obstaculos[i].y))

            #verifica se as vidas do jogador acabaram
            #caso tenha acabado, encerra o laço principal
            if self.__jogador.vidas <= 0:
                rodando = False

            #respawn projetil quando sai da tela
            """if self.__jogador.arma.projetil.y <= 0:
                triggered = False
                self.__jogador.arma.projetil.respawn(self.__jogador.x, (round(vertical/12) -4), self.__jogador.y, round(horizontal/4))"""

            #posição do rect do jogador
            self.__jogador.rect.x = self.__jogador.x
            self.__jogador.rect.y = self.__jogador.y

            """#posição do rect do projétil
            self.__jogador.arma.projetil.rect.x = self.__jogador.arma.projetil.x
            self.__jogador.arma.projetil.rect.y = self.__jogador.arma.projetil.y"""

            #caso o jogador atire, esse método vai fazer com que o tiro vá para frente
            #self.__jogador.arma.atirar()

            #sprite basico
            if contPrite >= len(self.__jogador.sprites):
                contPrite = 0
            else:
                contPrite += 1
            
            self.__jogador.image = pygame.image.load(self.__jogador.sprites[contPrite-1]).convert_alpha()
            self.__jogador.image = pygame.transform.scale(self.__jogador.image, (80, 40))
            self.__jogador.image = pygame.transform.rotate(self.__jogador.image, 90)

            #pontuação
            score = font.render(f'Vidas: {self.__jogador.vidas} | Pontos: {self.__jogador.pontos}', True, (255,255,255))
            screen.blit(score, (50, 50))

            #desenha o rect do projetil e jogador
            #pygame.draw.rect(screen, (0, 0, 0), self.__jogador.rect, 4)
            #pygame.draw.rect(screen, (0, 0, 0), self.__jogador.arma.projetil.rect, 4)
            projetil_group.draw(screen)
            player_group.draw(screen)
            projetil_group.update()

            #criar imagens do projetil e jogador
            #screen.blit(self.__jogador.arma.projetil.image, (self.__jogador.arma.projetil.x, self.__jogador.arma.projetil.y))
            screen.blit(self.__jogador.image, (self.__jogador.x, self.__jogador.y))

            pygame.display.update()
            pygame.display.flip()
            clock.tick(80)  # Limita o jogo a 60 FPS

            contador += 1 #contador é atualizado de acordo com a execução

        pygame.quit()

#Getters e setters da classe

    @property
    def obstaculos(self):
        return self.__obstaculos
    
    @obstaculos.setter
    def obstaculos(self, obstaculos):
        self.__obstaculos = obstaculos
    
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

