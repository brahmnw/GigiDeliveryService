import pygame

from src.constants import BG_COLOR
from src.scenes.scene import Scene

class StartScene(Scene):
    
    def __init__(self, screen):

        super().__init__(screen)
        self.menu_splash_image = pygame.image.load('assets/img/menusplash.png')
        self.state =  0
        
    def key_down(self, key):
        
        if key == pygame.K_ESCAPE:
            self.state = 1
                    
        else:
            self.state = 2

    def render(self):
        
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.menu_splash_image, (0,0))
        