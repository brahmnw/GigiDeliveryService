import pygame

from src.constants import HITBOX_RED
from src.game_entities.entity import Entity
from src.services.spritesheet import SpriteSheet

class Player(Entity):

    def __init__(
        self, 
        name:str,
        position:tuple
    ):
        
        # initialize entity and set the position of x/y
        super().__init__(name,position)
        self.x = position[0]
        self.y = position[1]
        
        # setting constants
        self.speed = 2
        self.hitbox = (self.x+41,self.y+41, 20, 20)

        # load the player sprite sheet and feed it into spritesheet.py
        sprite_sheet_image = pygame.image.load('img/player.png').convert_alpha()
        self.player_sprite_sheet = SpriteSheet(sprite_sheet_image)

        # initiate all the different sprites
        self.sprites = []

        for frame in range(2):

            self.sprites.append(
                self.player_sprite_sheet.get_image(frame, 32, 32, 3)
            )

        self.current_sprite = 0
        
    def display(self, surface):

        """ draw player on surface """

        # set the speed of the animation (6 FPS from 60 ticks * 0.1 sprites/s)
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        # update the display on the surface
        surface.blit(self.sprites[int(self.current_sprite)], (self.x, self.y))

        # hitbox
        pygame.draw.rect(surface, HITBOX_RED, self.hitbox)

    def move(self, direction):

        """move the character a direction based on speed of player :>"""

        if direction == "left":
            self.x -= self.speed

        if direction == "right":
            self.x += self.speed

        if direction == "up":
            self.y -= self.speed

        if direction == "down":
            self.y += self.speed


        #hitbox add 41 to both based on the scale to center in a 96x96 image.

        self.hitbox = (self.x+41,self.y+41, 20, 20)
        
