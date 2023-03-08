import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.text_utils import get_centered_message, get_dead_dinosaur, get_score_element


class Game:
    INITIAL_SPEED = 20
    INITIAL_DEAD = 0
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.INITIAL_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.deads = self.INITIAL_DEAD

    def show_score(self):
        self.points += 1
        
        if self.points % 100 == 0:
            self.game_speed += 1

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_deads(self):
        dead, dead_rect = get_dead_dinosaur(self.deads)
        self.screen.blit(dead, dead_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        text, text_rect = get_centered_message('Press any Key to Start!!')
        self.screen.blit(text, text_rect)
        self.show_deads()
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                
                print('Game Over')
                pygame.quit()
                self.deads = self.INITIAL_DEAD
           
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(500)
        self.playing = False
        self.points = 0
        self.game_speed = self.INITIAL_SPEED
        self.obstacle_manager.remove_obstacles()
        # self.deads += 1

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.show_score()
        self.show_deads()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
