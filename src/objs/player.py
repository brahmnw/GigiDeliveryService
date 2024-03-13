import pygame

from src.constants import HITBOX_RED
from src.objs.entity import Entity

class Player(Entity):

    """
    Class extends entity.py :)
    For player controllable entity!!!
    """

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32, initial_health=3):
        
        # initialize entity and set the position of x/y
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)
        self.health = initial_health
        
