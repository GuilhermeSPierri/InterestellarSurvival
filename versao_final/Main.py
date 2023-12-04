import pygame
import sys
from estados.State import GerenciadoraDeEstados


pygame.init()
jogo = GerenciadoraDeEstados()
jogo.executar()
pygame.quit()
sys.exit() 
