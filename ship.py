import pygame
from pygame.sprite import Sprite

width = 100
height = 100

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/shp.png")
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def center_ship(self):
        '''self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery + (self.screen_rect.centery * 0.9)
        self.rect.bottom = self.rect.y
        '''

        self.center_x = self.screen_rect.centerx
        self.center_y =self.screen_rect.centery + self.screen_rect.centery * 0.9



    def blitme(self):
        self.screen.blit(self.image, self.rect)
