import math

import random

from src.objs.enemy import Enemy
from src.objs.projectile import Projectile
from src.services import util
from pickle import FALSE

class Boss(Enemy):
    
    """dhar man"""
    
    def __init__(self):
        super().__init__("dhar-hero-3", 1, (300,0), (14,14,12,12), 0.05, sprite_width=997, sprite_height=1394)
        self.heading_towards = (310,400)
        self.speed = 5
        self.moves = [
            [0, 'boss_set_heading', [310,400]],
            [2000, 'boss.circle_attack', []],
            [2100, 'boss_set_heading', [100,100]],
            [2300, 'boss.basic_attack', []],
            [2350, 'boss.basic_attack', []],
            [2400, 'show_dialogue_text', [
                None, 
                ["Evil Dhar", "hahahaha i will unleash my wath on you.. bewear.", "phone_guy.png"]
            ]],
            [2500, 'rain_projectiles', [10, 10]]
        ]
    
    
    def update_position(self):
        
        if util.position_is_close((self.x,self.y), self.heading_towards):
            
            self.update_hitbox()
            return False 

        try:
            
            angle = (math.atan((self.position[1] - self.heading_towards[1])/(self.heading_towards[0] - self.position[0]))) 

            if self.x > self.heading_towards[0] and self.y >= self.heading_towards[1]:
                angle = math.pi - angle
                
            elif self.x > self.heading_towards[0] :
                angle += math.pi
            
            elif self.y >= self.heading_towards[1]:
                angle += math.pi
                
            
                if not self.x < self.heading_towards[0]+5 and self.x > self.heading_towards[0]-5:
            
                    self.x += self.speed * math.cos(angle)
            
            if not self.y > self.heading_towards[1]+5 and self.y < self.heading_towards[1]-5:
                
                if self.y > self.heading_towards[1]:
                    self.y += self.speed * math.sin(angle)
                else:
                    self.y -= self.speed * math.sin(angle)

        except ZeroDivisionError:
            
            if self.y > self.heading_towards[1]:
                angle = math.pi/2
                
            else:
                angle = 3*math.pi/2
            
            self.x += self.speed * math.cos(angle)
            if self.y > self.heading_towards[1]:
                self.y += self.speed * math.sin(angle)
            else:
                self.y -= self.speed * math.sin(angle)
        
            
        return False
