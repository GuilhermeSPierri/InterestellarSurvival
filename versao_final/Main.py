import pygame
import sys
from State import GerenciadoraDeEstados


pygame.init()
jogo = GerenciadoraDeEstados()
jogo.executar()
pygame.quit()
sys.exit() 