import pygame
from src.game import Game
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

if __name__ == '__main__':
    g = Game(screen, clock)
    g.run()
    pygame.quit()
