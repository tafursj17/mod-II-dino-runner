
from random import choice
import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            choices = (Cactus(SMALL_CACTUS[0]), Cactus(SMALL_CACTUS[1]), Cactus(SMALL_CACTUS[2]), Cactus(LARGE_CACTUS[0]), Cactus(LARGE_CACTUS[1]), Cactus(LARGE_CACTUS[2]))
            self.obstacles.append(random.choice(choices))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, obstacles=self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)