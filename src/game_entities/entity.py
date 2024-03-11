import pygame

class Entity(pygame.Surface):
    """
    This class defines any object on the screen of the game
    """

    def __init__(self, name:str, position, sprite: pygame.Surface):
        self.name: str = name
        self.position = position
        self.sprite: pygame.Surface = sprite

    def get_rect(self):
        return self.sprite.get_rect(topleft=self.position)

