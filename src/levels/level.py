import pygame
from src.objs.enemy import Enemy
import time


class Level:

    def __init__(self, scene, level_id=1):
        self.scene = scene
        
        self.start_time = time.time()

        # a list of tuples (time, event)
        self.level_events = [
            (0, 9)
        ]

    def update_events(self):
        pass

    def spawn_enemy(self):

        test_enemy = Enemy(
            "gigi2",
            4,
            (self.game_surface.get_width()/2,self.game_surface.get_height()/4),
            (14,34,12,12),
            sprite_height=64,
            render_scale=1.25
        )
        self.scene.enemies.append(test_enemy)
        test_enemy.circle_attack(self, 10)
