import random
from src.objs.enemy import Enemy

class Mobster(Enemy):

    def __init__(self, sprite_name:str, sprite_animation_frames:int, position:tuple, hitbox_args:tuple, render_scale=1, speed=2, sprite_width=32, sprite_height=32):
        super().__init__(sprite_name, sprite_animation_frames, position, hitbox_args, render_scale, speed, sprite_width, sprite_height)

    def attack_player(self, scene):
        for _ in range(15):
            scene.spawn_projectile('bullet_round', (random.randint(1,self.screen.get_width()),random.randint(0,1)), relative_positioning_y=True)
        scene.projectiles
