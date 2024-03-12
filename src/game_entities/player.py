import pygame

from src.constants import HITBOX_RED
from src.game_entities.entity import Entity

class Player(Entity):

    """
    Class extends entity.py :)
    For player controllable entity!!!
    """

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, sprite_width=32, sprite_height=32):
        
        # initialize entity and set the position of x/y
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args)
        
        
        # setting constants
        self.speed = 2 

    
        
