import pygame

class Scene:
    
    """
    setting the base scene so the scene manager can easily do its good work without 
    """
    
    def __init__(self, screen):
        
        self.screen = screen
        self.state = 0 
    
    def key_down(self, events) -> None:
        pass
    
    def key_pressed(self, events) -> None:
        pass

    def update(self) -> int:
        """should return True if starting new scene"""
        return self.state

    def render(self) -> None:
        pass

    