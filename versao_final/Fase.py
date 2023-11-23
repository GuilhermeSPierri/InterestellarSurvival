from Obstaculo import Obstaculo
from Powerup import Powerup
from Arma import Arma
from Projetil import Projetil
from Personagem import Personagem
from Jogador import Jogador
from Inimigo import Inimigo
from Colisao import Colisao
from Explosao import Explosao
from InimigoBaseFactory import InimigoBaseFactory
from ObstaculoFactory import ObstaculoFactory
import pygame, random


class Fase:
    def __init__(self, obstaculos,  projeteis, powerUps, inimigos, tempo_decorrido: float):
        self.__obstaculos = obstaculos
        self.__projeteis = projeteis
        self.__powerUps = powerUps
        self.__inimigos = inimigos
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = Jogador("Player 1", 3, 640, 600,
                            Arma("Arma base",
                                 Projetil(0, 0, 9, 1, 'versao_final/assets/imgs/shot1_asset.png', [])
                            ),
                            6, 0, 'versao_final/assets/imgs/jogadorbase.png',
                            ['versao_final/assets/imgs/jogadorbase.png', 'versao_final/assets/imgs/jogadorbase2.png', 'versao_final/assets/imgs/jogadorbase3.png', 'versao_final/assets/imgs/jogadorbase4.png']
                    )
        self.__inimigo_base_factory = InimigoBaseFactory()
        self.__obstaculo_factory = ObstaculoFactory()
        self.__nivel = 0

    def iniciar(self):
        # TAMANHO DA TELA
        x = 1100
        y = 660

        FPS = 80

         #inicia pygame
        pygame.init()

        #cria a janela do jogo
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('Interstellar Survival')

        #clock do jogo
        clock = pygame.time.Clock()

        #fonte do jogo
        font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 30)

        # Carrega os planos de fundo
        bg1 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        bg2 = pygame.image.load('versao_final/assets/imgs/bg.png').convert_alpha()
        bg1 = pygame.transform.scale(bg1, (x, y))
        bg2 = pygame.transform.scale(bg2, (x, y))

        # Posições iniciais dos planos de fundo
        bg1_y = 0
        bg2_y = -bg1.get_height()

        explosao1 = [
            'versao_final/assets/imgs/Explosion3_1.png','versao_final/assets/imgs/Explosion3_2.png',
            'versao_final/assets/imgs/Explosion3_3.png','versao_final/assets/imgs/Explosion3_4.png',
            'versao_final/assets/imgs/Explosion3_5.png','versao_final/assets/imgs/Explosion3_6.png',
            'versao_final/assets/imgs/Explosion3_7.png','versao_final/assets/imgs/Explosion3_8.png',
            'versao_final/assets/imgs/Explosion3_9.png','versao_final/assets/imgs/Explosion3_10.png','versao_final/assets/imgs/Explosion3_11.png',
        ]

        explosao2 = [
            'versao_final/assets/imgs/tile000.png','versao_final/assets/imgs/tile001.png',
            'versao_final/assets/imgs/tile002.png','versao_final/assets/imgs/tile003.png',
            'versao_final/assets/imgs/tile004.png','versao_final/assets/imgs/tile005.png',
            'versao_final/assets/imgs/tile006.png','versao_final/assets/imgs/tile007.png',
            'versao_final/assets/imgs/tile008.png','versao_final/assets/imgs/tile009.png',
            'versao_final/assets/imgs/tile010.png','versao_final/assets/imgs/tile011.png',
            'versao_final/assets/imgs/tile012.png','versao_final/assets/imgs/tile013.png',
            'versao_final/assets/imgs/tile014.png','versao_final/assets/imgs/tile015.png',
            'versao_final/assets/imgs/tile016.png'
        ]
        
        #carrega as imagens da vida
        coracao_cheio = pygame.image.load('versao_final/assets/imgs/coracao_cheio.png').convert_alpha()
        coracao_cheio = pygame.transform.scale(coracao_cheio, (60, 60))

        #carrega a imagem do placar
        barra_score = pygame.image.load('versao_final/assets/imgs/barra_score.png').convert_alpha()
        barra_score = pygame.transform.scale(barra_score, (150, 50))

        #carrega e deixa as imagens do jogador e rotaciona numa determinada escala
        self.__jogador.image = pygame.image.load(self.__jogador.image).convert_alpha()
        self.__jogador.image = pygame.transform.scale(self.__jogador.image, (80, 40))
        self.__jogador.image = pygame.transform.rotate(self.__jogador.image, 90)

        #coloca a nave do jogador na posição inicial
        self.__jogador.x = 640
        self.__jogador.y = 600

        horizontal, vertical = self.__jogador.image.get_size()

        #pega o rect da image jogador (usado para verificar colisões)
        self.__jogador.rect = self.__jogador.image.get_rect()

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

        #adiciona projetil aos sprites
        self.__jogador.arma.disparos = pygame.sprite.Group()

        tempo_inicio_execucao = pygame.time.get_ticks()

        self.__tempo_decorrido = 0

        tempo_ultimo_tiro = self.__tempo_decorrido
        delay_entre_tiros = 300  # Defina o atraso desejado em milissegundos (por exemplo, 500 ms).

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
            
            self.controle_dificuldade(x, -1000, self.__tempo_decorrido)
            
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
            tempo_atual = self.__tempo_decorrido
            if tecla[pygame.K_SPACE] and (tempo_atual - tempo_ultimo_tiro) > delay_entre_tiros:
                self.__jogador.arma.disparos.add(self.__jogador.arma.atirar(self.__jogador.x + round(horizontal/2), self.__jogador.y ,5, 1, 'versao_final/assets/imgs/shot1_asset.png', []))
                tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro

            #colisoes ou respawn
            if contador != 0: #verifica se não está no primeiro laço

                colisao = Colisao() #variavel que vai ser utilizada pra verificar colisão

                #laço dos inimigos
                for i in range(len(self.__inimigos)):
                    if random.randrange(0, 100) == 1 and self.__inimigos[i].y>0:
                        self.__inimigos[i].arma.disparos.add(self.__inimigos[i].arma.atirar(self.__inimigos[i].x + (self.__inimigos[i].image.get_width())/2, self.__inimigos[i].y  + (self.__inimigos[i].image.get_height())/2,7, 1, 'versao_final/assets/imgs/shot4_5.png', []))
                    self.__inimigos[i].arma.disparos.draw(screen)
                    self.__inimigos[i].arma.disparos.update(y)

                    #checa se o inimigo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__inimigos[i].rect):
                        self.__jogador.vidas -= 1
                        self.__jogador.diminuir_pontos(1)
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
                            self.__inimigos[i].vidas -= 1
                            projetil.kill()  # Remove o projétil após acertar um inimigo

                    #respawn inimigo morreu
                    if self.__inimigos[i].vidas <= 0:
                        explosion = Explosao(self.__inimigos[i].x + (self.__inimigos[i].image.get_width())/2, self.__inimigos[i].y  + (self.__inimigos[i].image.get_height())/2, explosao1)
                        explosion_group.add(explosion)
                        if random.random() > 0.9:
                            pow = Powerup(self.__inimigos[i].rect.center)
                            powerups.add(pow)
                        self.__inimigos[i].respawn(x, -1000)
                        self.__jogador.pontos += 1

                    #respawn inimigo saiu da tela
                    if self.__inimigos[i].y >= y+20:
                        self.__inimigos[i].respawn(x, -1000)
                    
                    #posição do rect do inimigo
                    self.__inimigos[i].rect.x = self.__inimigos[i].x
                    self.__inimigos[i].rect.y = self.__inimigos[i].y
                
                    #movimentacao do inimigo, somente para baixo
                    self.__inimigos[i].mover()

                    #cria a image do inimigo [i]
                    screen.blit(self.__inimigos[i].image, (self.__inimigos[i].x, self.__inimigos[i].y))
                
                #laço dos obstaculos
                for i in range(len(self.__obstaculos)):

                    #checa se o obstaculo da posição [i] da lista colidiu com o jogador
                    if colisao.check(self.__jogador.rect, self.__obstaculos[i].rect):
                        self.__jogador.vidas -= 1
                        self.__obstaculos[i].vidas = 0
                        self.__jogador.diminuir_pontos(1)
                    
                    #checa se o obstaculo da posição [i] da lista foi acertado com o projétil
                    for projetil in self.__jogador.arma.disparos:
                        if colisao.check(self.__obstaculos[i].rect, projetil.rect):
                            self.__obstaculos[i].vidas -= 1
                            projetil.kill()  # Remove o projétil após acertar um inimigo

                    #respawn obstaculo destruido
                    if self.__obstaculos[i].vidas <= 0:
                        explosion = Explosao(self.__obstaculos[i].x + (self.__obstaculos[i].image.get_width())/2, self.__obstaculos[i].y  + (self.__obstaculos[i].image.get_height())/2, explosao2)
                        explosion_group.add(explosion)
                        self.__obstaculos[i].respawn(x, -1000)
                        self.__jogador.pontos += 1

                    #respawn obstaculo saiu da tela
                    if self.__obstaculos[i].y >= y+20:
                        self.__obstaculos[i].respawn(x, -1000)
                    
                    #posição do rect do obstaculo
                    self.__obstaculos[i].rect.x = self.__obstaculos[i].x
                    self.__obstaculos[i].rect.y = self.__obstaculos[i].y
                
                    #movimentacao do obstaculo, somente para baixo
                    self.__obstaculos[i].mover()

                    #cria a image do obstaculo [i]
                    screen.blit(self.__obstaculos[i].image, (self.__obstaculos[i].x, self.__obstaculos[i].y))
            
            #verifica se o projétil do jogador saiu da tela 
            for projetil in self.__jogador.arma.disparos:
                if projetil.rect.y < 0:
                    projetil.kill()  # Remove o projétil após acertar um inimigo

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

            #desenha o rect do projetil e jogador
            self.__jogador.arma.disparos.draw(screen)
            player_group.draw(screen)
            self.__jogador.arma.disparos.update()
            
            #desenhar e atualizar a explosão
            explosion_group.draw(screen)
            explosion_group.update()

            powerups.draw(screen)
            powerups.update()

            #criar imagens do projetil e jogador
            #screen.blit(self.__jogador.arma.projetil.image, (self.__jogador.arma.projetil.x, self.__jogador.arma.projetil.y))
            screen.blit(self.__jogador.image, (self.__jogador.x, self.__jogador.y))

            #verifica se as vidas do jogador acabaram
            #caso tenha acabado, encerra o laço principal
            if self.__jogador.vidas <= 0:
                explosion = Explosao(self.__jogador.x + (self.__jogador.image.get_width())/2, self.__jogador.y  + (self.__inimigos[i].image.get_height())/2, explosao1)
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

        #pygame.quit()

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
    
    def controle_dificuldade(self, x, y, tempo):

        tamanho_onda_obstaculo = 0
        tamanho_onda_inimigo = 0

        vida_max_obstaculo = 0
        vida_min_obstaculo = 0
        velocidade_maxima_obstaculo = 0
        velocidade_minima_obstaculo = 0
        escala_x_obstaculo = 70
        escala_y_obstaculo = 70

        velocidade_minima_inimigo = 0
        velocidade_maxima_inimigo = 0
        escala_x_inimigo = 70
        escala_y_inimigo = 70

        if self.__nivel==0:

            self.__nivel += 1

            tamanho_onda_obstaculo = 3
            vida_min_obstaculo = 3
            vida_max_obstaculo = 5
            velocidade_minima_obstaculo = 3
            velocidade_maxima_obstaculo = 4

            tamanho_onda_inimigo = 3
            velocidade_minima_inimigo = 3
            velocidade_maxima_inimigo = 4
            
        
        elif self.__nivel == 1 and tempo >= 10000:
            
            self.__nivel += 1

            tamanho_onda_obstaculo = 1
            vida_min_obstaculo = 3
            vida_max_obstaculo = 5
            velocidade_minima_obstaculo = 3
            velocidade_maxima_obstaculo = 4

            tamanho_onda_inimigo = 3
            velocidade_minima_inimigo = 3
            velocidade_maxima_inimigo = 5
        
        elif self.__nivel == 2 and tempo >= 25000:

            self.__nivel += 1

            tamanho_onda_obstaculo = 1
            vida_min_obstaculo = 3
            vida_max_obstaculo = 4
            velocidade_minima_obstaculo = 4
            velocidade_maxima_obstaculo = 5

            tamanho_onda_inimigo = 3
            velocidade_minima_inimigo = 4
            velocidade_maxima_inimigo = 6
        
        elif self.__nivel == 3 and tempo >= 35000:
            self.__nivel += 1

            tamanho_onda_obstaculo = 1
            vida_min_obstaculo = 7
            vida_max_obstaculo = 8
            velocidade_minima_obstaculo = 4
            velocidade_maxima_obstaculo = 5
            escala_x_obstaculo = 100
            escala_y_obstaculo = 100
            
            tamanho_onda_inimigo = 3
            velocidade_minima_inimigo = 5
            velocidade_maxima_inimigo = 6
            
        for i in range(tamanho_onda_obstaculo):
            obstaculo = self.__obstaculo_factory.criar_objeto(0, -2000, vida_min_obstaculo, vida_max_obstaculo, velocidade_minima_obstaculo, velocidade_maxima_obstaculo)
            obstaculo.image = pygame.image.load(obstaculo.image).convert_alpha()
            obstaculo.image = pygame.transform.scale(obstaculo.image, (escala_x_obstaculo, escala_y_obstaculo))
            obstaculo.posicao_aleatoria(x, -1000)
            obstaculo.rect = obstaculo.image.get_rect()
            self.__obstaculos.append(obstaculo)
        
        for i in range(tamanho_onda_inimigo):
            inimigo = self.__inimigo_base_factory.criar_objeto(0, -1000, 1, velocidade_minima_inimigo, velocidade_maxima_inimigo)
            inimigo.image = pygame.image.load(inimigo.image).convert_alpha()
            inimigo.image = pygame.transform.scale(inimigo.image, (escala_x_inimigo, escala_y_inimigo))
            inimigo.posicao_aleatoria(x, -1000)
            inimigo.rect = inimigo.image.get_rect()
            self.__inimigos.append(inimigo)
            
    
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

