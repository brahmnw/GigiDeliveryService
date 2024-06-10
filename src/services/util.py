"""
util file contains common functions between files.
58
"""
from pickle import TRUE
from src.objs.element import Element

def position_is_close(pos1,pos2, uncertainty_x=10, uncertainty_y=10) -> bool:
    
    """checks if pos1 is close to pos2 within the uncertainties provided"""
    
    if ((pos2[0] - uncertainty_x) < pos1[0]) and ((pos2[0] + uncertainty_x) > pos1[0]):
        if ((pos2[1] + uncertainty_y) > pos1[1]) and ((pos2[1] - uncertainty_y) < pos1[1]):
            return True
        
    return False

def position_is_inside(pos,  element: Element) -> bool:
    
    """checks if position is inside an element."""
    
    element_l = element.x
    element_t = element.y
    element_r = element.x + element.sprite_width*element.render_scale
    element_b = element.y + element.sprite_height*element.render_scale
    
    
    if pos[0] < element_r and pos[0] > element_l:
        if pos[1] < element_b and pos[1] > element_t:
            return True 
        
    else:
        return False
