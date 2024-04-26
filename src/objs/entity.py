import pygame

from src.constants import HITBOX_RED
from src.services.spritesheet import SpriteSheet

class Entity():

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

        # set constants
        self.name: str = sprite_name
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.hitbox_args = hitbox_args
        self.render_scale = render_scale
        self.speed = speed
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

        # calculate hitbox values

        self.hitbox = (self.x+self.hitbox_args[0], self.y+self.hitbox_args[1], self.hitbox_args[2], self.hitbox_args[3])
        self.hitbox_rect = pygame.Rect(self.hitbox)

        self.hitbox_x_center = int(self.hitbox[0] + (1/2) * self.hitbox[2])
        self.hitbox_y_center = int(self.hitbox[1] + (1/2) * self.hitbox[3])

        self.hitbox_left = self.hitbox[0]
        self.hitbox_top = self.hitbox[1]
        self.hitbox_right = self.hitbox[0] + self.hitbox[2]
        self.hitbox_bottom = self.hitbox[1] + self.hitbox[3]

        # load the sprite sheet for the entity and feed it into spritesheet
        sprite_sheet_image = pygame.image.load('assets/img/spritesheets/{0}.png'.format(sprite_name)).convert_alpha()
        self.player_sprite_sheet = SpriteSheet(sprite_sheet_image)

        # initiate all the different sprites for the entity
        self.sprites = []

        for frame in range(sprite_animation_frames):

            self.sprites.append(
                self.player_sprite_sheet.get_image(frame, sprite_width, sprite_height, render_scale)
            )

        self.current_sprite = 0
        
    def display(self, surface: pygame.Surface, animation_speed: float, show_hitbox=False):

        """
        drawing the sprijt on a surface.

        Args:
            surface (pygame.Surface): The surface which the entity will be drawn on
            animation_speed (float): Sets the speed of the animation in frames/tick.
            show_hitbox (bool): Toggles whether or not the hitbox is displayed. (default: False)
        """

        # set the speed of the animation
        self.current_sprite += animation_speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        # update the display on the surface
        surface.blit(self.sprites[int(self.current_sprite)], (self.x, self.y))

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
    
    

    def relative_adjust(self, screen: pygame.Surface, x_relative_pos=None, y_relative_pos=None):

        """
        adjusts based on a fraction of the screen 
        
        Args:
            screen (pygame.Surface): surface to center on.
            x_relative_pos: value from 0 - 1, aligns sprite to that x location. default=None
            y_relative_pos: value from 0 - 1, aligns sprite to that y location. default=None
        """

        if x_relative_pos is not None:
            self.x = screen.get_width() * x_relative_pos - self.sprite_width * self.render_scale * (1/2)

        if y_relative_pos is not None:
            self.y = screen.get_height() * y_relative_pos - self.sprite_height * self.render_scale * (1/2)

        self.update_hitbox()

        return None
        
