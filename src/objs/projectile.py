import math

from src.objs.entity import Entity

class Projectile(Entity):

    """
    Projectile extends Entity -> used for smaller objects that can collide with the player
    """

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, direction=-90, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        
        # initialize entity and set the position of x/y
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)
        self.direction=direction

    def head_in_direction(self, angle, speed):

        angle = angle * (math.pi/180)

        move_x = speed * math.cos(angle)
        move_y = speed * math.sin(angle)

        self.x += move_x
        self.y -= move_y

        self.update_hitbox()
