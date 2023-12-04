import pygame
from estados.EstadoGenerico import EstadoGenerico
from logica_de_jogo.Jogo import Jogo
from singleton.Configuracoes import Configuracoes
import time


class EstadoJogar(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT():
                pygame.quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.jogo.mudar_estado(self.jogo.estado_menu)

                elif evento.key == pygame.K_SPACE:
                    self.jogo.self.som_shoot_jogador.play() 
  
    def atualizar(self):
        pass

    def desenhar(self):

        config = Configuracoes()
        #carrega a musica e inicia o jogo
        pygame.mixer.music.load(config.audio_jogo)
        p = Jogo()
        pygame.mixer.music.play(-1)
        pontos = p.iniciar_jogo()
        
        #logo após o jogo acabar, para a musica, troca de estado e atualiza a última pontuação
        config.persistencia.update_highscore('Jogador', pontos)
        #config.ultima_pontuacao(pontos)
        #print(pontos)
        pygame.mixer.music.stop()
        self.jogo.mudar_estado(self.jogo.estado_game_over)

        #inicia o som de game over
        self.jogo.som_game_over.play()
        pygame.mixer.music.load(config.audio_home)
        time.sleep(2)
        pygame.mixer.music.play(-1)

