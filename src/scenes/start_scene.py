import pygame

from src.constants import BG_COLOR
from src.objs.gui import button
from src.scenes.scene import Scene
from src.services import util

import textwrap

class StartScene(Scene):
    
    def __init__(self, screen):

        super().__init__(screen)
        self.menu_splash_image = pygame.image.load('assets/img/menusplash.png')
        self.state =  0
        
        self.buttons = [button.PlayButton((100, 550)), button.ExitButton((100, 600))] 
    
    def key_down(self, key):
        
        if key == pygame.K_ESCAPE:
            self.state = 1
            
    def update(self) -> int:
        
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in self.buttons:
            if util.position_is_inside(self.mouse_position, button):
                
                if pygame.mouse.get_pressed()[0]:
                    self.state = button.on_click()
                    
                else:
                    button.on_hover()
            
        return self.state

    def render(self):
        
        self.screen.fill(BG_COLOR)
        # self.screen.blit(self.menu_splash_image, (0,0))
        
        for button in self.buttons:
            button.display(self.screen, 0.1)
        