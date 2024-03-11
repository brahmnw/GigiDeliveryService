import pygame

from src.constants import BLACK
from src.game_entities.entity import Entity

class Player(Entity):

    def __init__(
        self, 
        name:str,
        position,
        sprite
    ):
        super().__init__(name,position,sprite)
        self.x = position[0]
        self.y = position[1]
        # distance moved / frame
        self.speed = 2

    def display(self, surface):
        """ draw player on surface """
        pygame.draw.rect(surface, BLACK, pygame.Rect(self.x,self.y,20,20))
        # surface.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed

        if direction == "right":
            self.x += self.speed

        if direction == "up":
            self.y -= self.speed

        if direction == "down":
            self.y += self.speed

        
