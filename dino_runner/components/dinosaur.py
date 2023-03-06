import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310


    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step = 0

    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.duck()
        elif user_input[pygame.K_UP]:
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
        if self.step < 5 == 0:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS + 33
        self.dino_rect.x = self.X_POS

    def jump(self):
        self.image = JUMPING
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS - 100
        self.dino_rect.x = self.X_POS 
