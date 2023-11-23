import pygame
from EstadoGenerico import EstadoGenerico
from Jogo import Jogo
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
        #carrega a musica e inicia o jogo
        pygame.mixer.music.load('versao_final/assets/audio/MyVeryOwnDeadShip.ogg')
        p = Jogo()
        pygame.mixer.music.play(-1)
        p.iniciar_jogo()
        
        #logo após o jogo acabar, para a musica e troca de estado
        pygame.mixer.music.stop()
        self.jogo.mudar_estado(self.jogo.estado_game_over)

        #inicia o som de game over
        self.jogo.som_game_over.play()
        pygame.mixer.music.load('versao_final/assets/audio/Home.wav')
        time.sleep(2)
        pygame.mixer.music.play(-1)

