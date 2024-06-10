import math

import random

from src.objs.enemy import Enemy
from src.objs.projectile import Projectile
from src.services import util

class Drone(Enemy):
    
    """drone will move to a position. do an attack. fuck right off."""
    
    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)
        self.heading_towards = position
        self.end_position = (self.heading_towards[0], -100)
        self.movement_state = 0
        self.attack = self.circle_attack
    
    
    def update_position(self) -> bool:

        try:
            angle = (math.atan((self.position[1] - self.heading_towards[1])/(self.heading_towards[0] - self.position[0]))) 

            if self.x > self.heading_towards[0]:
                angle += math.pi

            elif self.y >= self.heading_towards[1]:
                angle += math.pi

        except ZeroDivisionError:
            
            if self.y > self.heading_towards[1]:
                angle = math.pi/2
                
            else:
                angle = 3*math.pi/2
            
            if self.x > self.heading_towards[0]:
                angle += math.pi

            elif self.y >= self.heading_towards[1]:
                angle += math.pi

        if self.movement_state == 0:
            
            if util.position_is_close((self.x,self.y), self.heading_towards):
                
                self.heading_towards = self.end_position
                self.movement_state = 1
                
                return True     

            self.x += self.speed * math.cos(angle)
            self.y -= self.speed * math.sin(angle)

        else:
            
            self.x += self.speed * math.cos(angle)
            self.y -= self.speed * math.sin(angle)

        self.update_hitbox()
        return False    
