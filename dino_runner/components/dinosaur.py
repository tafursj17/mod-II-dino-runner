import pygame
from dino_runner.components import game
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import DEAD, RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 10
    Y_POS_LIMIT = 140


    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
    
    def process_event(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP]:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True


    def update(self, user_input):
        self.process_event(user_input)
        if self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
        else:
            self.run()

        self.step += 1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        if self.step < 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS
        self.dino_rect.x = self.X_POS
    
    def duck(self):
        if self.step < 5:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS + 33
        self.dino_rect.x = self.X_POS
        self.dino_duck = False


    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.JUMP_VEL
        if self.dino_rect.y <= self.Y_POS_LIMIT:
            self.JUMP_VEL *= -1
        if self.dino_rect.y > self.Y_POS:
            self.JUMP_VEL *= -1
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False

       