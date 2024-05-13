import pygame
from src.services.spritesheet import SpriteSheet

class Element:
    
    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, render_scale=1, sprite_width=32, sprite_height=32):
        
        self.name: str = sprite_name
        self.position = position
        self.x = position[0]
        self.y = position[1]
        
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.render_scale = render_scale
        
        # load the sprite sheet for the element and feed it into spritesheet
        sprite_sheet_image = pygame.image.load('assets/img/spritesheets/{0}.png'.format(sprite_name)).convert_alpha()
        self.sprites = SpriteSheet(sprite_sheet_image).get_sprites(sprite_animation_frames, sprite_width, sprite_height, render_scale)
        self.current_sprite = 0
    
    def on_display(self, surface: pygame.Surface, animation_speed = float):
        
            
        """
        drawing the element on a surface.

        Args:
            surface (pygame.Surface): The surface which the entity will be drawn on
            animation_speed (float): Sets the speed of the animation in frames/tick.
        """
        
        # set the speed of the animation
        self.current_sprite += animation_speed
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        # update the display on the surface
        surface.blit(self.sprites[int(self.current_sprite)], (self.x, self.y))
        
    def display(self, surface: pygame.Surface, animation_speed = float):
        
        self.on_display(surface, animation_speed)

       
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

        return None