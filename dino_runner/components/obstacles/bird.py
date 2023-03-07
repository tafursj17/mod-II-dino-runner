import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        posiciones = [300, 260, 200]
        pos = random.choice(posiciones)
        self.rect.y = pos
