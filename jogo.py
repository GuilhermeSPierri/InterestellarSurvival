from obstaculo import *
from powerup import *
from projetil import *
from personagem import *

class Jogo:
    def __init__(self, projeteis = {}, powerUps = {}, inimigos = {}, tempo_decorrido: float, jogador: Jogador):
        self.__projeteis = projeteis
        self.__powerUps = powerUps
        self.__inimigos = inimigos
        self.__tempo_decorrido = tempo_decorrido
        self.__jogador = jogador

#Getters e setters da classe

    @property
    def projeteis(self):
        return self.__projeteis
    
    @projeteis.setter
    def projeteis(self, projeteis):
        self.projeteis = projeteis

    @property
    def powerUps(self):
        return self.__powerUps
    
    @powerUps.setter
    def powerUps(self, powerUps):
        self.powerUps = powerUps

    @property
    def inimigos(self):
        return self.__inimigos
    
    @inimigos.setter
    def inimigos(self, inimigos):
        self.inimigos = inimigos

    @property
    def tempo_decorrido(self):
        return self.__tempo_decorrido
    
    @tempo_decorrido.setter
    def tempo_decorrido(self, tempo_decorrido):
        self.tempo_decorrido = tempo_decorrido

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.jogador = jogador

#Demais métodos
    
    def cadastrar_jogador(self):
        pass

    def iniciar_jogo(self):
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