import pygame
import sys
from estados.State import GerenciadoraDeEstados


#caso precise colocar um caminho próprio
#sys.path.append(r'c:\atividades\ProjetoFinal\projeto-final-grupo-3-23-2\versao_final')
pygame.init()
jogo = GerenciadoraDeEstados()
jogo.executar()
pygame.quit()
sys.exit() 
