from logica_de_jogo.armas.Arma import Arma
from logica_de_jogo.personagens.Jogador import Jogador
from logica_de_jogo.outros_elementos.Colisao import Colisao
from logica_de_jogo.outros_elementos.Explosao import Explosao
from logica_de_jogo.powerups.PowerupVida import PowerupVida
from logica_de_jogo.powerups.PowerupArmaTripla import PowerupArmaTripla
from logica_de_jogo.powerups.PowerupMaisDano import PowerupMaisDano
from logica_de_jogo.outros_elementos.Dificuldade import Dificuldade
from singleton.Configuracoes import Configuracoes
import pygame, random


class Fase:
    def __init__(self, tempo_decorrido: float):
        self.__obstaculos = []
        self.__powerUps = []
        self.__inimigos = []
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = None
        self.__dificuldade = Dificuldade()
        self.__config = Configuracoes()


    def iniciar(self):
        # TAMANHO DA TELA
        x = self.__config.largura_tela
        y = self.__config.altura_tela

        FPS = self.__config.FPS

         #inicia pygame
        pygame.init()

        self.__jogador = Jogador("Player 1", 3, round(self.__config.largura_tela/2), self.__config.altura_tela-30,
                            Arma("Arma base", 300
                            ),
                            6, 0, self.__config.caminho_imagem_jogador,
                            self.__config.sprites_jogador
                    )
        
        self.__jogador.x = round(self.__config.largura_tela/2)
        self.__jogador.y = self.__config.altura_tela-100

        #cria a janela do jogo
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption(self.__config.titulo)

        #clock do jogo
        clock = pygame.time.Clock()

        #fonte do jogo
        font = pygame.font.Font(self.__config.caminho_fonte1, 30)

        # Carrega os planos de fundo
        bg1 = pygame.image.load(self.__config.caminho_background).convert_alpha()
        bg2 = pygame.image.load(self.__config.caminho_background).convert_alpha()
        bg1 = pygame.transform.scale(bg1, (x, y))
        bg2 = pygame.transform.scale(bg2, (x, y))

        # Posições iniciais dos planos de fundo
        bg1_y = 0
        bg2_y = -bg1.get_height()
        
        #carrega as imagens da vida
        coracao_cheio = pygame.image.load(self.__config.caminho_imagem_coracao_cheio).convert_alpha()
        coracao_cheio = pygame.transform.scale(coracao_cheio, (60, 60))

        #carrega a imagem do placar
        barra_score = pygame.image.load(self.__config.caminho_imagem_barra_score).convert_alpha()
        barra_score = pygame.transform.scale(barra_score, (150, 50))

        horizontal, vertical = self.__jogador.image.get_size()

        #variável que controla o laço do jogo
        rodando = True

        #contador que vai ser utilizado pra saber se o jogo está na primeira execução
        contador = 0

        #adiciona jogador aos sprites
        player_group = pygame.sprite.Group()
        player_group.add(self.__jogador)

        #adiciona inimigos aos sprites
        inimigos_group = pygame.sprite.Group()
        inimigos_group.add(self.__inimigos)

        #adiciona obstaculos aos sprites
        obstaculos_group = pygame.sprite.Group()
        obstaculos_group.add(self.__obstaculos)

        #sprites de explosão
        explosion_group = pygame.sprite.Group()

        #grupo de power ups
        powerups = pygame.sprite.Group()

        tempo_inicio_execucao = pygame.time.get_ticks()

        self.__tempo_decorrido = 0

        tempo_ultimo_tiro = self.__tempo_decorrido

        #laço principal
        while rodando:

            self.__tempo_decorrido = pygame.time.get_ticks() - tempo_inicio_execucao

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
            
            self.__dificuldade.controle_dificuldade(x, -1000, self.__tempo_decorrido, self.__obstaculos, self.__inimigos)
            
            #teclas pressionadas 
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_LEFT] and self.__jogador.x > 1:
                self.__jogador.mover_esquerda()
            if tecla[pygame.K_RIGHT] and self.__jogador.x < (x - 55):
                self.__jogador.mover_direita()
            if tecla[pygame.K_UP] and self.__jogador.y > 1:
                self.__jogador.mover_cima()
            if tecla[pygame.K_DOWN] and self.__jogador.y <(y -55):
                self.__jogador.mover_baixo()
            tempo_atual = self.__tempo_decorrido
            if tecla[pygame.K_SPACE] and (tempo_atual - tempo_ultimo_tiro) > self.__jogador.arma.cadencia:
                tiros = self.__jogador.arma.atirar(self.__jogador.x + round(horizontal/2), self.__jogador.y)
                for tiro in tiros:
                    self.__jogador.arma.disparos.add(tiro)
                tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro

            #colisoes ou respawn
            if contador != 0: #verifica se não está no primeiro laço

                colisao = Colisao() #variavel que vai ser utilizada pra verificar colisão

                #laço dos inimigos
                for i in range(len(self.__inimigos)):
                    if random.randrange(0, 100) == 1 and self.__inimigos[i].y>0:
                        self.__inimigos[i].arma.disparos.add(self.__inimigos[i].arma.atirar(self.__inimigos[i].x + (self.__inimigos[i].image.get_width())/2, self.__inimigos[i].y  + (self.__inimigos[i].image.get_height()),7, 1))
                    self.__inimigos[i].arma.disparos.draw(screen)
                    self.__inimigos[i].arma.disparos.update(y)

                    #checa se o inimigo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__inimigos[i].rect):
                        self.__jogador.vidas -= 1
                        self.__inimigos[i].vidas = 0
                    
                    # remove o projetil que o inimigo lançou quando acerta o jogador
                    for projetil in self.__inimigos[i].arma.disparos:
                        if colisao.check(self.jogador.rect, projetil.rect):
                            self.__jogador.vidas -= 1
                            projetil.kill() 
                    
                    # remove o projetil que o inimigo lançou quando sai da tela
                    for projetil in self.__inimigos[i].arma.disparos:
                        if projetil.rect.y > y:
                            projetil.kill() 

                    # Verifica colisões do projétil com inimigos
                    for projetil in self.__jogador.arma.disparos:
                        if colisao.check(self.__inimigos[i].rect, projetil.rect):
                            self.__inimigos[i].vidas -= projetil.dano
                            projetil.kill()  # Remove o projétil após acertar um inimigo

                    #respawn inimigo morreu
                    if self.__inimigos[i].vidas <= 0:
                        explosion = Explosao(self.__inimigos[i].x + (self.__inimigos[i].image.get_width())/2, self.__inimigos[i].y  + (self.__inimigos[i].image.get_height())/2, self.__config.caminho_imagem_explosao1)
                        explosion_group.add(explosion)

                        self.gerar_power_up(self.__inimigos[i], powerups)
                        
                        self.__inimigos[i].respawn(x, -1000)
                        self.__jogador.pontos += 1

                    #respawn inimigo saiu da tela
                    if self.__inimigos[i].y >= y+20:
                        self.__inimigos[i].respawn(x, -1000)
                    
                    #posição do rect do inimigo
                    self.__inimigos[i].rect.x = self.__inimigos[i].x
                    self.__inimigos[i].rect.y = self.__inimigos[i].y
                
                    #movimentacao do inimigo
                    self.__inimigos[i].mover()

                    #cria a image do inimigo [i]
                    screen.blit(self.__inimigos[i].image, (self.__inimigos[i].x, self.__inimigos[i].y))
                
                #laço dos obstaculos
                for i in range(len(self.__obstaculos)):

                    #checa se o obstaculo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__obstaculos[i].rect):
                        self.__jogador.vidas -= 1
                        self.__obstaculos[i].vidas = 0
                    
                    #checa se o obstaculo da posição [i] da lista foi acertado com o projétil
                    for projetil in self.__jogador.arma.disparos:
                        if colisao.check(self.__obstaculos[i].rect, projetil.rect):
                            self.__obstaculos[i].vidas -= projetil.dano
                            projetil.kill()  # Remove o projétil após acertar um inimigo

                    #respawn obstaculo destruido
                    if self.__obstaculos[i].vidas <= 0:
                        explosion = Explosao(self.__obstaculos[i].x + (self.__obstaculos[i].image.get_width())/2, self.__obstaculos[i].y  + (self.__obstaculos[i].image.get_height())/2, self.__config.caminho_imagem_explosao2)
                        explosion_group.add(explosion)
                        self.__obstaculos[i].respawn(x, -1000)
                        self.__jogador.pontos += 1

                    #respawn obstaculo saiu da tela
                    if self.__obstaculos[i].y >= y+20:
                        self.__obstaculos[i].respawn(x, -1000)
                    
                    #posição do rect do obstaculo
                    self.__obstaculos[i].rect.x = self.__obstaculos[i].x
                    self.__obstaculos[i].rect.y = self.__obstaculos[i].y
                
                    #movimentacao do obstaculo
                    self.__obstaculos[i].mover(self.__jogador.rect.x, self.__jogador.rect.y)

                    #cria a image do obstaculo [i]
                    screen.blit(self.__obstaculos[i].image, (self.__obstaculos[i].x, self.__obstaculos[i].y))
            
            #verifica se o projétil do jogador saiu da tela 
            for projetil in self.__jogador.arma.disparos:
                if projetil.rect.y < 0:
                    projetil.kill()  # Remove o projétil
            
            #verifica colisão do jogador com os powerups
            for power in powerups:
                if colisao.check(self.__jogador.rect, power.rect):
                    power.implementar_power(self.__jogador, pygame.time.get_ticks())
                    power.kill() 

            #posição do rect do jogador
            self.__jogador.rect.x = self.__jogador.x
            self.__jogador.rect.y = self.__jogador.y

            self.__jogador.update()

            #pontuação
            texto = font.render(f'PONTOS', True, (255,255,255))
            score = font.render(f'{self.__jogador.pontos}', True, (255,255,255))
            screen.blit(barra_score, (900, 50))
            screen.blit(texto, (917, 65))
            screen.blit(score, (910, 110))

            #mostra a quantidade de vidas
            for i in range(self.__jogador.vidas):
                coracao_x = 40 + i * 60
                coracao_y = 50
                screen.blit(coracao_cheio, (coracao_x, coracao_y))

            #desenha e atualiza projetil e jogador
            self.__jogador.arma.disparos.draw(screen)
            player_group.draw(screen)
            self.__jogador.arma.disparos.update()
            
            #desenhar e atualizar a explosão
            explosion_group.draw(screen)
            explosion_group.update()

            powerups.draw(screen)
            powerups.update()

            #criar imagem do jogador
            screen.blit(self.__jogador.image, (self.__jogador.x, self.__jogador.y))

            #verifica se as vidas do jogador acabaram
            #caso tenha acabado, encerra o laço principal
            if self.__jogador.vidas <= 0:
                explosion = Explosao(self.__jogador.x + (self.__jogador.image.get_width())/2, self.__jogador.y  + (self.__inimigos[i].image.get_height())/2, self.__config.caminho_imagem_explosao1)
                explosion_group.add(explosion)
                for i in range(40):#loop para garantir que a explosão seja exibida por alguns frames
                    # Atualiza a explosão
                    explosion_group.draw(screen)
                    explosion_group.update()
                    pygame.display.update()
                    pygame.time.delay(25)
                pygame.time.delay(100)
                rodando = False

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)  # Limita o jogo a 60 FPS

            contador += 1 #contador é atualizado de acordo com a execução
        return self.__jogador.pontos
        #pygame.quit()


    @property
    def obstaculos(self):
        return self.__obstaculos
    
    @obstaculos.setter
    def obstaculos(self, obstaculos):
        self.__obstaculos = obstaculos

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

    def gerar_power_up(self, inimigo, grupo_power):
        if random.random() > 0.90:
            opcoes = [PowerupArmaTripla(inimigo.rect.center), PowerupVida(inimigo.rect.center), PowerupMaisDano(inimigo.rect.center)]
            pow = random.choice(opcoes)
            grupo_power.add(pow)
