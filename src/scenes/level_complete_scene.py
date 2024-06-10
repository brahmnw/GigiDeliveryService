import pygame

from src.constants import BG_COLOR
from src.objs.gui import button
from src.scenes.scene import Scene
from src.services import util

import textwrap

class LevelCompleteScene(Scene):
    
    def __init__(self, screen, win_con, time_elapsed, max_length, lives_remaining):

        super().__init__(screen)
        
        self.win_con = win_con
        self.time_elapsed = time_elapsed
        self.max_length = max_length
        self.lives = lives_remaining
        self.percent_completed = round(time_elapsed/max_length*100,1)
        
        self.TITLE_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 24)
        self.SUBTITLE_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 12)
        
        #self.menu_splash_image = pygame.image.load('assets/img/menusplash.png')
        self.state =  0
        
        self.buttons = [button.MenuButton((self.screen.get_width()/2-50, 550))] 
    
    def key_down(self, key):
        
        if key == pygame.K_ESCAPE:
            self.state = 1
                    
        else:
            self.state = 2
            
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
        
        self.TITLE_FONT.render_to(self.screen, (100,200), f"YOU {self.win_con}!", fgcolor=(255,255,255))
        self.SUBTITLE_FONT.render_to(self.screen, (100,250), f"PROGRESS: {self.percent_completed}% COMPLETED! ({self.time_elapsed}ms/{self.max_length}ms) ",fgcolor=(255,255,255))
        self.SUBTITLE_FONT.render_to(self.screen, (100,300), f"LVIES REMAINING: {self.lives}",fgcolor=(255,255,255))
        
        for button in self.buttons:
            button.display(self.screen, 0.1)
        