import pygame

class Scene:
    """
    setting the base scene so the game can easily do its good work
    """
    def __init__(self, screen, clock):
        self.next_scene = self
        self.screen = screen
        self.clock = clock

    def process_input(self, events):
        pass

    def update(self):
        print('u forgot to override this')
        pass

    def render(self):
        print('u forgot to override this')

    def switch_scene(self, new_scene):
        if new_scene == 'previous':
            new_scene = self
        self.next_scene = new_scene
        

    def terminate(self):
        self.switch_scene(None)

    