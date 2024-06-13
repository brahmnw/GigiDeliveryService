import math

import random

from src.objs.enemy import Enemy
from src.objs.projectile import Projectile
from src.services import util
from pickle import FALSE

class Boss(Enemy):
    
    """dhar man"""
    
    def __init__(self):
        super().__init__("dhar-hero-3", 1, (300,0), (25,25,1,1), 0.05, sprite_width=997, sprite_height=1394)
        self.heading_towards = (310,400)
        self.speed = 5
        self.moves = [
            [0, 'boss_set_heading', [310,400]],
            [2000, 'boss.circle_attack', []],
            [2100, 'boss_set_heading', [100,100]],
            [2300, 'boss.basic_attack', []],
            [2400, 'show_dialogue_text', [
                None, 
                ["dhar mann", "What's up dhar mann fam!", "phone_guy.png"]
            ]],
            [2500, 'rain_projectiles', [10, 10]],
            [2600, 'boss.basic_attack', []],
            [2700, 'boss.basic_attack', []],
            [2800, 'boss.basic_attack', []],
            [3000, 'boss.circle_attack', []],
            [3500, 'boss_set_heading', [450,500]],
            [5000, 'boss.circle_attack', [12, 20]],
            [5100, 'clear_dialogue', []],
            [5500, 'rain_projectiles', [10, 0]],
            [6000, 'boss_set_heading', [300,250]],
            [6500, 'boss.circle_attack', [12, 30]],
            [6600, 'boss.basic_attack', []],
            [6700, 'boss.basic_attack', []],
            [6800, 'boss.basic_attack', []],
            [7000, 'boss.circle_attack', [12, 10]],
            [7100, 'show_dialogue_text', [
                None, 
                ["dhar mann", "that's it. i've had it up to here with you. angry mode activated.", "phone_guy.png"]
            ]],
            [10000, 'clear_dialogue', []],
            [10500, 'rain_projectiles', [10, 0]],
            [11000, 'rain_projectiles', [10, 10]],
            [11000, 'boss.circle_attack', []],
            [11500, 'rain_projectiles', [10, 20]],
            [11500, 'boss.circle_attack', [12, 0]],
            [11600, 'boss.circle_attack', [12, 20]],
            [11700, 'boss.circle_attack', [12, 40]],
            [12000, 'rain_projectiles', [10, 30]],
            [12500, 'rain_projectiles', [10, 40]],
            [13000, 'boss.circle_attack', []],
            [13000, 'rain_projectiles', [10, 50]],
            [13500, 'rain_projectiles', [10, 60]],
            [14500, 'boss.circle_attack', [12, 0]],
            [14600, 'boss.circle_attack', [12, 5]],
            [14700, 'boss.circle_attack', [12, 10]],
            [14800, 'boss.circle_attack', [12, 15]],
            [15000, 'boss.circle_attack', [12, 20]],
            [15500, 'rain_projectiles', [10, 0]],
            [16500, 'boss.circle_attack', [12, 0]],
            [16600, 'boss.circle_attack', [12, 5]],
            [16700, 'boss.circle_attack', [12, 10]],
            [16800, 'boss.circle_attack', [12, 15]],
            [17000, 'boss.circle_attack', [12, 20]],
            [18000, 'rain_projectiles', [10, 30]],
            [18500, 'boss.circle_attack', [12, 0]],
            [18500, 'rain_projectiles', [10, 40]],
            [18600, 'boss.circle_attack', [12, 5]],
            [18700, 'boss.circle_attack', [12, 10]],
            [18800, 'boss.circle_attack', [12, 15]],
            [19000, 'boss.circle_attack', [12, 20]],
            [19000, 'boss.circle_attack', []],
            [19500, 'rain_projectiles', [10, 50]],
            [20000, 'rain_projectiles', [10, 60]],
            [20800, 'boss.circle_attack', [12, 15]],
            [21000, 'boss.circle_attack', [12, 20]],
            [22000, 'rain_projectiles', [10, 30]],
            [22500, 'boss.circle_attack', [12, 0]],
            [22500, 'rain_projectiles', [10, 40]],
            [22600, 'boss.circle_attack', [12, 5]],
            [22700, 'boss.circle_attack', [12, 10]],
            [22800, 'boss.circle_attack', [12, 15]],
            [22000, 'boss.circle_attack', [12, 20]],
            [23000, 'boss.circle_attack', []],
            [24500, 'rain_projectiles', [10, 50]],
            [24600, 'rain_projectiles', [10, 60]],
            [25000, 'show_dialogue_text', [
                None, 
                ["Dhar Mann", "okay im tired now. deliver your damn pizza.", "dharmann.png"]
            ]],
            [26000, 'boss_set_heading', [450,-500]],
            [30000, 'show_dialogue_text', [
                None, 
                ["mimi", "omg thanks so much for the pizzas lol", "mimi.png"]
            ]],
        ]
    
    
    def update_position(self):
        
        angle = util.position_to_angle((self.x,self.y), self.heading_towards)

        if util.position_is_close((self.x,self.y), self.heading_towards):
            return False
        
        else:
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)

        self.update_hitbox()

        return False
