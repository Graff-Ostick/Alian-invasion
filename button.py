import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ai_setting = ai_settings

        self.width, self.height = 200, 50
        self.btn_color = (179, 16, 16)
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Lobster", 48, True, True)

        #self.triangle = pygame.draw.polygon(screen, self.btn_color, \
        #[[100, 100], [0, 200], [200, 200]], 5)
        #self.triangle.center = self.screen_rect.center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color,\
         self.btn_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        '''self.msg_image_triangle = self.msg_image.draw.polygon(screen, self.btn_color, \
        [[100, 100], [0, 200], [200, 200]], 5)

        self.msg_image_triangle.center = self.triangle.center'''


    def draw_button(self):
        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
