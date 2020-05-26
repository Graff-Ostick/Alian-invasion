import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scorebord import Scoreboard


import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))

    pygame.display.set_caption("Alian Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_group = Group()
    star = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    score = Scoreboard(ai_settings, screen, stats)

    gf.create_star(ai_settings, screen, star)
    gf.create_fleet(ai_settings, screen, alien_group, ship)
    gf.update_display(ai_settings, screen, star, alien_group, ship, bullets, stats, score, play_button)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, score)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,  ai_settings, alien_group, screen, ship, stats, score)
            gf.update_aliens(ai_settings, stats, screen, ship, alien_group, bullets, score)

            gf.update_display(ai_settings, screen, star, alien_group, ship, bullets, stats, score, play_button)


run_game()
