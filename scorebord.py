import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_settings
        self.stats = stats

        self.font_color = (71, 179, 50)
        self.font = pygame.font.SysFont("Lobster", 48, True, True)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.font_color, \
        self.ai_setting.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.high_score = str(self.stats.hight_score)
        self.high_score_img = self.font.render(self.high_score, True, self.font_color, self.ai_setting.bg_color)

        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.level), True, self.font_color, self.ai_setting.bg_color)

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right - 20
        self.level_rect.top = self.screen_rect.top

    def prep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_setting, self.screen)
            ship.image = ship.image
            ship.image = pygame.transform.scale(ship.image,(50, 50))
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def show_score(self):
        self.screen.blit(self.score_img, self.screen_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)
