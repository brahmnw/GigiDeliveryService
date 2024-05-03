import pygame

from src.constants import FRAME_RATE
from src.scenes.scene import Scene
from src.scenes.menu_splash_scene import MenuSplashScene
from src.scenes.level_scene import LevelScene

class Game:

    def __init__(self, screen, clock):
        
        # set default scene
        self.active_scene = Scene(screen, clock)
        self.screen = screen
        self.clock = clock

    def run(self):
        
        self.active_scene.switch_scene(MenuSplashScene(self.screen, self.clock))

        while self.active_scene != None:
            
            # run everything in the scene
            self.active_scene.process_input(pygame.event.get())
            self.active_scene.update()
            self.active_scene.render()
            self.active_scene = self.active_scene.next_scene

            # tick and update the frame
            pygame.display.flip()
            self.clock.tick(FRAME_RATE)
