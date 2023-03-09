
from random import choice
import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus, CactusLarge
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.utils.constants import BIRD, CLOUD, DEAD, HAMMER_TYPE, LARGE_CACTUS, SHIELD_TYPE, SMALL_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.obstacles_pasive = []

    def update(self, game):

        if len(self.obstacles) == 0:

            choices = (Cactus(SMALL_CACTUS[0]),Cactus(SMALL_CACTUS[1]), Cactus(SMALL_CACTUS[2]), CactusLarge(LARGE_CACTUS[0]), CactusLarge(LARGE_CACTUS[1]), CactusLarge(LARGE_CACTUS[2]), Bird(BIRD[0]))
            self.obstacles.append(random.choice(choices))

            cloud_object = Cloud(CLOUD)
            self.obstacles_pasive.append(cloud_object)
        
        for obstacle in self.obstacles_pasive:
            obstacle.update(game.game_speed, obstacles=self.obstacles_pasive)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, obstacles=self.obstacles)
            if game.player.type == SHIELD_TYPE:
                pass
            elif game.player.dino_rect.colliderect(obstacle.rect) and game.player.type == HAMMER_TYPE:
                self.obstacles.pop()
            elif game.player.dino_rect.colliderect(obstacle.rect):
                game.player.image = DEAD[0]
                game.deads += 1
                game.playing = False

    def draw(self, screen):
        for obstacle in (self.obstacles):
            obstacle.draw(screen)
        
        for obstacle in (self.obstacles_pasive):
            obstacle.draw(screen)
        
    def remove_obstacles(self):
        self.obstacles = []    
        self.obstacles_pasive = [] 