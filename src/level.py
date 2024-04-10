import pygame
from src.objs.enemy import Enemy
import time


class Level:

    def __init__(self, scene, level_id=1):
        self.scene = scene

        # a list of tuples (time, list of events)
        self.level_events = [
            (0, [self.spawn_enemy], ["gigi2", (250,0), (300,250)]),
            (50, [self.spawn_enemy], ["gigi2", (200,0), (300,250)]),
            (100, [self.spawn_enemy], ["gigi2", (300,0), (300,250)]),
            (150, [self.spawn_enemy], ["gigi2", (150,0), (300,250)]),
            (200, [self.spawn_enemy], ["gigi2", (350,0), (300,250)]),
            (2000, [self.spawn_enemy], ["gigi2", (0,0), (250, 150)]),
            (2200, [self.spawn_enemy], ["gigi2", (0,0), (300, 150)]),
            (2400, [self.spawn_enemy], ["gigi2", (0,0), (350, 150)]),
            (2600, [self.spawn_enemy], ["gigi2", (0,0), (400, 150)]),
            (3000, [self.rain_projectiles], [12,0]),
            (3200, [self.spawn_enemy], ["gigi2", (550,0), (350, 150)]),
            (3400, [self.spawn_enemy], ["gigi2", (550,0), (300, 150)]),
            (3600, [self.spawn_enemy], ["gigi2", (550,0), (250, 150)]),
            (3500, [self.rain_projectiles], [12,10]),
            (4000, [self.rain_projectiles], [12,20]),
            (5000, [self.rain_projectiles], [12,30])
        ]

    def update_events(self, elapsed_time):
        
        for event in self.level_events:

            if elapsed_time >= event[0]:
                for action in event[1]:
                    action(*event[2])
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
            pos1,
            (14,34,12,12),
            sprite_height=64,
            render_scale=1.25
        )
        test_enemy.heading_towards = pos2
        self.scene.enemies.append(test_enemy)
