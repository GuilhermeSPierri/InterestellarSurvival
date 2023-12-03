from logica_de_jogo.fases.Fase import Fase


class Jogo:
    def __init__(self):
        self.__fases = [
            Fase(0)
        ]
        
    @property
    def fases(self):
        return self.__fases
    
    @fases.setter
    def fases(self, fases):
        self.__fases = fases
    
    def iniciar_jogo(self):
        return self.__fases[0].iniciar()
