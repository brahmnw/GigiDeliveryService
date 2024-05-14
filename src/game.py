import pygame

from src.constants import FRAME_RATE
from src.services.scene_man import SceneMan

class Game:

    def __init__(self, screen, clock):
        
        # set default scene
        self.scene_man = SceneMan(screen)
        self.screen = screen
        self.clock = clock

    def run(self):

        while self.scene_man.scene != None:
            
            self.scene_man.process()
            pygame.display.flip()
            self.clock.tick(FRAME_RATE)
