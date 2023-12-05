from factories.InimigoBaseFactory import InimigoBaseFactory
from factories.InimigoZigzagFactory import InimigoZigzagFactory
from factories.ObstaculoFactory import ObstaculoFactory
from factories.ObstaculoPerseguidorFactory import ObstaculoPerseguidorFactory
import pygame


class Dificuldade():

    def __init__(self):
        self.__nivel = 0
        self.__inimigo_base_factory = InimigoBaseFactory()
        self.__inimigo_zig_zag_factory = InimigoZigzagFactory()
        self.__obstaculo_factory = ObstaculoFactory()
        self.__obstaculo_perseguidor_factory = ObstaculoPerseguidorFactory()
    
    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    def controle_dificuldade(self, x, y, tempo, obstaculos, inimigos):

        tamanho_onda_obstaculo = 0
        tamanho_onda_inimigo = 0
        tamanho_onda_inimigo_zig_zag = 0
        tamanho_onda_obstaculo_perseguidor = 0

        vida_max_obstaculo = 1
        vida_min_obstaculo = 1
        velocidade_maxima_obstaculo = 3
        velocidade_minima_obstaculo = 5
        escala_x_obstaculo = 70
        escala_y_obstaculo = 70

        vida_min_inimigo = 1
        vida_max_inimigo = 1
        velocidade_minima_inimigo = 3
        velocidade_maxima_inimigo = 5
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

            tamanho_onda_inimigo_zig_zag = 1
            tamanho_onda_inimigo = 3
            velocidade_minima_inimigo = 3
            velocidade_maxima_inimigo = 5
        
        elif self.__nivel == 2 and tempo >= 25000:

            self.__nivel += 1

            tamanho_onda_obstaculo_perseguidor = 1

            tamanho_onda_obstaculo = 1
            vida_min_obstaculo = 3
            vida_max_obstaculo = 4
            velocidade_minima_obstaculo = 4
            velocidade_maxima_obstaculo = 5

            tamanho_onda_inimigo_zig_zag = 1
            tamanho_onda_inimigo = 3
            vida_min_inimigo = 1
            vida_max_inimigo = 2
            velocidade_minima_inimigo = 4
            velocidade_maxima_inimigo = 6
        
        elif self.__nivel == 3 and tempo >= 35000:
            self.__nivel += 1

            tamanho_onda_obstaculo_perseguidor = 2

            tamanho_onda_obstaculo = 1
            vida_min_obstaculo = 7
            vida_max_obstaculo = 8
            velocidade_minima_obstaculo = 4
            velocidade_maxima_obstaculo = 5
            escala_x_obstaculo = 100
            escala_y_obstaculo = 100
            
            tamanho_onda_inimigo = 3
            vida_min_inimigo = 1
            vida_max_inimigo = 3
            velocidade_minima_inimigo = 5
            velocidade_maxima_inimigo = 6
        
        elif self.__nivel == 4 and tempo >= 45000:
            self.__nivel += 1
            tamanho_onda_inimigo_zig_zag = 3
            
            
        for i in range(tamanho_onda_obstaculo):
            obstaculo = self.__obstaculo_factory.criar_objeto(0, -2000, vida_min_obstaculo, vida_max_obstaculo, velocidade_minima_obstaculo, velocidade_maxima_obstaculo)
            obstaculo.image = pygame.image.load(obstaculo.image).convert_alpha()
            obstaculo.image = pygame.transform.scale(obstaculo.image, (escala_x_obstaculo, escala_y_obstaculo))
            obstaculo.posicao_aleatoria(x, -1000)
            obstaculo.rect = obstaculo.image.get_rect()
            obstaculos.append(obstaculo)
        
        for i in range(tamanho_onda_obstaculo_perseguidor):
            obstaculo = self.__obstaculo_perseguidor_factory.criar_objeto(0, -3500, 3, 5, 1, 2)
            obstaculo.image = pygame.image.load(obstaculo.image).convert_alpha()
            obstaculo.image = pygame.transform.scale(obstaculo.image, (50, 50))
            obstaculo.posicao_aleatoria(x, -1000)
            obstaculo.rect = obstaculo.image.get_rect()
            obstaculos.append(obstaculo)
        
        for i in range(tamanho_onda_inimigo):
            inimigo = self.__inimigo_base_factory.criar_objeto(0, -1000, vida_min_inimigo, vida_max_inimigo, velocidade_minima_inimigo, velocidade_maxima_inimigo)
            inimigo.image = pygame.image.load(inimigo.image).convert_alpha()
            inimigo.image = pygame.transform.scale(inimigo.image, (escala_x_inimigo, escala_y_inimigo))
            inimigo.posicao_aleatoria(x, -1000)
            inimigo.rect = inimigo.image.get_rect()
            inimigos.append(inimigo)
        
        for i in range(tamanho_onda_inimigo_zig_zag):
            inimigo = self.__inimigo_zig_zag_factory.criar_objeto(0, -1000, 1, 1, 3, 4)
            inimigo.image = pygame.image.load(inimigo.image).convert_alpha()
            inimigo.image = pygame.transform.scale(inimigo.image, (escala_x_inimigo, escala_y_inimigo))
            inimigo.posicao_aleatoria(x, -1000)
            inimigo.rect = inimigo.image.get_rect()
            inimigos.append(inimigo)

    