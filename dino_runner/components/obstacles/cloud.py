import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cloud(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        posiciones = [50, 80, 100]
        pos = random.choice(posiciones)
        self.rect.y = pos

        posiciones = [ 900, 1300]
        pos_x = random.choice(posiciones)
        self.rect.x = pos_x
        