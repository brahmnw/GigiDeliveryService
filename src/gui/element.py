import pygame
from src.services.spritesheet import SpriteSheet

class Element:
    
    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        self.name: str = sprite_name
        self.position = position
        self.x = position[0]
        self.y = position[1]
        
        # load the sprite sheet for the entity and feed it into spritesheet
        sprite_sheet_image = pygame.image.load('assets/img/spritesheets/{0}.png'.format(sprite_name)).convert_alpha()
        self.sprite_sheet = SpriteSheet(sprite_sheet_image).get_sprites(sprite_animation_frames, sprite_width, sprite_height, render_scale)
    
    def display(self, surface: pygame.Surface, animation_speed: float):

        """
        drawing the elem,ent on a surface.

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