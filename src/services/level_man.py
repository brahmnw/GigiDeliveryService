import json
import importlib
import math
import pygame
import textwrap

from src.constants import DIALOGUE_COLOR, WHITE
from src.objs.enemies.drone import Drone
from src.objs.projectile import Projectile
from src.services.spritesheet import SpriteSheet


class LevelMan:

    def __init__(self, scene, level_id=2):
        self.scene = scene
        self.TITLE_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 24)
        self.SUBTITLE_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 12)
        self.NAME_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 20)
        self.DIALOGUE_FONT = pygame.freetype.Font("assets/fonts/VictorMono-Bold.ttf", 12)

        # a list of tuples (time, event, args)
        self.level_events = [

        ]
        
        with open('orders/{0}/order.json'.format(level_id)) as f:
            self.level_dict = json.load(f)
            
            title_str = "ORDER {0}: {1}".format(level_id, self.level_dict['recipient'])
            subtitle_str = self.level_dict['order_details']
            self.level_events.append((500, self.show_stage_text, (title_str, subtitle_str)))
            self.level_events.append((2000, self.clear_gui, ()))
            
            for i in range(3):
                self.level_events.append((2100+i*200, self.show_stage_text, (title_str, subtitle_str)))
                self.level_events.append((2200+i*200, self.clear_gui, ()))
            
            for level in self.level_dict['level_events']:
                
                event = getattr(self, level[1])
                
                self.level_events.append((level[0]+3000, event, level[2]))
            
            boss = importlib.import_module(f"orders.{level_id}.{self.level_dict['boss']}")
            
            self.boss = boss.Boss()
            

    def update_events(self, elapsed_time):
        
        self.scene.level_conditions = ['LOSE!', elapsed_time-3000, self.level_dict['length'], 0]
        
        for event in self.level_events:

            if elapsed_time >= event[0]:
                event[1](*event[2])
                self.level_events.remove(event)
                break

            else:
                break
            
    def end_level(self):
        self.scene.level_conditions = ['WIN!', self.level_dict['length'], self.level_dict['length'], self.scene.player.health]
        self.scene.state = 4
            
    def clear_gui(self) -> None:
        
        self.scene.gui *= 0
        
    def clear_dialogue(self) -> None:
        
        self.scene.dialog *= 0
        
    def show_dialogue_text(self, dialogue_num, dialogue=[]) -> None:
        
        self.scene.dialog *= 0
        
        dialogue_surface = pygame.Surface((560, 175))
        dialogue_surface.fill(DIALOGUE_COLOR)
        dialogue_surface.set_alpha(191)
        
        sprite_surface = pygame.Surface((100,100))
        sprite_surface.fill(WHITE)
        dialogue_surface.blit(sprite_surface, (25,50))
        
        if dialogue_num is None:
            dialogue = dialogue
            
        else:
            dialogue = self.level_dict['voicelines'][dialogue_num]
        
        lines = textwrap.wrap(dialogue[1], 58)
        
        line_counter = 0
        
        for line in lines:
            
            text_surface, _ = self.DIALOGUE_FONT.render(line,
            (255,255,255)
            )
            
            dialogue_surface.blit(text_surface, (150, 50+20*line_counter))
            
            line_counter += 1
        
        name_surface, _ = self.NAME_FONT.render(dialogue[0],(255,255,255))
        dialogue_surface.blit(name_surface, (25, 15))
        
        self.scene.dialog.append([dialogue_surface, (20,self.scene.game_surface.get_height()-205)])
        
    def show_stage_text(self, title, subtitle) -> None:
        
        title_surface, _ = self.TITLE_FONT.render(title,(255,255,255))
        subtitle_surface, _ = self.SUBTITLE_FONT.render(subtitle,(255,255,255))
        
        t_left_adj = (24*len(title)/4)+24
        st_left_adj = (12*len(subtitle)/4)+24
        
        self.scene.gui.append([title_surface, ((1/2)*(self.scene.game_surface.get_width())-t_left_adj, self.scene.game_surface.get_height()/2-25)])
        self.scene.gui.append([subtitle_surface, ((1/2)*(self.scene.game_surface.get_width())-st_left_adj, self.scene.game_surface.get_height()/2+25)])
    
    def rain_projectiles(self, num=16, offset=0) -> None:
        
        for i in range(num):
            self.spawn_projectile("bullet_round", ((self.scene.game_surface.get_width()/num)*i+offset,0),relative_positioning_y=True,speed=3)
    
    def spawn_boss(self) -> None:
        x = self.level_events[-2][0]
        for move in self.boss.moves:
            
            move[0] += x
            if move[1].startswith('boss.'):
                move[1] = getattr(self.boss, move[1][5:])
                move[2].insert(0, self.scene)
            else:
                move[1] = getattr(self, move[1])
        
            self.level_events.append(move)
        
        
        self.level_events.sort(key=lambda x: int(x[0]))
            
        self.scene.enemies.append(self.boss)
        
    def spawn_drone(self, sprite, pos1, pos2) -> None:

        drone = Drone(
            sprite,
            2,
            pos1,
            (14,14,12,12),
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
        
    def boss_set_heading(self, pos1, pos2):
        self.boss.heading_towards = (pos1,pos2)
    
    
