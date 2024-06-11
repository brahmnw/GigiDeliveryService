"""
util file contains common functions between files.
58
"""
import math
from pickle import TRUE
from src.objs.element import Element

def value_is_close(value1, value2, uncertainty=10) -> bool:
    
    """checks if val1 is close to val2 within the uncertainties provided"""
    
    if ((value1 - uncertainty) < value2) and ((value1 + uncertainty) > value2):
        return True
        
    return False

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

def position_to_angle(pos1, pos2) -> float:
    """converts two positions to angles"""
    try:
        angle = (math.atan((pos2[1] - pos1[1])/(pos1[0] - pos2[0]))) 

    except ZeroDivisionError:
            
        if pos1[1] > pos2[1]:
            return math.pi/2
                
        else:
            return -math.pi/2

    else:
        """
        if value_is_close(pos1[1], pos2[1]) and pos1[1] > pos2[1]:
            return math.pi/2
        elif value_is_close(pos1[1], pos2[1]) and pos1[1] < pos2[1]:
            return -math.pi/2
        elif value_is_close(pos1[0], pos2[0]) and pos1[0] > pos2[0]:
            return 0
        elif value_is_close(pos1[0], pos2[0]) and pos1[0] < pos2[0]:
            return math.pi
        """
        
        if pos1[0] < pos2[0] and pos1[1] > pos2[1]:
            return angle
        elif pos1[0] > pos2[0] and pos1[1] > pos2[1]:
            return math.pi - angle
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
            return -math.pi + angle
        elif pos1[0] < pos2[0] and pos1[1] < pos2[1]:
            return -angle
        elif pos1[0] > pos2[0]:
            return math.pi
        elif pos1[0] < pos2[0]:
            return math.pi
        
