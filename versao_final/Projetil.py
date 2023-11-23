import pygame

class Projetil(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__dano = dano
        self.__image = pygame.image.load("versao_final/assets/imgs/shot1_asset.png")
        self.__image = pygame.transform.rotate(self.__image, 90)
        self.__rect = self.__image.get_rect(center = (x, y))

    def update(self):
        # Movimentar o projétil
        if self.__y <= 0:
            self.kill()
        else:
            self.__rect.y -= self.__velocidade

    def mover_esquerda(self, velocidade_desejada=None):
        if velocidade_desejada == None:
            self.__x -= self.__velocidade
        else:
            self.__x -= velocidade_desejada

    def mover_direita(self, velocidade_desejada=None):
        if velocidade_desejada == None:
            self.__x += self.__velocidade 
        else:
            self.__x += velocidade_desejada
    
    def mover_cima(self, velocidade_desejada=None):
        if velocidade_desejada == None:
            self.__y -= self.__velocidade
            self.__rect.y -= self.__velocidade
        else:
            self.__y -= velocidade_desejada
            self.__rect.y -= velocidade_desejada
    
    def mover_baixo(self, velocidade_desejada=None):
        if velocidade_desejada == None:
            self.__y += self.__velocidade
        else:
            self.__y += velocidade_desejada

    def respawn(self, pos_x_player, adc_x, pos_y_player, adc_y):
        self.__x = pos_x_player + adc_x
        self.__y = pos_y_player + adc_y
        self.__velocidade = 0

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
