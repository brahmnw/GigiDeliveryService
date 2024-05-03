import pygame

from src.scenes.scene import Scene
from src.scenes.level_scene import LevelScene

class MenuSplashScene(Scene):
    
    def __init__(self, screen, clock):

        super().__init__(screen, clock)
        self.menu_splash_image = pygame.image.load('assets/img/menusplash.png')
        
    def process_input(self, events):
        
        for event in events:

            if event.type == pygame.QUIT:
                self.terminate()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    
                    self.terminate()
                    
                else:
                    
                    self.switch_scene(LevelScene(self.screen, self.clock))

    def update(self):
        
        pass

    def render(self):
        self.screen.blit(self.menu_splash_image, (0,0))
        