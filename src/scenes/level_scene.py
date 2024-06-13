import pygame

from src.constants import WHITE, BG_COLOR, GAMEPLAY_GRAY, SHOW_HITBOX
from src.services.level_man import LevelMan
from src.services.spritesheet import SpriteSheet
from src.objs.player import Player
from src.scenes.scene import Scene

class LevelScene(Scene):

    """extends scene class. is used for level gameplay"""

    def __init__(self, screen):

        super().__init__(screen)

        self.player = Player(
            "gigi2",
            4,
            (0, 0),
            (14,34,13,13),
            sprite_height=64,
            render_scale=1.25
        )
        
        self.heart_sprite = SpriteSheet(pygame.image.load("assets/img/spritesheets/heart.png")).get_image(0,15,16,2)

        self.game_surface = pygame.Surface((600,688))

        self.player.relative_adjust(self.game_surface, x_relative_pos=(1/2), y_relative_pos=(3/4))
        self.projectiles=[]
        self.enemies=[]
        self.gui = []
        self.dialog = []
        self.level_id = 1
        self.level = LevelMan(self, self.level_id)
        self.score = 0
        self.starting_time = pygame.time.get_ticks()
        self.elapsed_time = self.starting_time
        self.state = 0
        self.player.invulnerability_timer = 0

        # sounds

        self.hurt_sound = pygame.mixer.Sound("assets/sounds/ouch.ogg")
        self.circle_sound = pygame.mixer.Sound("assets/sounds/circle.ogg")
        self.rain_sound = pygame.mixer.Sound("assets/sounds/rain.ogg")
        self.basic_sound = pygame.mixer.Sound("assets/sounds/shoot.ogg")
        

    def key_pressed(self, pressed):

        # deal with movements

        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.player.move("up")

        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.player.move("left")

        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            self.player.move("down")

        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.player.move("right")
            
        if pressed[pygame.K_SPACE]:
            self.dialog *= 0

    def update(self):

        self.elapsed_time = pygame.time.get_ticks() - self.starting_time
        self.level.update_events(self.elapsed_time)
        
        if self.player.invulnerability_timer > 0:
            self.player.invulnerability_timer -= 1 

        for projectile in self.projectiles:
            projectile.head_in_direction(projectile.direction, projectile.speed)

            if (projectile.hitbox_left > self.game_surface.get_width()) or (projectile.hitbox_right < 0) or (projectile.hitbox_top > self.game_surface.get_height()) or (projectile.hitbox_bottom < 0):
                self.projectiles.remove(projectile)
            
            if self.player.invulnerability_timer == 0:
                if self.player.hitbox_rect.colliderect(projectile.hitbox_rect):
                    self.projectiles.remove(projectile)
                    pygame.mixer.Sound.play(self.hurt_sound)
                    self.player.invulnerability_timer += 15
                
                    self.player.health -= 1

                    
        
        for enemy in self.enemies:
            
            if enemy.update_position():
                enemy.attack(self)

            if (enemy.hitbox_left > self.game_surface.get_width()) or (enemy.hitbox_right < 0) or (enemy.hitbox_top > self.game_surface.get_height()) or (enemy.hitbox_bottom < 0):
                self.enemies.remove(enemy)
                
        if (self.player.hitbox_left > self.game_surface.get_width()) or (self.player.hitbox_right < 0) or (self.player.hitbox_top > self.game_surface.get_height()) or (self.player.hitbox_bottom < 0):
                self.player.health -= 1
                self.player.relative_adjust(self.game_surface, x_relative_pos=(1/2), y_relative_pos=(3/4))
                self.player.invulnerability_timer += 120
        
        if self.player.health <= 0:
                    
            self.state = 4
        
        return self.state

    def render(self):
        
        self.game_surface.fill(GAMEPLAY_GRAY)
        self.screen.fill(BG_COLOR)

        self.player.display(self.game_surface, 0.1, show_hitbox=SHOW_HITBOX)

        for projectile in self.projectiles:
            projectile.display(self.game_surface, 0.1, show_hitbox=SHOW_HITBOX)

        for enemy in self.enemies:
            enemy.display(self.game_surface, 0.1, show_hitbox=SHOW_HITBOX)
            
        for element in self.gui:
            self.game_surface.blit(element[0], element[1])
            
        for element in self.dialog:
            self.game_surface.blit(element[0], element[1])
        
        for life in range(self.player.health):
            self.screen.blit(self.heart_sprite, (700+life*30, 100))

        self.screen.blit(self.game_surface, (32,32))
        
    

    
