import pygame

from src.constants import BLACK

class SpriteSheet:

    def __init__(self, sheet_image):
        self.sheet = sheet_image

    def get_image(self, frame, width, height, scale=1):
        
        """
        Returns an image from a loaded spritesheet.
        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), (0, frame*height, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(BLACK)

        return image
