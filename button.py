import pygame.font


class Button:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.msg_image = pygame.image.load('images/play_button.bmp')
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)