import pygame


from src.constants import HITBOX_RED
from src.objs.element import Element

class Entity(Element):

    """
    this forp any objct that i put on the screeen

    Args:
        sprite_name (str): used for spritesheets n stuff. naming convention for all assets this entity uses will follow this name
        sprite_animation_frames (int): the total amount of frames in the entity.
        position (tuple): a tuple (x,y) which contains the coordinates of the entity.
        hitbox (tuple): a tuple (x_adjustment,y_adjustment,length,width) which contains the hitbox rectangle of the entity
            x_adjustment - amount of pixels to move in the x axis
            y_adjustment -  amount of pixels to move in the y axis
        render_scale (int): magnitude which sprite is scaled up. (default: 1) player uses 3
        speed (int): amount of pixels to move / tick (default: 2)
        sprite_width (int): width of the entity sprite sheet (default: 32)
        sprite_height (int): height of the entity sprite sheet (default: 32)
    """

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        
        super().__init__(sprite_name, sprite_animation_frames, position, render_scale, sprite_width, sprite_height)
        
        # set constants
        
        self.hitbox_args = hitbox_args
        self.speed = speed
        
        # calculate hitbox values

        self.hitbox = (self.x+self.hitbox_args[0], self.y+self.hitbox_args[1], self.hitbox_args[2], self.hitbox_args[3])
        self.hitbox_rect = pygame.Rect(self.hitbox)

        self.hitbox_x_center = int(self.hitbox[0] + (1/2) * self.hitbox[2])
        self.hitbox_y_center = int(self.hitbox[1] + (1/2) * self.hitbox[3])

        self.hitbox_left = self.hitbox[0]
        self.hitbox_top = self.hitbox[1]
        self.hitbox_right = self.hitbox[0] + self.hitbox[2]
        self.hitbox_bottom = self.hitbox[1] + self.hitbox[3]
    
    def display(self, surface: pygame.Surface, animation_speed: float, show_hitbox=False):

        """
        drawing the sprijt on a surface.

        Args:
            surface (pygame.Surface): The surface which the entity will be drawn on
            animation_speed (float): Sets the speed of the animation in frames/tick.
            show_hitbox (bool): Toggles whether or not the hitbox is displayed. (default: False)
        """
        
        self.update_hitbox()
        self.on_display(surface, animation_speed)
        
        # draw the hitbox if show_hitbox is on
        if show_hitbox:
            pygame.draw.rect(surface, HITBOX_RED, self.hitbox, 2)

    def update_hitbox(self):

        self.hitbox = (self.x+self.hitbox_args[0], self.y+self.hitbox_args[1], self.hitbox_args[2], self.hitbox_args[3])
        self.hitbox_rect = pygame.Rect(self.hitbox)

        self.hitbox_x_center = int(self.hitbox[0] + (1/2) * self.hitbox[2])
        self.hitbox_y_center = int(self.hitbox[1] + (1/2) * self.hitbox[3])

        self.hitbox_left = self.hitbox[0]
        self.hitbox_top = self.hitbox[1]
        self.hitbox_right = self.hitbox[0] + self.hitbox[2]
        self.hitbox_bottom = self.hitbox[1] + self.hitbox[3]
    
    

    
        
