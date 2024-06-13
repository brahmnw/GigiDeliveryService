import pygame
from pygame import mixer
from src.scenes.level_scene import LevelScene
from src.scenes.level_complete_scene import LevelCompleteScene
from src.scenes.start_scene import StartScene

class SceneMan():
    
    """
    the scene manager for the game
    """
    
    def __init__(self, screen):
        
        mixer.music.load('assets/music/menu.mp3')
        self.screen = screen
        self.scene = StartScene(screen)
        mixer.music.play(-1)
    
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
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load('assets/music/level.mp3')
            self.scene = LevelScene(self.screen)
            mixer.music.play(-1)
            
        elif state == 3:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load('assets/music/menu.mp3')
            self.scene = StartScene(self.screen)
            mixer.music.play(-1)

        elif state == 4:
            conditions = self.scene.level_conditions
            mixer.music.stop()
            mixer.music.unload()
            
            self.scene = LevelCompleteScene(self.screen, *conditions)

            if conditions[0] == "WIN!":
                mixer.music.load('assets/music/win.mp3')
                mixer.music.play(-1)
            else:
                mixer.music.load('assets/music/lose.mp3')
                mixer.music.play(-1)
            
        
        
        
        
        