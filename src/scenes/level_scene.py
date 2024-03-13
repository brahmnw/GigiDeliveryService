import pygame
import random

from src.constants import WHITE
from src.objs.player import Player
from src.objs.projectile import Projectile
from src.scenes.scene import Scene

class LevelScene(Scene):

    """extends scene class. is used for level gameplay"""

    def __init__(self, screen):

        super().__init__(screen)

        self.player = Player(
            "gigi",
            2,
            (0, 0),
            (41,41,20,20),
            render_scale=3
        )

        self.player.relative_adjust(screen, x_relative_pos=(1/2), y_relative_pos=(3/4))
        self.projectiles=[]


    def process_input(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.terminate()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    for _ in range(10):
                        self.spawn_projectile('pizza', ((1/random.randint(1,5)),random.randint(0,1)), relative_positioning=True)


        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            self.player.move("up")

        if pressed[pygame.K_a]:
            self.player.move("left")

        if pressed[pygame.K_s]:
            self.player.move("down")

        if pressed[pygame.K_d]:
            self.player.move("right")

    def update(self):

        player_collision = False

        for projectile in self.projectiles:
            projectile.head_in_direction(projectile.direction, 5)

            if (projectile.hitbox_left > self.screen.get_width()) or (projectile.hitbox_right < 0) or (projectile.hitbox_top > self.screen.get_height()) or (projectile.hitbox_bottom < 0):
                self.projectiles.remove(projectile)

            if self.player.hitbox_rect.colliderect(projectile.hitbox_rect):
                self.projectiles.remove(projectile)
                
                self.player.health -= 1

                if self.player.health <= 0:
                    self.terminate()

                print('---\nCOLLISION DETECTED!\nProjectiles: {0}\nPlayerCollision: {1}\nHealth: {2}'.format(self.projectiles, player_collision, self.player.health))

        #print('FRAME UPDATED!\nProjectiles: {0}\nPlayerCollision: {1}'.format(self.projectiles, player_collision))

    def render(self):
        self.screen.fill(WHITE)
        self.player.display(self.screen, 0.1, show_hitbox=True)

        for projectile in self.projectiles:
            projectile.display(self.screen, 0.1, show_hitbox=True)

    def spawn_projectile(self, projectile_name, position, relative_positioning=True, direction=-90):

        if relative_positioning:
            projectile = Projectile(projectile_name, 1, (0,0), (8,8,16,16), direction=direction)
            projectile.relative_adjust(self.screen, x_relative_pos=position[0], y_relative_pos=position[1])

            if position[1] == 1:
                projectile.direction = random.randint(0,180)
            
            if position[1] == 0:
                projectile.direction = random.randint(-180,0)

        else:
            projectile = Projectile(projectile_name, 1, position, (8,8,16,16), direction=direction)

        self.projectiles.append(projectile)
