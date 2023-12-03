import random, pygame


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, nome: str, vidas: int, x: int, y: int, velocidade: int, image:str):
        self.__nome = nome
        self.__vidas = vidas
        self.__velocidade = velocidade
        self.__image = image
        self.__x = x
        self.__y = y
        self.__maximo_vidas = vidas
        self.__rect = None
    
    def mover_baixo(self):
        self.__y += self.__velocidade

    def mover(self, jogador_x, jogador_y):
        self.mover_baixo()

    def respawn(self, largura, altura=None):
        self.posicao_aleatoria(largura, altura)
        self.vidas = self.__maximo_vidas

    def posicao_aleatoria(self, largura, altura = None):
        if altura == None:
            self.y = -100
        else:
            self.y = random.randint(altura, 0)
        self.x = random.randint(1, largura-40)

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y