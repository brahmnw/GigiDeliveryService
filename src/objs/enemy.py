import pygame
import math

from src.objs.entity import Entity
from src.objs.projectile import Projectile
from src.services import util

class Enemy(Entity):

    """enemies will move to a position. do an attack. fuck right off."""

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)
        self.heading_towards = position
        self.end_position = (self.heading_towards[0], -100)
        self.movement_state = 0
        self.attack = self.circle_attack

    def update_position(self):

        try:
            angle = (math.atan((self.position[1] - self.heading_towards[1])/(self.heading_towards[0] - self.position[0]))) 

            if self.x > self.heading_towards[0]:
                angle += math.pi

            elif self.y >= self.heading_towards[1]:
                angle += math.pi

        except ZeroDivisionError:
            angle = math.pi/2

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

    def basic_attack(self, scene, direction=270):
        
        projectile = Projectile("bullet_round", 1, (self.hitbox_x_center,self.hitbox_y_center), (8,8,16,16))
        projectile.direction = direction
        scene.projectiles.append(projectile)

    def circle_attack(self, scene, count=12, starting_angle=0):
        
        for i in range(count):

            projectile = Projectile("bullet_round", 1, (self.hitbox_x_center,self.hitbox_y_center), (8,8,16,16))
            projectile.direction = starting_angle+(i*(360//(count)))-180
            scene.projectiles.append(projectile)


