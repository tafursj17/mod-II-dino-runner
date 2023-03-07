import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        posiciones = [300, 260, 200]
        pos = random.choice(posiciones)
        self.rect.y = pos
        self.step = 0
    
    def update(self, game_speed, obstacles):
        if self.step < 5:
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]
        
        super().update(game_speed, obstacles) #Ejecuta clase padre
        self.step += 1
        if self.step == 10:
            self.step = 0


    