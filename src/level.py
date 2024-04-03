import pygame
from src.objs.enemy import Enemy
import time


class Level:

    def __init__(self, scene, level_id=1):
        self.scene = scene

        # a list of tuples (time, list of events)
        self.level_events = [
            (0, [self.spawn_enemy]),
            (1000, [self.rain_projectiles]),
            (1200, [self.rain_projectiles]),
            (1400, [self.rain_projectiles]),
            (1600, [self.rain_projectiles]),
            (1800, [self.rain_projectiles]),
            (2000, [self.spawn_enemy,self.spawn_enemy])
        ]

    def update_events(self, elapsed_time):
        
        for event in self.level_events:

            if elapsed_time >= event[0]:
                for action in event[1]:
                    action()
                self.level_events.remove(event)
                break

            else:
                break

    def rain_projectiles(self, num=16, offset=5):
        
        for i in range(num):
            self.scene.spawn_projectile("bullet_round", ((self.scene.game_surface.get_width()/num)*i+offset,0),relative_positioning_y=True,speed=3)

    def spawn_enemy(self):

        test_enemy = Enemy(
            "gigi2",
            4,
            (self.scene.game_surface.get_width()/2,self.scene.game_surface.get_height()/4),
            (14,34,12,12),
            sprite_height=64,
            render_scale=1.25
        )
        self.scene.enemies.append(test_enemy)
        test_enemy.circle_attack(self.scene, 10)
