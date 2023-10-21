class Projetil:
    def __init__(self, x: int, y: int, velocidade: int, dano: int, imagem: str):
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__dano = dano
        self.__imagem = imagem

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
        else:
            self.__y -= velocidade_desejada
    
    def mover_baixo(self, velocidade_desejada=None):
        if velocidade_desejada == None:
            self.__y += self.__velocidade
        else:
            self.__y += velocidade_desejada

    def respawn(self, pos_x_player, pos_y_player):
        self.__x = pos_x_player +15
        self.__y = pos_y_player +5
        self.__velocidade = 0

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

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
