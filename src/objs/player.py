import pygame

from src.constants import HITBOX_RED
from src.objs.entity import Entity

class Player(Entity):

    """
    Class extends entity.py :)
    For player controllable entity!!!
    """

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=3, sprite_width=32, sprite_height=32, initial_health=3):
        
        # initialize entity and set the position of x/y
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)
        self.health = initial_health
        
    def move(self, direction):

        """
        move the entity a direction based on its speed :>

        Args:
            direction (str): either left/right/up/down and adjusts the position of player based on speed.
        
        """

        if direction == "left":
            self.x -= self.speed

        if direction == "right":
            self.x += self.speed

        if direction == "up":
            self.y -= self.speed

        if direction == "down":
            self.y += self.speed

        self.update_hitbox()