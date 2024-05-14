"""
util file contains common functions between files.
"""

def position_is_close(pos1,pos2, uncertainty_x=10, uncertainty_y=10) -> bool:
    
    """checks if pos1 is close to pos2 within the uncertainties provided"""
    
    if ((pos2[0] - uncertainty_x) < pos1[0]) and ((pos2[0]+uncertainty_x) > pos1[0]):
        if ((pos2[1] + uncertainty_y) > pos1[1]) and ((pos2[1] - uncertainty_y) < pos1[1]):
            return True
        
    return False
