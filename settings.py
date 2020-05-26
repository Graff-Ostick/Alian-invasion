class Settings():
    def __init__(self):
        #screen
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (67, 51, 97)

        #ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (252, 57, 3)
        self.bullets_alowed = 6


        #star
        self.count_stars = 30

        #Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_directions = 1

        #speed game

        self.speedup = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_spped_factor = 2
        self.alien_speed_factor = 1
        self.fleet_directions = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup
        self.bullet_spped_factor *= self.speedup
        self.alien_speed_factor *= self.speedup
        self.fleet_directions = self.speedup
