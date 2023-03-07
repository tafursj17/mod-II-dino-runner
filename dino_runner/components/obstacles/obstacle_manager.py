
from random import choice
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            choices = (Cactus(SMALL_CACTUS[1]), Cactus(SMALL_CACTUS[0]))
            self.obstacles.append(choice(choices))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, obstacles=self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)