import pygame

from src.objs.entity import Entity
from src.objs.projectile import Projectile

class Enemy(Entity):

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)

    def update_state(self):
        pass

    def basic_attack(self, scene, direction=270):
        
        projectile = Projectile("bullet_round", 1, (self.hitbox_x_center,self.hitbox_y_center), (8,8,16,16))
        projectile.direction = direction
        scene.projectiles.append(projectile)

    def circle_attack(self, scene, count=6, starting_angle=0):
        
        for i in range(count):

            projectile = Projectile("bullet_round", 1, (self.hitbox_x_center,self.hitbox_y_center), (8,8,16,16))
            projectile.direction = starting_angle+(i*(360//(count)))-180
            scene.projectiles.append(projectile)


