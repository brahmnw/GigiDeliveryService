import pygame
from src.objs.element import Element

class Button(Element):
    
    """defines the base class for a button"""
    
    def __init__(self, sprite_name:str, position:tuple, render_scale=2, sprite_width=100, sprite_height=20):
        super().__init__(sprite_name, 1, position, render_scale, sprite_width, sprite_height)
    
    def display(self, surface: pygame.Surface, animation_speed: float) -> None:
        
        self.on_display(surface, animation_speed)
        
    def on_hover(self) -> int:
        
        pass
        
    def on_click(self) -> int:
        
        print("clicked!")

class PlayButton(Button):
    
    """PlayButton"""
    
    def __init__(self, position:tuple, render_scale=2, sprite_width=100, sprite_height=20):
        super().__init__("gui_button_play", position, render_scale, sprite_width, sprite_height)
    
    def display(self, surface: pygame.Surface, animation_speed: float) -> None:
        
        self.on_display(surface, animation_speed)
        
    def on_click(self) -> int:
        
        return 2
    
class ExitButton(Button):
    
    """ExitButton"""
    
    def __init__(self, position:tuple, render_scale=2, sprite_width=100, sprite_height=20):
        super().__init__("gui_button_exit", position, render_scale, sprite_width, sprite_height)
    
    def display(self, surface: pygame.Surface, animation_speed: float) -> None:
        
        self.on_display(surface, animation_speed)     
        
    def on_click(self) -> int:
        
        return 1
    
class MenuButton(Button):
    
    """ExitButton"""
    
    def __init__(self, position:tuple, render_scale=2, sprite_width=100, sprite_height=20):
        super().__init__("gui_button_menu", position, render_scale, sprite_width, sprite_height)
    
    def display(self, surface: pygame.Surface, animation_speed: float) -> None:
        
        self.on_display(surface, animation_speed)
        
    def on_click(self) -> int:
        
        return 3