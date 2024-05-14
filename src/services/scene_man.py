import pygame
from src.scenes.level_scene import LevelScene
from src.scenes.start_scene import StartScene

class SceneMan():
    
    """
    the scene manager for the game
    """
    
    def __init__(self, screen):
        
        self.screen = screen
        self.scene = StartScene(screen)
    
    def process(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.scene = None
                return

            if event.type == pygame.KEYDOWN:
                self.scene.key_down(event.key)

        self.scene.key_pressed(pygame.key.get_pressed())
        self.handle_state(self.scene.update())
        self.scene.render()
        
    def handle_state(self, state:int):
        
        if state == 0:
            pass
        
        elif state == 1:
            self.scene = None
            
        elif state == 2:
            self.scene = LevelScene(self.screen)
            
        elif state == 3:
            self.scene = StartScene(self.screen)
            
        
        
        
        
        