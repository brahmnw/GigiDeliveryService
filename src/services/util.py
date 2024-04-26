
def position_is_close(pos1,pos2, uncertainty_x=10, uncertainty_y=10):

    if ((pos2[0] - uncertainty_x) < pos1[0]) and ((pos2[0]+uncertainty_x) > pos1[0]):
        if ((pos2[1] + uncertainty_y) > pos1[1]) and ((pos2[1] - uncertainty_y) < pos1[1]):
            return True
        
    return False
