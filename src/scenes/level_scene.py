import pygame
import random

from src.constants import WHITE, BG_COLOR
from src.objs.enemy import Enemy
from src.objs.player import Player
from src.objs.projectile import Projectile
from src.scenes.scene import Scene

class LevelScene(Scene):

    """extends scene class. is used for level gameplay"""

    def __init__(self, screen, clock):

        super().__init__(screen, clock)

        self.player = Player(
            "gigi2",
            4,
            (0, 0),
            (14,34,13,13),
            sprite_height=64,
            render_scale=1.25
        )

        self.game_surface = pygame.Surface((600,688))

        self.player.relative_adjust(self.game_surface, x_relative_pos=(1/2), y_relative_pos=(3/4))
        self.projectiles=[]
        self.enemies=[]

        self.CREATE_PROJECTILE = pygame.USEREVENT
        self.current_level = 1
        self.score = 0


    def process_input(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.terminate()

            if event.type == self.CREATE_PROJECTILE:

                for _ in range(20):
                    self.spawn_projectile('bullet_round', (random.randint(1,self.screen.get_width()),random.randint(0,1)), relative_positioning_y=True)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    test_enemy = Enemy(
                        "gigi2",
                        4,
                        (self.game_surface.get_width()/2,self.game_surface.get_height()/4),
                        (14,34,12,12),
                        sprite_height=64,
                        render_scale=1.25
                    )
                    self.enemies.append(test_enemy)
                    test_enemy.circle_attack(self, 10)

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.player.move("up")

        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.player.move("left")

        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            self.player.move("down")

        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.player.move("right")

    def update(self):

        self.score += 1

        for projectile in self.projectiles:
            projectile.head_in_direction(projectile.direction, projectile.speed)

            if (projectile.hitbox_left > self.screen.get_width()) or (projectile.hitbox_right < 0) or (projectile.hitbox_top > self.screen.get_height()) or (projectile.hitbox_bottom < 0):
                self.projectiles.remove(projectile)

            if self.player.hitbox_rect.colliderect(projectile.hitbox_rect):
                self.projectiles.remove(projectile)
                
                self.player.health -= 1

                if self.player.health <= 0:
                    print("YOU SUCK!!! Score: {}".format(self.score))
                    self.terminate()

    def render(self):
        
        
        self.game_surface.fill(WHITE)
        self.screen.fill(BG_COLOR)

        self.player.display(self.game_surface, 0.1, show_hitbox=True)

        for projectile in self.projectiles:
            projectile.display(self.game_surface, 0.1, show_hitbox=True)

        for enemy in self.enemies:
            enemy.display(self.game_surface, 0.1, show_hitbox=True)

        self.screen.blit(self.game_surface, (32,32))

    def spawn_projectile(self, projectile_name, position, hitbox=(8,8,16,16), relative_positioning_x=False, relative_positioning_y=False, direction=-90):
        projectile = Projectile(projectile_name, 1, (0,0), hitbox, direction=direction)
        projectile.x = position[0]
        projectile.y = position[1]
        
        if relative_positioning_y:
            
            projectile.relative_adjust(self.game_surface, y_relative_pos=position[1])

            if position[1] == 1:
                projectile.direction = random.randint(0,180)
            
            if position[1] == 0:
                projectile.direction = random.randint(-180,0)

        if relative_positioning_x:
            
            projectile.relative_adjust(self.game_surface, y_relative_pos=position[1])

            if position[1] == 1:
                projectile.direction = random.randint(0,180)
            
            if position[1] == 0:
                projectile.direction = random.randint(-180,0)

        self.projectiles.append(projectile)
