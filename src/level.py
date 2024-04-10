import pygame
from src.objs.enemy import Enemy
import time


class Level:

    def __init__(self, scene, level_id=1):
        self.scene = scene

        # a list of tuples (time, list of events)
        self.level_events = [
            (0, [self.spawn_enemy], []),
            (1000, [self.rain_projectiles], []),
            (2000, [self.spawn_enemy], [])
        ]

    def update_events(self, elapsed_time):
        
        for event in self.level_events:

            if elapsed_time >= event[0]:
                for action in event[1]:
                    action(*event[3])
                self.level_events.remove(event)
                break

            else:
                break

    def rain_projectiles(self, num=16, offset=0):
        
        for i in range(num):
            self.scene.spawn_projectile("bullet_round", ((self.scene.game_surface.get_width()/num)*i+offset,0),relative_positioning_y=True,speed=3)

    def spawn_enemy(self, sprite, pos1, pos2):

        test_enemy = Enemy(
            sprite,
            4,
            (0,0),
            (14,34,12,12),
            sprite_height=64,
            render_scale=1.25
        )
        test_enemy.heading_towards = (150,150)
        self.scene.enemies.append(test_enemy)
