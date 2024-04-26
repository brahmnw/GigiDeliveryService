import json
import pygame
from src.objs.enemies.drone import Drone
from src.objs.projectile import Projectile
import time


class Level:

    def __init__(self, scene, level_id=1):
        self.scene = scene

        # a list of tuples (time, event, args)
        self.level_events = [

        ]
        
        with open('orders/{0}/order.json'.format(level_id)) as f:
            self.level_dict = json.load(f)
            
            for level in self.level_dict['level_events']:
                
                event = getattr(self, level[1])
                
                self.level_events.append((level[0], event, level[2]))
            

    def update_events(self, elapsed_time):
        
        for event in self.level_events:

            if elapsed_time >= event[0]:
                event[1](*event[2])
                self.level_events.remove(event)
                break

            else:
                break
    
    def rain_projectiles(self, num=16, offset=0):
        
        for i in range(num):
            self.spawn_projectile("bullet_round", ((self.scene.game_surface.get_width()/num)*i+offset,0),relative_positioning_y=True,speed=3)
            
    def spawn_drone(self, sprite, pos1, pos2):

        drone = Drone(
            sprite,
            4,
            pos1,
            (14,34,12,12),
            sprite_height=64,
            render_scale=1.25
        )
        drone.heading_towards = pos2
        self.scene.enemies.append(drone)
        
    def spawn_projectile(self, projectile_name, position, hitbox=(8,8,16,16), speed=3, relative_positioning_x=False, relative_positioning_y=False, direction=-90):
        
        projectile = Projectile(projectile_name, 1, (0,0), hitbox, direction=direction, speed=speed)
        projectile.x = position[0]
        projectile.y = position[1]
        
        if relative_positioning_y:
            
            projectile.relative_adjust(self.scene.game_surface, y_relative_pos=position[1])

        if relative_positioning_x:
            
            projectile.relative_adjust(self.scene.game_surface, x_relative_pos=position[0])

        self.scene.projectiles.append(projectile)
    
    

    
