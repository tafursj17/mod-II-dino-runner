import pygame
from dino_runner.components import game
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import DEAD, DEFAULT_TYPE, SHIELD_TYPE ,RUNNING, DUCKING, JUMPING
from dino_runner.utils.constants import RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 10
    Y_POS_LIMIT = 140
    POWER_UP_TIME = 100

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.type = DEFAULT_TYPE
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.power_up_time = 0
    
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

        self.power_up_time -= 1
        if self.power_up_time < 0:
            self.type = DEFAULT_TYPE

        self.step += 1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        if self.step < 5:
            self.image = self.run_img[self.type][0]
        else:
            self.image = self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS
        self.dino_rect.x = self.X_POS
    
    def duck(self):
        if self.step < 5:
            self.image = self.duck_img[self.type][0]
        else:
            self.image = self.duck_img[self.type][1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.y = self.Y_POS + 33
        self.dino_rect.x = self.X_POS
        self.dino_duck = False


    def jump(self):
        self.image = self.jump_img[self.type]
        self.dino_rect.y -= self.JUMP_VEL
        if self.dino_rect.y <= self.Y_POS_LIMIT:
            self.JUMP_VEL *= -1
        if self.dino_rect.y > self.Y_POS:
            self.JUMP_VEL *= -1
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False

    def active_power_up(self, power_up_type):
        if power_up_type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.power_up_time = self.POWER_UP_TIME