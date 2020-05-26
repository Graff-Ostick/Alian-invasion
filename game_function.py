import sys
import pygame
import random
from time import sleep
from bullet import Bullet
from alien import Alien
from star import Star

def check_keydown_event(event, ai_settings, screen, ship, bullets, score, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_RETURN:
        play_game(ai_settings, stats, score)
        print("enter")
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_play_button(ai_settings, stats, play_button, mouse_x, mouse_y, score):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and \
    not stats.game_active:
        play_game(ai_settings, stats, score)

def play_game(ai_settings, stats, score):
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        score.prep_level()
        score.prep_score()
        score.prep_ship()




def fire_bullet(ai_settings, screen, ship, bullets):
    if ai_settings.bullets_alowed > len(bullets):
        left_bullet = Bullet(ai_settings, screen, ship)
        left_bullet.rect.centerx = left_bullet.rect.centerx-5
        right_bullet = Bullet(ai_settings,screen, ship)
        right_bullet.rect.centerx = right_bullet.rect.centerx+5
        bullets.add(right_bullet)
        bullets.add(left_bullet)

def update_bullets(bullets,  ai_settings, alien_group, screen, ship, stats, score):
    bullets.update()

    for bullet in bullets:
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, alien_group, ship, bullets,\
    stats, score)

def check_bullet_alien_collision(ai_settings, screen, alien_group, ship, bullets,\
stats, score):
    collisions = pygame.sprite.groupcollide(bullets, alien_group, True, True)

    if collisions:
        for alien in collisions.values():
            stats.score +=1
            score.prep_score()
            check_hight_score(stats, score)

    if len(alien_group)==0:
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, alien_group, ship)
        stats.level += 1
        score.prep_level()
        bullets.empty()

def get_number_of_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_of_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height \
     - (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / (2*alien_height))

    return number_rows

def create_alien(ai_settings, screen, alien_group, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
    alien_group.add(alien)

def create_fleet(ai_settings, screen, alien_group, ship):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_of_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x ):
            create_alien(ai_settings,screen,alien_group,alien_number, row_number)

def check_fleet_edges(ai_settings, alien_group):
    for alien in alien_group.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, alien_group)
            break

def change_fleet_direction(ai_settings, alien_group):
    for alien in alien_group.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_directions *= -1

def update_aliens(ai_settings, stats, screen, ship, alien_group, bullets, score):
    check_fleet_edges(ai_settings, alien_group)
    alien_group.update()
    if pygame.sprite.spritecollideany(ship, alien_group):
        ship_hit(ai_settings, stats, screen, ship, alien_group, bullets, score)
    check_alien_bottom(ai_settings, stats, screen, ship, alien_group, bullets)

def ship_hit(ai_settings, stats, screen, ship, alien_group, bullets, score):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        alien_group.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, alien_group, ship)
        ship.center_ship()
        score.prep_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(ai_settings, stats, screen, ship, alien_group, bullets):
    screen_rect = screen.get_rect()
    for alien in alien_group.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, alien_group, bullets, score)
            break


def check_events(ai_settings, screen, ship, bullets, stats, play_button, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==  pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets,  score, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button, mouse_x, mouse_y, score)

def create_star(ai_settings, screen, star_group):

    for row in range(ai_settings.count_stars):
        star = Star(ai_settings, screen)
        star_width = star.rect.width
        star_height = star.rect.height

        count_star_x = int(ai_settings.screen_width / star_width)
        count_star_y = int(ai_settings.screen_height / star_height)

        random_x = random.randint(0,count_star_x)
        random_y = random.randint(0,count_star_y)

        star.x = star_width * (random_x)
        star.rect.x = star.x
        star.rect.y = star.rect.height * (random_y)
        star_group.add(star)

def check_hight_score(stats, score):
     if stats.score > stats.hight_score:
         stats.hight_score = stats.score
         score.prep_high_score()


def update_display(ai_settings,screen, star,aliens, ship,bullets, stats, score, play_button):
    screen.fill(ai_settings.bg_color)
    star.draw(screen)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
