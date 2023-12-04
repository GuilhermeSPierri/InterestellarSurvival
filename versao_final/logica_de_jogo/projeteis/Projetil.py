import pygame
from singleton.Configuracoes import Configuracoes


class Projetil(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, velocidade: int, dano: int):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__dano = dano
        config = Configuracoes()
        self.__image = pygame.image.load(config.img_projetil_verde)
        self.__image = pygame.transform.rotate(self.__image, 90)
        self.__rect = self.__image.get_rect(center = (x, y))

    def update(self):
        # Movimentar o projétil
        if self.__y <= 0:
            self.kill()
        else:
            self.__rect.y -= self.__velocidade

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def dano(self):
        return self.__dano
    
    @dano.setter
    def dano(self, dano):
        self.__dano = dano
