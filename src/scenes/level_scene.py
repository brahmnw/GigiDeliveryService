import pygame

from src.constants import BLACK, WHITE
from src.game_entities.player import Player
from src.scenes.scene import Scene

class LevelScene(Scene):

    """extends scene class. is used for level gameplay"""

    def __init__(self, screen):
        super().__init__(screen)
        self.player = Player("gigi", (screen.get_width() * (1/2), screen.get_height() * (3/4)))

    def process_input(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()

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
        pass

    def render(self):
        self.screen.fill(WHITE)
        self.player.display(self.screen)