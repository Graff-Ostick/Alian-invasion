import pygame
from pygame.sprite import Sprite
import random

width = 25
height = 25
color_of_stars = ["images/star.png","images/star1.png","images/star2.png"]

class Star(Sprite):
    def __init__(self, ai_setting, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load(random.choice(color_of_stars))
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)
