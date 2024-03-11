
import pygame

class Scene:
    """
    setting the base scene so the game can easily do its good work
    """
    def __init__(self, screen):
        self.next_scene = self
        self.screen = screen

    def process_input(self, events):
        pass

    def update(self):
        print('u forgot to override this')
        pass

    def render(self, screen):
        print('u forgot to override this')

    def switch_scene(self, next_scene):
        self.next_scene = next_scene

    def terminate(self):
        self.switch_scene(None)

    