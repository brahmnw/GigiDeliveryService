import pygame
from src.constants import BLACK

class Entity(pygame.Surface):
    """
    This class defines any object on the screen of the game
    """

    def __init__(self, name:str, position):
        self.name: str = name
        self.position = position

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.position)

